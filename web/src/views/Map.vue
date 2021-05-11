<template>
<div class="container mt-2 mb-3">
    <h1 class="title mt-3 mx-2">Map</h1>
    <div class="card mt-3">
        <div class="card-header">
            <h3 class="subtitle">Pakistan</h3>
        </div>
        <div id="map"></div>
    </div>
</div>
</template>

<script lang="js">

export default {
    name: "Map",

    data() {
        return {
            loading: true,
            provience: {},
        }
    },

    mounted() {
        window.scrollTo(0, 0);
        this.getProvience()
        console.log(this.test("AJK"))
    },
    methods: {
        test(state)
        {
          let filtered = []
          // eslint-disable-next-line no-undef
          let data = feed
          for (let item in data) {
            let des = data[item].desc
            let words = des.split(" ")
            for (let word in words) {
              if (words[word] === state) {
                filtered.push(data[item])
              }
            }
          }

          return  filtered
        },
        getProvience() {
          // eslint-disable-next-line no-undef
             this.provience = provience
             this.getMap()
        },
        getMap() {
            var data = [
              ['pk-sd', this.provience['Sindh'].infected.total],
              ['pk-ba', this.provience['Balochistan'].infected.total],
              ['pk-jk', this.provience['AJK'].infected.total],
              ['pk-na', this.provience['KPK'].infected.total],
              ['pk-gb', this.provience['GB'].infected.total],
              ['pk-pb', this.provience['Punjab'].infected.total],
              ['pk-is', this.provience['Islamabad'].infected.total]
            ];

          // eslint-disable-next-line no-undef
            Highcharts.mapChart('map', {
                chart: {
                    map: 'countries/pk/pk-all'
                },

                title: {
                    text: 'Map COVID-19 Pakistan'
                },

                subtitle: {
                    text: 'Source map: <a href="http://code.highcharts.com/mapdata/countries/pk/pk-all.js">Pakistan</a>'
                },

                mapNavigation: {
                    enabled: true,
                    buttonOptions: {
                        verticalAlign: 'bottom'
                    }
                },

                colorAxis: {
                    min: 0
                },

                series: [{
                    data: data,
                    name: 'cases',
                    states: {
                        hover: {
                            color: '#BADA55'
                        }
                    },
                    dataLabels: {
                        enabled: true,
                        format: '{point.name}'
                    }
                }]
            });
        }
    },
}
</script>
