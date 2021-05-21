<template>
  <div class="container mt-4 mb-4">
    <div class="spinner-border text-muted" style="width: 350px; height: 350px"></div>
    Loading...
  </div>
</template>
<script>
export default {
  name: "loding",
  mounted() {
    // eslint-disable-next-line no-undef
    if (typeof loaded !== 'undefined') this.$router.push({ path: '/' })
  }
}
</script>
