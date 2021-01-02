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
          <div class="card-header">
            <div style="display: flex">
              <h3 class="subtitle">Cases Confirmations</h3>
              <div
                :class="
                  page >= 2 ? 'float-right offset-8' : 'float-right offset-9'
                "
              >
                <a style="cursor: pointer" v-if="page >= 2" @click="prevPage"
                  >Prev</a
                >&nbsp; &nbsp; &nbsp; &nbsp;

                <a style="cursor: pointer" @click="nextPage">
                  Next
                </a>
              </div>
            </div>
          </div>
          <div class="container">
            <ol class="mt-3">
              <div
                class="spinner-border text-info text-center"
                v-if="loading"
                role="status"
              >
                <span class="sr-only">Loading...</span>
              </div>
              <li v-for="(item, idx) in data" :key="idx" style="display: block">
                <p :class="getClass(item.type)" style="display: inline">
                  {{ item.desc }}
                </p>
                <p class="content" style="font-size: 11px">
                  {{ item.date }} &nbsp; &nbsp;
                  <a v-if="item.ref" :href="item.ref" target="_blank"
                    ><svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="16"
                      height="16"
                      fill="currentColor"
                      class="bi bi-link-45deg"
                      viewBox="0 0 16 16"
                    >
                      <path
                        d="M4.715 6.542L3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 8.586 5.5L8 6.086a1.001 1.001 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4.018 4.018 0 0 1-.128-1.287z"
                      />
                      <path
                        d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 0 1 2.83 2.83l-.793.792c.112.42.155.855.128 1.287l1.372-1.372a3 3 0 0 0-4.243-4.243L6.586 4.672z"
                      /></svg
                  ></a>
                </p>
              </li>
              <br />
            </ol>
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
            <canvas id="myChart"></canvas>
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

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src
import axios from "axios";
import Chart from 'chart.js';

@Options({
  components: {
    HelloWorld,
  },

  mounted() {
    this.getFeed()
    this.getAll()
    this.fillData()
  
  },

  data() {
    return {
      page: 1,
      loading: true,
      data: [],
      alldate: [],
      datacollection: null,
      dataLabels: [],
      dataset: [],
    };
  },

  methods: {
    mount() {
      var ctx = document.getElementById('myChart');
      let labels = []
      let dataset = []
      console.log("Daata", this.data)
      let months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
      this.alldate.map(e => {
          //if (e.type == "INFECTED")  {
            let num = e.desc.match(/\b\d[\d,.]*\b/g);
            num = num[0]
            let d = e.date.split('-')
            let date = months[d[1] - 1] + "/" + d[2].split("T")[0] 

            console.log(e.desc)
            console.log(num)
            labels.push(date)
            dataset.push(num)
          //}
       
      })
      console.log("laabel", this.data)
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: '# of INFECTED',
            data: dataset,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
    }
    getAll() {
      const url = `http://127.0.0.1:5000/`;
      let lbls = []
      axios.get(url).then(response => {
        console.log(response.status);
        //if (response.status == 200) {
        this.alldate = response.data;
        this.mount()
        //}
      });

    },
    getFeed() {
      this.data = []
      this.loading = true
      const url = `http://127.0.0.1:5000/feed?page=${this.page}`;
      let lbls = []
      axios.get(url).then(response => {
        console.log(response.status);
        //if (response.status == 200) {
        this.data = response.data;
        this.loading = false
        //}
      });

    },


  prevPage() {
    this.page--
    this.getFeed();
  },

  nextPage() {
    this.page++
    this.getFeed();
  },

    getClass (item: string) {
      console.log(item)
      if (item.toString() == "RECOVERED")
        return "content alert-success"
      else if (item.toString() == "INFECTED")
        return "content alert-warning"
      else if (item.toString() == "DECEASED")
        return "content alert-danger"
    },
    fillData () {
        this.datacollection = {
          labels: [this.getRandomInt(), this.getRandomInt()],
          datasets: [
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: [this.getRandomInt(), this.getRandomInt()]
            }, {
              label: 'Data One',
              backgroundColor: '#f87979',
              data: [this.getRandomInt(), this.getRandomInt()]
            }
          ]
        }
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      }

  },

  computed: {
  }
})
export default class Home extends Vue {}
</script>
