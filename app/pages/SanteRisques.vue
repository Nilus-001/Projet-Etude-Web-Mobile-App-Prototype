<template>
  <div class="sante-risques">
    <!-- Indice de santé global -->
    <div class="card-elevated animate-fade-up">
      <p class="section-label">Indice de santé global</p>
      <div class="health-score">
        <div class="score-text">
          <span class="score-value">{{ healthScore }}</span>
          <span class="score-max">/ 100 — <span class="score-label">Bon état</span></span>
        </div>
        <div class="score-ring">
          <svg viewBox="0 0 80 80" width="80" height="80">
            <circle
              cx="40" cy="40" r="34"
              fill="none"
              stroke="rgba(255,255,255,0.08)"
              stroke-width="7"
            />
            <circle
              cx="40" cy="40" r="34"
              fill="none"
              stroke="#4ade80"
              stroke-width="7"
              stroke-linecap="round"
              :stroke-dasharray="`${2 * Math.PI * 34}`"
              :stroke-dashoffset="`${2 * Math.PI * 34 * (1 - healthScore / 100)}`"
              transform="rotate(-90 40 40)"
              style="transition: stroke-dashoffset 1s cubic-bezier(.4,0,.2,1)"
            />
            <text x="40" y="44" text-anchor="middle" fill="#4ade80" font-size="14" font-weight="800" font-family="DM Sans">
              {{ healthScore }}%
            </text>
          </svg>
        </div>
      </div>
    </div>

    <!-- Risques maladies -->
    <div class="card delay-1 animate-fade-up">
      <p class="section-label">Risques maladies</p>
      <div class="disease-list">
        <div v-for="disease in diseases" :key="disease.name" class="disease-row">
          <div class="disease-icon">{{ disease.emoji }}</div>
          <div class="disease-info">
            <p class="disease-name">{{ disease.name }}</p>
            <p class="disease-desc text-secondary text-xs">{{ disease.desc }}</p>
          </div>
          <span class="badge" :class="disease.badgeClass">{{ disease.risk }}</span>
        </div>
      </div>
    </div>

    <!-- Sensibilité produits -->
    <div class="card delay-2 animate-fade-up">
      <p class="section-label">Sensibilité produits</p>
      <div class="products-list">
        <div v-for="prod in products" :key="prod.name" class="product-row">
          <span class="product-name">{{ prod.name }}</span>
          <span class="badge" :class="prod.badgeClass">{{ prod.level }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const healthScore = ref(74)

const diseases = [
  {
    name: 'Mildiou',
    desc: 'Conditions favorables demain',
    risk: 'Élevé',
    badgeClass: 'badge--high',
    emoji: '🍄',
  },
  {
    name: 'Pucerons',
    desc: 'Surveillance recommandée',
    risk: 'Moyen',
    badgeClass: 'badge--medium',
    emoji: '🐛',
  },
  {
    name: 'Botrytis',
    desc: 'Risque faible cette semaine',
    risk: 'Faible',
    badgeClass: 'badge--low',
    emoji: '🌿',
  },
]

const products = [
  { name: 'Fongicides cupriques', level: 'Modéré', badgeClass: 'badge--medium' },
  { name: 'Herbicides sélectifs', level: 'Faible', badgeClass: 'badge--low' },
  { name: 'Insecticides contact', level: 'Élevé', badgeClass: 'badge--high' },
]
</script>

<style scoped lang="scss">
.sante-risques {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.health-score {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 8px;
}

.score-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.score-value {
  font-size: 3.5rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  color: var(--accent-green);
  line-height: 1;
}

.score-max {
  font-size: 0.875rem;
  color: var(--text-muted);
}

.score-label {
  color: var(--text-secondary);
  font-weight: 600;
}

.score-ring {
  svg { overflow: visible; }
}

.disease-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.disease-row {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 0;
  border-bottom: 1px solid var(--border-subtle);

  &:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }
}

.disease-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: var(--bg-elevated);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  flex-shrink: 0;
}

.disease-info {
  flex: 1;
  min-width: 0;
}

.disease-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-primary);
}

.disease-desc {
  margin-top: 2px;
}

.products-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.product-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid var(--border-subtle);

  &:last-child {
    border-bottom: none;
    padding-bottom: 0;
  }
}

.product-name {
  font-size: 0.875rem;
  color: var(--text-secondary);
  font-weight: 500;
}
</style>
