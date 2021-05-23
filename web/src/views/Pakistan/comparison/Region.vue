<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8">
        <h1 class="title mt-3"><b>FORECAST</b></h1>
      </div>
    </div>
    <p class="content mt-3 mb-5">
      Forecast of cumulative confirmed COVID-19 Cases in Pakistan using linear regression model.
    </p>
    <div class="row mt-5 mb-5">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h1 class="subtitle">Daily Trend</h1>
          </div>
          <div class="container">
            <canvas id="myChart" style="width: 100%"></canvas>
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
import Chart from 'chart.js'
import round from "@/round"
import {get_province_stat} from "@/helper";

export default {
  mounted() {
    window.scrollTo(0, 0);
    this.test()

    // eslint-disable-next-line no-undef
    // this.trend = trend
    // // eslint-disable-next-line no-undef
    // this.forecast = forecast
    // this.mount()
  },

  data() {
    return {
      trend: [],
      forecast: [],

      dataset: [
        {
          label: 'Islamabad',
          data: {},
          borderColor: [
            'rgba(255, 153, 0, 1)',
          ],
          borderWidth: 2,
          fill: false,
        },
      ]
    }
  },

  methods: {
    test() {
      let isb = get_province_stat("Islamabad")
      // let punjab = get_province_stat("Punjab")
      // let sindh = get_province_stat("Sindh")
      // let gb = get_province_stat("GB")
      // let balochistan = get_province_stat("Balochistan")
      // let ajk = get_province_stat("AJK")
      // let kpk = get_province_stat("KPK")


    },
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
        labels.push(this.forecast[item].Date)
        PREDICTED.push(this.forecast[item].PREDICT)
      }
      let isb = get_province_stat("Islamabad")


      const myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: this.datasets
        },
        options: {
          responsive: true,
          maintainAspectRatio: true,
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      })
    },


  },
}
</script>
