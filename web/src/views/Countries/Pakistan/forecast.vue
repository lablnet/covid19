<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8">
        <h1 class="title mt-3"><b>FORECAST</b></h1>
      </div>
    </div>
    <p class="content mt-3 mb-5">
      Forecast of cumulative confirmed COVID-19 Cases in Pakistan using Neural Network model.
    </p>
    <div class="row mt-5 mb-5">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h1 class="subtitle">Daily Trend</h1>
          </div>
          <div class="container">
            <div id="myChart" style="width: 100%"></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import {
  Options,
  Vue
} from 'vue-class-component'
import ApexCharts from 'apexcharts'
import round from "@/round"

export default {
  mounted() {
    window.scrollTo(0, 0);
    // eslint-disable-next-line no-undef
    this.trend = trend
    // eslint-disable-next-line no-undef
    this.forecast = forecast
    this.mount()
  },

  data() {
    return {
      trend: [],
      forecast: [],
    }
  },

  methods: {
    mount() {
      const ctx = document.getElementById('myChart')
      const labels = []
      const PREDICTED = []
      const INFECTED = []
      this.trend.map(e => {
        labels.push(e.DATE)
        INFECTED.push(e.INFECTED)
        PREDICTED.push(NaN)
      })
      for (let item in this.forecast) {
        labels.push(this.forecast[item].DATE)
        PREDICTED.push(this.forecast[item].PREDICT)
      }

      const myChart = new ApexCharts(ctx, {
        chart: {type: 'line'},
        series: [
          {
            name: "INFECTED",
            data: INFECTED,
            color: "rgba(255, 153, 0, 1)",
          },
          {
            name: "FORECAST",
            data: PREDICTED,
            color: "rgba(3, 215, 252, 1)",
          },
        ],
        xaxis: {
          categories: labels
        },
        stroke: {
          width: 2
        },
        markers: {
          show: true,
          fillOpacity: 0.5,
          lineWidth: 1,
          size: 5
        },
      })
      myChart.render()
    },
  },
}
</script>
