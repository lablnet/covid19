<template>
  <div class="container">
    <h1 class="title mt-3">COVID-19 SITUATION IN PAKISTAN</h1>
    <h2 class="subtitle mt-1">COVID-19 SITUATION IN PAKISTAN</h2>
    <p class="content mt-3 mb-5">
      The coronavirus aka COVID-19, is igniting fear worldwide because of number
      of reasons. As COVID-19 is a new virus, there is no available vaccine for
      this. Alongside developing vaccine for COVID-19, researchers are also
      trying to predict its behaviour.
    </p>
    <div class="row">
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Total tests</h1>
            <p class="stat mx-2 mt-2">7,536,134</p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Total Cases</h1>
            <p class="stat mx-2 mt-2">7,536,134</p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Recoveries</h1>
            <p class="stat mx-2 mt-2">7,536,134</p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Deceased</h1>
            <p class="stat mx-2 mt-2">7,536,134</p>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-5">
      <div class="col-md-8">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Case Confirmations</h1>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Cases Provience wise</h1>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-5">
      <div class="col-md-12">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Daily Trend</h1>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-5 mb-3">
      <div class="col-md-4">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Cases Breakdown</h1>
          </div>
        </div>
      </div>
      <div class="col-md-8">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2">Section 2</h1>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang='ts'>
import { Options, Vue } from 'vue-class-component'
import HelloWorld from '@/components/HelloWorld.vue' // @ is an alias to /src

@Options({
  components: {
    HelloWorld
  }
})
export default class Home extends Vue {}
</script>
