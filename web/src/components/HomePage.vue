<script lang="ts">
export default {
    name: "HomePage"
}
</script>

<template>
  <h1>Monitoring tp</h1>
  <router-link :to="{ name: 'list'}">
    <button>List all persons</button>
  </router-link>
  <router-link :to="{ name: 'add'}">
    <button>Add a new person</button>
  </router-link>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
