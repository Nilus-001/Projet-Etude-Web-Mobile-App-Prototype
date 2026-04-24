<template>
  <div class="page-content">

    <!-- Alerte mildiou -->
    <div class="alert-banner animate-fade-up" v-if="store.unreadAlerts.length">
      <span class="alert-icon">⚠️</span>
      <div>
        <p class="alert-title">{{ store.unreadAlerts[0].title }}</p>
        <p class="alert-msg">{{ store.unreadAlerts[0].message }}</p>
      </div>
    </div>

    <!-- Navigation grid -->
    <div>
      <p class="section-label">Navigation</p>
      <div class="nav-grid">
        <NuxtLink
          v-for="nav in navItems"
          :key="nav.to"
          :to="nav.to"
          class="nav-tile card"
        >
          <div class="nav-tile-icon" :style="{ background: nav.color }">
            <component :is="nav.icon" :size="22" color="#fff" :stroke-width="2" />
          </div>
          <div>
            <p class="nav-tile-name">{{ nav.label }}</p>
            <p class="nav-tile-sub text-muted text-xs">{{ nav.sub }}</p>
          </div>
        </NuxtLink>
      </div>
    </div>

    <!-- Résumé du jour -->
    <div>
      <p class="section-label">Résumé du jour</p>
      <div class="grid-2">
        <div class="card summary-card animate-fade-up delay-1">
          <p class="summary-label">Température</p>
          <p class="summary-value">{{ sensors.airTemp }}<span class="summary-unit">°C</span></p>
          <span class="badge badge--neutral">Normal</span>
        </div>
        <div class="card summary-card animate-fade-up delay-2">
          <p class="summary-label">Humidité sol</p>
          <p class="summary-value">{{ sensors.soilHumidity }}<span class="summary-unit">%</span></p>
          <span class="badge badge--medium">Modéré</span>
        </div>
        <div class="card summary-card animate-fade-up delay-3">
          <p class="summary-label">Hum. air</p>
          <p class="summary-value">{{ sensors.airHumidity }}<span class="summary-unit">%</span></p>
          <span class="badge badge--high">Élevé</span>
        </div>
        <div class="card summary-card animate-fade-up delay-4">
          <p class="summary-label">Santé</p>
          <p class="summary-value">74<span class="summary-unit">/100</span></p>
          <span class="badge badge--low">Bon état</span>
        </div>
      </div>
    </div>

    <!-- Activité récente -->
    <div>
      <p class="section-label">Activité récente</p>
      <div class="activity-list card animate-fade-up delay-2">
        <div v-for="(item, i) in activity" :key="i" class="activity-row">
          <div class="activity-dot" :class="`activity-dot--${item.type}`"></div>
          <div class="activity-content">
            <p class="activity-title">{{ item.title }}</p>
            <p class="activity-time text-muted text-xs">{{ item.time }}</p>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { Cloud, Activity, MapPin, ShieldAlert } from 'lucide-vue-next'
import { useAppStore } from '../store/app'
import { useSensorData } from '../composables/useSensorData'
import {definePageMeta} from "../../.nuxt/imports";


definePageMeta({ layout: 'default' })

const store = useAppStore()
const { sensors } = useSensorData()

const navItems = [
  { to: '/meteo',    label: 'Météo',    sub: 'Prévisions 7j',    icon: Cloud,       color: '#2563eb' },
  { to: '/capteurs', label: 'Capteurs', sub: 'Temp / Humidité',   icon: Activity,    color: '#0d9488' },
  { to: '/sante',    label: 'Santé',    sub: 'Analyse & risques', icon: ShieldAlert, color: '#7c3aed' },
  { to: '/',         label: 'Alertes',  sub: `${store.unreadCount} notifications`, icon: MapPin, color: '#dc2626' },
]

const activity = [
  { title: 'Capteur air mis à jour',        time: 'Il y a 2 min',   type: 'green'  },
  { title: 'Prévision mildiou — Élevé',     time: 'Il y a 18 min',  type: 'orange' },
  { title: 'Analyse sol Parcelle A',        time: 'Il y a 1h',      type: 'blue'   },
  { title: 'Rapport journalier généré',     time: 'Ce matin 07:00', type: 'green'  },
]
</script>

<style scoped lang="scss">
.alert-title {
  font-size: 0.875rem;
  font-weight: 700;
  color: var(--alert-warning-text);
}
.alert-msg {
  font-size: 0.8rem;
  margin-top: 2px;
  opacity: 0.85;
}

.nav-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.nav-tile {
  display: flex;
  flex-direction: column;
  gap: 10px;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
  transition: transform 0.15s ease, background 0.2s;

  &:active {
    transform: scale(0.97);
  }
}

.nav-tile-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.9;
}

.nav-tile-name {
  font-size: 0.95rem;
  font-weight: 700;
}

.summary-card {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.summary-label {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 500;
}

.summary-value {
  font-size: 1.8rem;
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1;
}

.summary-unit {
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--text-secondary);
  margin-left: 2px;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 0;
  padding: 4px 16px;
}

.activity-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid var(--border-subtle);

  &:last-child { border-bottom: none; }
}

.activity-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;

  &--green  { background: var(--accent-green); }
  &--orange { background: var(--accent-orange); }
  &--blue   { background: var(--accent-blue); }
  &--red    { background: var(--accent-red); }
}

.activity-content { flex: 1; }
.activity-title {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-primary);
}
</style>
