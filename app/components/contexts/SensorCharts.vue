<template>
  <div class="sensor-charts">
    <!-- Grid capteurs -->
    <div class="grid-2 animate-fade-up">
      <div class="card sensor-card">
        <p class="sensor-label">Temp. air</p>
        <p class="sensor-value">{{ sensors.airTemp }}<span class="sensor-unit">°C</span></p>
        <span class="badge badge--low">↑ +0.8°</span>
      </div>
      <div class="card sensor-card">
        <p class="sensor-label">Temp. sol</p>
        <p class="sensor-value">{{ sensors.soilTemp }}<span class="sensor-unit">°C</span></p>
        <span class="badge badge--stable">Stable</span>
      </div>
      <div class="card sensor-card delay-1 animate-fade-up">
        <p class="sensor-label">Hum. air</p>
        <p class="sensor-value">{{ sensors.airHumidity }}<span class="sensor-unit">%</span></p>
        <span class="badge badge--high">↑ Élevé</span>
      </div>
      <div class="card sensor-card delay-1 animate-fade-up">
        <p class="sensor-label">Hum. sol</p>
        <p class="sensor-value">{{ sensors.soilHumidity }}<span class="sensor-unit">%</span></p>
        <span class="badge badge--low">Optimal</span>
      </div>
    </div>

    <!-- Graphique température -->
    <div class="card delay-2 animate-fade-up">
      <p class="section-label">Température — 24H</p>
      <div class="chart-container">
        <canvas ref="tempChartRef" height="110"></canvas>
      </div>
      <div class="chart-axis">
        <span v-for="h in xLabels" :key="h" class="chart-tick">{{ h }}</span>
      </div>
    </div>

    <!-- Humidité comparée -->
    <div class="card delay-3 animate-fade-up">
      <p class="section-label">Humidité comparée</p>
      <div class="humidity-bars">
        <div class="hum-row">
          <span class="hum-label">Air</span>
          <div class="progress-bar flex-1">
            <div class="progress-fill progress-fill--blue" :style="{ width: sensors.airHumidity + '%' }"></div>
          </div>
          <span class="hum-value">{{ sensors.airHumidity }}%</span>
        </div>
        <div class="hum-row">
          <span class="hum-label">Sol</span>
          <div class="progress-bar flex-1">
            <div class="progress-fill progress-fill--green" :style="{ width: sensors.soilHumidity + '%' }"></div>
          </div>
          <span class="hum-value">{{ sensors.soilHumidity }}%</span>
        </div>
        <div class="hum-row">
          <span class="hum-label">Feuilles</span>
          <div class="progress-bar flex-1">
            <div class="progress-fill progress-fill--orange" :style="{ width: sensors.leafHumidity + '%' }"></div>
          </div>
          <span class="hum-value">{{ sensors.leafHumidity }}%</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useSensorData } from '../../composables/useSensorData'

const { sensors } = useSensorData()

const tempChartRef = ref(null)
// const tempChartRef = ref<HTMLCanvasElement| null>(null)

let chartInstance: any = null

const xLabels = ['00', '03', '06', '09', '12', '15', '18', '21', '24']

const tempData = [6.8, 6.5, 6.2, 7.1, 9.4, 12.8, 15.6, 16.4, 15.9, 14.2, 12.1, 10.3, 9.1, 8.4, 7.9, 7.4]

onMounted(async () => {
  if (!tempChartRef.value) return
  try {
    const { Chart, registerables } = await import('chart.js')
    Chart.register(...registerables)

    chartInstance = new Chart(tempChartRef.value, {
      type: 'line',
      data: {
        labels: Array.from({ length: 16 }, (_, i) => `${(i * 1.5).toFixed(0)}h`),
        datasets: [{
          data: tempData,
          borderColor: '#60a5fa',
          backgroundColor: 'rgba(96, 165, 250, 0.08)',
          borderWidth: 2,
          pointRadius: 3,
          pointBackgroundColor: '#60a5fa',
          pointBorderColor: '#1a1a1a',
          pointBorderWidth: 1.5,
          tension: 0.4,
          fill: true,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false }, tooltip: {
          backgroundColor: '#242424',
          titleColor: '#9a9590',
          bodyColor: '#f0ede8',
          borderColor: 'rgba(255,255,255,0.08)',
          borderWidth: 1,
          padding: 8,
          callbacks: {
            label: (ctx) => ` ${ctx.parsed.y}°C`
          }
        }},
        scales: {
          x: { display: false },
          y: {
            display: true,
            grid: { color: 'rgba(255,255,255,0.04)' },
            border: { display: false },
            ticks: {
              color: '#6b6760',
              font: { size: 10 },
              maxTicksLimit: 4,
              callback: (v) => `${v}°`
            }
          }
        }
      }
    })
  } catch (e) {
    console.error('Chart.js not available', e)
  }
})

onUnmounted(() => {
  chartInstance?.destroy()
})
</script>

<style scoped lang="scss">
.sensor-charts {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sensor-card {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sensor-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}

.sensor-value {
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1;
  color: var(--text-primary);
}

.sensor-unit {
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--text-secondary);
  margin-left: 2px;
}

.chart-container {
  height: 110px;
  position: relative;
}

.chart-axis {
  display: flex;
  justify-content: space-between;
  margin-top: 6px;

  .chart-tick {
    font-size: 0.65rem;
    color: var(--text-muted);
    font-family: var(--font-mono);
  }
}

.humidity-bars {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.hum-row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.hum-label {
  width: 52px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  font-weight: 500;
}

.flex-1 { flex: 1; }

.hum-value {
  width: 36px;
  text-align: right;
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--text-primary);
}
</style>
