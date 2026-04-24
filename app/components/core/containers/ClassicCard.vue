<template>
  <div class="card delay-1 animate-fade-up">
    <p class="section-label">{{ title }}</p>
    <slot></slot>
  </div>
</template>


<script setup lang="ts">
const props = defineProps({
  title: { type: String, default: "" },
});
</script>

<style scoped lang="scss">

</style>