<template>
  <div class="page-content">
    <SanteRisques />
  </div>
</template>

<script setup lang="ts">
import {definePageMeta} from "../../.nuxt/imports";
import SanteRisques from "../components/contexts/SanteRisques.vue";

definePageMeta({ layout: 'default' })
</script>
