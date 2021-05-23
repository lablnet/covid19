<template>
  <div class="container">
    <h1 class="title mt-3 mx-2">Feedback</h1>
    <div class="card mt-3">
      <div class="container">
        <p class="content mt-2">If you are reporting data issue, please also include supporting creditable source</p>

      </div>
      <contact/>
    </div>
  </div>
</template>

<script lang="js">
import contact from '@/components/contact'

export default {
  name: "About",
  components: {
    contact
  },
  mounted() {
    window.scrollTo(0, 0)
  }
}
</script>
