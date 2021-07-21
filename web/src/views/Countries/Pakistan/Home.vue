<template>
  <div class="container">
    <div class="row">
      <div class="col-md-8">
        <h1 class="title mt-3"><b>COVID-19 SITUATION IN PAKISTAN</b></h1>
      </div>
      <div class="col-md-4">
        <p class="content mt-3"><b>Last Update:</b> {{ update }}</p>
      </div>
    </div>
    <h2 class="subtitle mt-1">COVID-19 SITUATION IN PAKISTAN</h2>
    <p class="content mt-3 mb-5">
      The coronavirus aka COVID-19, is igniting fear worldwide because of number
      of reasons. there are vaccines available for
      COVID-19. Alongside developing vaccine for COVID-19, researchers are also
      trying to predict its behaviour.
    </p>

    <h2 class="subtitle mt-2 mb-2"><b>Vaccine Statistic</b> <span class="badge badge-danger">new</span></h2>
    <div class="row">
      <div class="col-md-4">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2"><b>Partially Vaccinated</b></h1>
            <p class="stat mx-2 mt-2 text-info"><b>{{ vaccine.total_partially }}</b> <sub
              v-if="isToday()">+{{ vaccine.last_partially }}</sub></p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2"><b>Fully Vaccinated</b></h1>
            <p class="stat mx-2 mt-2 text-success"><b>{{ vaccine.total_fully }}</b> <sub
              v-if="isToday()">+{{ vaccine.last_fully }}</sub></p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2"><b>Total Doses Administered</b></h1>
            <p class="stat mx-2 mt-2 text-primary"><b>{{ vaccine.total_doses }}</b> <sub
              v-if="isToday()">+{{ vaccine.last_doses }}</sub></p>
          </div>
        </div>
      </div>
    </div>

    <h2 class="subtitle mt-2 mb-2"><b>COVID-19 Statistic</b></h2>
    <div class="row">
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2"><b>Total tests</b></h1>
            <p class="stat mx-2 mt-2 text-info"><b>{{ summery.total_tests }}</b> <sub
              v-if="isToday()">+{{ summery.last_tests }}</sub></p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2"><b>Total Cases</b></h1>
            <p class="stat mx-2 mt-2 text-warning"><b>{{ summery.total_cases }}</b> <sub
              v-if="isToday()">+{{ summery.last_cases }}</sub></p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2"><b>Recoveries</b></h1>
            <p class="stat mx-2 mt-2 text-success"><b>{{ summery.total_recovered }}</b> <sub
              v-if="isToday()">+{{ summery.last_recovered }}</sub></p>
          </div>
        </div>
      </div>
      <div class="col-md-3">
        <div class="card">
          <div class="container">
            <h1 class="title twelve mt-2"><b>Deceased</b></h1>
            <p class="stat mx-2 mt-2 text-danger"><b>{{ summery.total_deaths }}</b> <sub
              v-if="isToday()">+{{ summery.last_deaths }}</sub></p>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-5">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <div>
              <div style="float: left">
                <h3 class="subtitle feed-title">Cases Confirmations</h3>
              </div>
              <div style="float:right">
                <button class="feedbutton" v-if="page >= 2" @click="prevPage">
                  <svg viewBox="64 64 896 896" width="1em" height="1em" fill="currentColor" aria-hidden="true"
                       focusable="false" class="">
                    <path
                      d="M724 218.3V141c0-6.7-7.7-10.4-12.9-6.3L260.3 486.8a31.86 31.86 0 0 0 0 50.3l450.8 352.1c5.3 4.1 12.9.4 12.9-6.3v-77.3c0-4.9-2.3-9.6-6.1-12.6l-360-281 360-281.1c3.8-3 6.1-7.7 6.1-12.6z"></path>
                  </svg>
                </button>
                <button class="feedbutton" @click="nextPage">
                  <svg viewBox="64 64 896 896" width="1em" height="1em" fill="currentColor" aria-hidden="true"
                       focusable="false" class="">
                    <path
                      d="M765.7 486.8L314.9 134.7A7.97 7.97 0 0 0 302 141v77.3c0 4.9 2.3 9.6 6.1 12.6l360 281.1-360 281.1c-3.9 3-6.1 7.7-6.1 12.6V883c0 6.7 7.7 10.4 12.9 6.3l450.8-352.1a31.96 31.96 0 0 0 0-50.4z"></path>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div class="container">
            <ol class="mt-3 feed-content">
              <li v-for="(item, idx) in feed" :key="idx" style="display: block">
                <p :class="getClass(item.type)" style="display: inline">
                  {{ item.desc }}

                </p>
                <p class="content" style="font-size: 11px">
                  {{ item.date }} &nbsp; &nbsp;
                  <a v-if="item.ref" :href="item.ref" target="_blank">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                         class="bi bi-link-45deg" viewBox="0 0 16 16">
                      <path
                        d="M4.715 6.542L3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 8.586 5.5L8 6.086a1.001 1.001 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4.018 4.018 0 0 1-.128-1.287z"/>
                      <path
                        d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 0 1 2.83 2.83l-.793.792c.112.42.155.855.128 1.287l1.372-1.372a3 3 0 0 0-4.243-4.243L6.586 4.672z"/>
                    </svg>
                  </a>
                </p>
              </li>
              <br/>
            </ol>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <h1 class="subtitle">Cases Province wise</h1>
          </div>
          <div class="container">
            <div class="table-responsive">
              <table class="table table-strip">
                <thead class="subtitle">
                <tr>
                  <th>
                    <span class="text-info">Name</span>
                  </th>
                  <th>
                    <span class="text-warning">Infected</span>
                  </th>
                  <th>
                    <span class="text-success">Recovered</span>
                  </th>
                  <th>
                    <span class="text-danger">Deceased</span>
                  </th>
                </tr>

                </thead>
                <tbody class="content">
                <span style="display: none">{{ i = 0 }}</span>
                <tr v-for="item in provience" :key="item">
                  <td><b>{{ provienceName[i] }}</b></td>
                  <td>{{ item.infected.total }} <sub v-if="isToday()">+{{ item.infected.last }}</sub></td>
                  <td>{{ item.recovered.total }} <sub v-if="isToday()">+{{ item.recovered.last }}</sub></td>
                  <td>{{ item.deceased.total }} <sub v-if="isToday()">+{{ item.deceased.last }}</sub></td>
                  <span style="display: none">{{ i++ }}</span>
                </tr>

                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-5 mb-5">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <h1 class="subtitle">Vaccine Trend</h1>
          </div>
          <div class="container">
            <div id="vaccineChart" style="width: 100%"></div>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <h1 class="subtitle">Cases Breakdown</h1>
          </div>
          <div class="container">
            <div id="percentage" style="width: 100%"></div>
          </div>
        </div>
      </div>
    </div>

    <div class="row mt-5 mb-5">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            <h1 class="subtitle">Daily Trend </h1>
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
import {get_feed_by_province, object_length} from "@/views/Countries/Pakistan/helper";
import ApexCharts from 'apexcharts'
import round from "@/round"
//import {numFormatter} from '@/views/Countries/Pakistan/helper'

