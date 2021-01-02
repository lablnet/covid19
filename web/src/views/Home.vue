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
                        <div :class="
                  page >= 2 ? 'float-right offset-8' : 'float-right offset-9'
                ">
                            <a style="cursor: pointer" v-if="page >= 2" @click="prevPage">Prev</a>&nbsp; &nbsp; &nbsp; &nbsp;

                            <a style="cursor: pointer" @click="nextPage">
                                Next
                            </a>
                        </div>
                    </div>
                </div>
                <div class="container">
                    <ol class="mt-3">
                        <div class="spinner-border text-info text-center" v-if="loading" role="status">
                            <span class="sr-only">Loading...</span>
                        </div>
                        <li v-for="(item, idx) in data" :key="idx" style="display: block">
                            <p :class="getClass(item.type)" style="display: inline">
                                {{ item.desc }}
                            </p>
                            <p class="content" style="font-size: 11px">
                                {{ item.date }} &nbsp; &nbsp;
                                <a v-if="item.ref" :href="item.ref" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-link-45deg" viewBox="0 0 16 16">
                                        <path d="M4.715 6.542L3.343 7.914a3 3 0 1 0 4.243 4.243l1.828-1.829A3 3 0 0 0 8.586 5.5L8 6.086a1.001 1.001 0 0 0-.154.199 2 2 0 0 1 .861 3.337L6.88 11.45a2 2 0 1 1-2.83-2.83l.793-.792a4.018 4.018 0 0 1-.128-1.287z" />
                                        <path d="M6.586 4.672A3 3 0 0 0 7.414 9.5l.775-.776a2 2 0 0 1-.896-3.346L9.12 3.55a2 2 0 0 1 2.83 2.83l-.793.792c.112.42.155.855.128 1.287l1.372-1.372a3 3 0 0 0-4.243-4.243L6.586 4.672z" /></svg></a>
                            </p>
                        </li>
                        <br />
                    </ol>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="card">
                <div class="card-header">
                    <h1 class="subtitle">Cases Provience wise</h1>
                </div>
                <div class="container">
                    <div class="table-responsive">
                        <table class="table table-strip">
                            <thead class="subtitle">
                                <tr>
                                    <th>
                                        Name
                                    </th>
                                    <th>
                                        Case
                                    </th>
                                </tr>

                            </thead>
                            <tbody class="content">
                                <tr>
                                    <td>Islamabad</td>
                                    <td>{{provience.isb}}</td>
                                </tr>
                                <tr>
                                    <td>Punjab</td>
                                    <td>{{provience.punjab}}</td>
                                </tr>
                                <tr>
                                    <td>Sindh</td>
                                    <td>{{provience.sindh}}</td>
                                </tr>
                                <tr>
                                    <td>Balochistan</td>
                                    <td>{{provience.balochistan}}</td>
                                </tr>
                                <tr>
                                    <td>Gilgit Baltistan</td>
                                    <td>{{provience.gb}}</td>
                                </tr>
                                <tr>
                                    <td>KKP</td>
                                    <td>{{provience.kpk}}</td>
                                </tr>
                                <tr>
                                    <td>AJK</td>
                                    <td>{{provience.ajk}}</td>
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
                    <h1 class="subtitle">Daily Trend</h1>
                </div>
                <div class="spinner-border text-info text-center" v-if="trendLoading" role="status">
                    <span class="sr-only">Loading...</span>
                </div>
                <div class="container">
                    <canvas id="myChart" style="width: 100%"></canvas>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h1 class="subtitle">Cases Breakdown</h1>
                </div>
                <div class="spinner-border text-info text-center" v-if="breakdownLoading" role="status">
                    <span class="sr-only">Loading...</span>
                </div>
                <div class="container">
                    <canvas id="percentage" style="width: 100%"></canvas>
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
import axios from 'axios'
import Chart from 'chart.js'
import url from "@/url.js"

