<template>
  <div class="default-layout">
    <AppHeader title="test" />
      <slot id="main-slot" />
    <AppNavBottom />
  </div>
</template>

<script setup>
import AppHeader from "~/components/contexts/AppHeader.vue";
import AppNavBottom from "~/components/contexts/AppNavBottom.vue";
</script>

<style lang="scss">
#main-slot {
  margin-top: 100em;
}
</style>