export default {
  mounted() {
    // // eslint-disable-next-line no-undef
    // if (typeof loaded === 'undefined') this.$router.push({ name: 'loading' })

    // eslint-disable-next-line no-undef
    this.update = update['update']
    this.getVaccine()
    this.getSummery()
    window.scrollTo(0, 0);
    this.getFeed()
    this.getProvience()
    this.getTrend()
    this.getPercentage()
    this.isToday()
    this.getVacChart()
  },

  data() {
    return {
      vaccine: {},
      update: "",
      provienceName: [
        'Islamabad',
        'Punjab',
        'Sindh',
        "KPK",
        'GB',
        'Balochistan',
        'AJK'
      ],
      summery: {},
      page: 1,
      data: [],
      percent: {},
      provience: {},
      trend: [],
      feed: {},
    }
  },

  methods: {
    getVacChart() {
      // eslint-disable-next-line no-undef
      let vac = vaccine
      let data = {
        total_doses: [],
        total_fully: [],
        total_partially: [],
        vaccinated: []
      }
      let labels = []
      let len = object_length(vac)
      for (let i = len; i >= 0; i--) {
        if (vac[i] !== undefined) {
          data.total_doses.push(Number.parseInt(vac[i].total_doses.toString().replace(/,/g, '')))
          data.total_fully.push(Number.parseInt(vac[i].total_fully.toString().replace(/,/g, '')))
          data.total_partially.push(Number.parseInt(vac[i].total_partially.toString().replace(/,/g, '')))
          data.vaccinated.push(round((Number.parseInt(vac[i].total_fully.toString().replace(/,/g, '')) / 216600000)*100))
          labels.push(vac[i].datetime)
          if ((len - 8) === i) break
        }
      }
      const ctx = document.getElementById("vaccineChart")
      const myChart = new ApexCharts(ctx, {
        chart: {type: 'line'},
        series:
          [{
            name: 'Fully Vaccinated',
            data: data.total_fully.reverse(),
            color: "rgba(0, 255, 0, 1)",
          },
            {
              name: 'Partially Vaccinated',
              data: data.total_partially.reverse(),
              color: "rgba(255, 153, 0, 1)",
            },
            {
              name: 'Doses Administered',
              data: data.total_doses.reverse(),
              color: "rgba(3, 252, 244, 1)",
            },
            {
              name: '%age Vaccinated over population',
              data: data.vaccinated.reverse(),
              color: "rgba(9, 112, 0, 1)",
            },
          ],
        xaxis: {
          categories: labels.reverse()
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
    getVaccine() {
      // eslint-disable-next-line no-undef
      let highest = vaccine[Object.keys(vaccine).pop()];
      this.vaccine = highest
    },
    getSummery() {
      // eslint-disable-next-line no-undef
      let highest = summery[Object.keys(summery).pop()];
      this.summery = highest
    },
    percentage() {
      const ctx = document.getElementById('percentage')
      const INFECTED = this.percent.inf
      const DECEASED = this.percent.des
      const RECOVERED = this.percent.rec
      const TOTAL = this.percent.total
      const data = [INFECTED, DECEASED, RECOVERED]
      //const data = [round((INFECTED / TOTAL) * 100), round((DECEASED / TOTAL) * 100), round((RECOVERED / TOTAL) * 100)]

      const myChart = new ApexCharts(ctx, {
        chart: {type: 'donut'},
        series: data,
        colors: ["rgba(255, 153, 0, 1)", "rgba(255, 0, 0, 1)", "rgba(0, 255, 0, 1)"],
        labels: ['INFECTED', 'DECEASED', 'RECOVERED'],
        yaxis: {
          labels: {
            // formatter: function (value) {
            //   return numFormatter(value)
            // }
          },
        },
        plotOptions: {
          pie: {
            donut: {
              labels: {
                show: true,
                // formatter: function (value) {
                //   return numFormatter(value)
                // }
              }
            }
          }
        }
      })
      myChart.render()
    },

    mount() {
      const ctx = document.getElementById('myChart')

      const labels = []
      const INFECTED = []
      const DECEASED = []
      const RECOVERED = []

      const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
      this.trend.map(e => {
        labels.push(e.DATE)
        INFECTED.push(e.INFECTED)
        DECEASED.push(e.DECEASED)
        RECOVERED.push(e.RECOVERED)
      })
      const myChart = new ApexCharts(ctx, {
        chart: {type: 'line'},
        series:
          [{
            name: 'RECOVERED',
            data: RECOVERED,
            color: "rgba(0, 255, 0, 1)",
          },
            {
              name: 'INFECTED',
              data: INFECTED,
              color: "rgba(255, 153, 0, 1)",
            },
            {

              name: 'DECEASED',
              data: DECEASED,
              color: "rgba(255, 0, 0, 1)",
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

    getProvience() {
      // eslint-disable-next-line no-undef
      this.provience = provience
    },
    getPercentage() {
      let percent = 0;
      let inf = 0
      let dec = 0
      let recv = 0
      let total = 0
      for (let item in this.provience) {
        inf += this.provience[item].infected.total
        dec += this.provience[item].deceased.total
        recv += this.provience[item].recovered.total
      }
      total = inf

      inf = inf - recv - dec
      this.percent = {
        "des": dec,
        "inf": inf,
        "rec": recv,
        "total": total
      }

      this.percentage()
    },
    getTrend() {
      // eslint-disable-next-line no-undef
      this.trend = trend
      this.mount()
    },
    getFeed() {
      this.data = get_feed_by_province("all")
      let records = 7 * this.page
      let start = 0;
      if (this.page !== 1) start = records - 7
      this.feed = []
      let feed = []
      for (let i = start; i <= records; i++) {
        feed.push(this.data[i])
      }
      this.feed = feed
    },

    prevPage() {
      this.page--
      this.getFeed()
    },

    nextPage() {
      this.page++
      this.getFeed()
    },

    getClass(item) {
      if (item.toString() == 'RECOVERED') {
        return 'content text-success'
      } else if (item.toString() == 'INFECTED') {
        return 'content text-warning'
      } else if (item.toString() == 'DECEASED') {
        return 'content text-danger'
      }
    },
    isToday() {
      let date = new Date()
      date = date.getDate()
      let updated = parseInt(String(this.update.split(' ')[0]).split(' ')[0])
      return updated === date
    }
  },
}
</script>