export default {
    mounted() {
        window.scrollTo(0, 0);
        this.getFeed()

        this.getPercentage()
        this.getProvience()
        this.getTrend()
        // this.fillData()
        // this.getAll()
    },

    data() {
        return {
            page: 1,
            loading: true,
            trendLoading: true,
            breakdownLoading: true,
            provienceLoading: true,
            data: [],
            alldate: [],
            datacollection: null,
            dataLabels: [],
            dataset: [],
            percent: {},
            provience: {},
            trend: [],
        }
    },

    methods: {
        percentage() {
            const ctx = document.getElementById('percentage')
            const INFECTED = this.percent.inf
            const DECEASED = this.percent.des
            const RECOVERED = this.percent.rec
            const TOTAL = this.percent.total
            const data = [(INFECTED / TOTAL) * 100, (DECEASED / TOTAL) * 100, (RECOVERED / TOTAL) * 100]

            const myChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    datasets: [{
                        data: data,
                        backgroundColor: [
                            'rgba(255, 153, 0, 1)',
                            'rgba(255, 0, 0, 1)',
                            'rgba(0, 255, 0, 1)'
                        ]
                    }],

                    // These labels appear in the legend and in the tooltips when hovering different arcs
                    labels: [
                        'INFECTED',
                        'DECEASED',
                        'RECOVERED'
                    ]
                },
                options: {
                    elements: {
                        arc: {
                            borderWidth: 0
                        }
                    },
                }
            })
        },

        mount() {
            const ctx = document.getElementById('myChart')

            const labels = []
            const INFECTED = []
            const DECEASED = []
            const RECOVERED = []

            const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            this.trend.map(e => {
                // if (e.type == "INFECTED")  {
                //let num = e.desc.match(/\b\d[\d,.]*\b/g)
                //num = num[0]
                //const d = e.date.split('-')
                //const date = months[d[1] - 1] + '/' + d[2].split('T')[0]

                labels.push(e.DATE)
                INFECTED.push(e.INFECTED)
                DECEASED.push(e.DECEASED)
                RECOVERED.push(e.RECOVERED)
                // }
            })
            const myChart = new Chart(ctx, {
                type: 'line',

                data: {
                    labels: labels,
                    datasets: [{

                            label: '#RECOVERED',
                            data: RECOVERED,
                            borderColor: [
                                'rgba(0, 255, 0, 1)',
                            ],

                            borderWidth: 2,
                            fill: false,

                        },
                        {
                            label: '#INFECTED',
                            data: INFECTED,
                            borderColor: [
                                'rgba(255, 153, 0, 1)',
                            ],

                            borderWidth: 2,
                            fill: false,

                        },
                        {

                            label: '#DECEASED',
                            data: DECEASED,
                            borderColor: [
                                'rgba(255, 0, 0, 1)',
                            ],

                            borderWidth: 2,
                            fill: false,

                        },
                    ]
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

        getProvience() {
            const link = url + '/provience'
            const lbls = []
            axios.get(link).then(response => {
                if (response.status == 200) {
                    this.provience = response.data
                    this.provienceLoading = false
                }
            })
        },
        getPercentage() {
            const link = url + '/percent'
            axios.get(link).then(response => {
                if (response.status == 200) {
                    this.percent = response.data
                    this.breakdownLoading = false
                    this.percentage()
                }
            })
        },
        getAll() {
            const link = url + '/'
            const lbls = []
            axios.get(link).then(response => {
                if (response.status == 200) {
                    this.alldate = response.data
                    this.mount()
                }
            })
        },
        getTrend() {
            const link = url + '/trend'
            axios.get(link).then(response => {
                if (response.status == 200) {
                    this.trend = response.data
                    this.trendLoading = false
                    this.mount()
                }
            })
        },
        getFeed() {
            this.data = []
            this.loading = true
            const link = url + `/feed?page=${this.page}`
            const lbls = []
            axios.get(link).then(response => {
                // if (response.status == 200) {
                this.data = response.data
                this.loading = false
                // }
            })
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
                return 'content alert-success'
            } else if (item.toString() == 'INFECTED') {
                return 'content alert-warning'
            } else if (item.toString() == 'DECEASED') {
                return 'content alert-danger'
            }
        },
        fillData() {
            this.datacollection = {
                labels: [this.getRandomInt(), this.getRandomInt()],
                datasets: [{
                    label: 'Data One',
                    backgroundColor: '#f87979',
                    data: [this.getRandomInt(), this.getRandomInt()]
                }, {
                    label: 'Data One',
                    backgroundColor: '#f87979',
                    data: [this.getRandomInt(), this.getRandomInt()]
                }]
            }
        },
        getRandomInt() {
            return Math.floor(Math.random() * (50 - 5 + 1)) + 5
        }

    },

    computed: {}

}
</script>
