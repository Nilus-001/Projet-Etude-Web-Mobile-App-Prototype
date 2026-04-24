<template>
  <div class="meteo-widget animate-fade-up">
    <!-- Hero météo actuelle -->
    <div class="weather-hero card-elevated">
      <div class="weather-main">
        <div class="weather-temp">
          <span class="temp-value">{{ current.temp }}°</span>
          <div class="weather-meta">
            <p class="weather-desc">{{ current.desc }}</p>
            <p class="weather-detail text-secondary">
              <span>Vent {{ current.wind }}km/h</span>
            </p>
            <p class="weather-detail text-blue">
              Humidité {{ current.humidity }}%
            </p>
          </div>
        </div>
        <div class="weather-icon">
          <span class="weather-emoji">{{ current.emoji }}</span>
        </div>
      </div>
    </div>

    <!-- Prévisions 5 jours -->
    <div class="card delay-1 animate-fade-up">
      <p class="section-label">Prévisions 5 jours</p>
      <div class="forecast-list">
        <div
          v-for="(day, i) in forecast"
          :key="i"
          class="forecast-row"
          :class="{ 'forecast-row--today': i === 0 }"
        >
          <span class="forecast-day">{{ day.label }}</span>
          <span class="forecast-icon">{{ day.emoji }}</span>
          <span class="forecast-temps">{{ day.max }}° / {{ day.min }}°</span>
          <span class="forecast-rain badge" :class="day.rain > 0 ? 'badge--medium' : 'badge--neutral'">
            {{ day.rain }}mm
          </span>
        </div>
      </div>
    </div>

    <!-- Conditions agricoles -->
    <div class="card delay-2 animate-fade-up">
      <p class="section-label">Conditions agricoles</p>
      <div class="agri-grid">
        <div class="agri-card">
          <p class="agri-label">Gel prévu</p>
          <p class="agri-value">{{ agri.frost }}</p>
          <span class="badge" :class="agri.frostBadge">{{ agri.frostStatus }}</span>
        </div>
        <div class="agri-card">
          <p class="agri-label">ETP</p>
          <p class="agri-value">{{ agri.etp }}</p>
          <span class="badge" :class="agri.etpBadge">{{ agri.etpStatus }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const current = {
  temp: 17,
  desc: 'Partiellement nuageux',
  wind: 12,
  humidity: 78,
  emoji: '⛅',
}

const forecast = [
  { label: 'Auj.', emoji: '⛅', max: 17, min: 11, rain: 0 },
  { label: 'Jeu.',  emoji: '🌧️', max: 13, min: 8,  rain: 6 },
  { label: 'Ven.', emoji: '🌧️', max: 11, min: 7,  rain: 14 },
  { label: 'Sam.', emoji: '⛅', max: 16, min: 9,  rain: 1 },
  { label: 'Dim.', emoji: '☀️', max: 19, min: 10, rain: 0 },
]

const agri = {
  frost: 'Non',
  frostStatus: 'Sûr',
  frostBadge: 'badge--low',
  etp: '2.4 mm/j',
  etpStatus: 'Modéré',
  etpBadge: 'badge--medium',
}
</script>

<style scoped lang="scss">
.meteo-widget {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 8em;
  margin-bottom: 6em;
}

.weather-hero {
  background: linear-gradient(135deg, #e8f0fe 0%, #f0e6ff 50%, #e6f7ff 100%);
  border: none;
}

.weather-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.weather-temp {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.temp-value {
  font-size: 3.5rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  color: #1a2a4a;
  line-height: 1;
}

.weather-desc {
  font-size: 1rem;
  font-weight: 600;
  color: #2563eb;
}

.weather-detail {
  font-size: 0.875rem;
  font-weight: 500;
  color: #4f6895;
}

.text-blue { color: #3b82f6; }

.weather-icon {
  .weather-emoji {
    font-size: 4rem;
    line-height: 1;
    filter: drop-shadow(0 4px 12px rgba(0,0,0,0.15));
  }
}

.forecast-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.forecast-row {
  display: flex;
  align-items: center;
  padding: 10px 4px;
  gap: 12px;
  border-radius: 8px;
  transition: background 0.2s;

  &--today {
    background: rgba(255,255,255,0.04);
  }
}

.forecast-day {
  width: 36px;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-secondary);
}

.forecast-icon {
  font-size: 1.1rem;
  width: 24px;
  text-align: center;
}

.forecast-temps {
  flex: 1;
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-primary);
}

.forecast-rain {
  min-width: 48px;
  text-align: center;
  justify-content: center;
}

.agri-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.agri-card {
  background: var(--bg-elevated);
  border-radius: var(--radius-sm);
  padding: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.agri-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}

.agri-value {
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}
</style>
