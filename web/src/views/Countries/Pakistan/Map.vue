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
  },
  methods: {
    getProvience() {
      // eslint-disable-next-line no-undef
      this.provience = provience
      this.getMap()
    },
    getMap() {
      var data = [
        ['pk-sd', this.provience['Sindh'].infected.total - this.provience['Sindh'].recovered.total - this.provience['Sindh'].deceased.total],
        ['pk-ba', this.provience['Balochistan'].infected.total - this.provience['Balochistan'].recovered.total - this.provience['Balochistan'].deceased.total],
        ['pk-jk', this.provience['AJK'].infected.total - this.provience['AJK'].recovered.total - this.provience['AJK'].deceased.total],
        ['pk-na', this.provience['KPK'].infected.total - this.provience['KPK'].recovered.total - this.provience['KPK'].deceased.total],
        ['pk-gb', this.provience['GB'].infected.total - this.provience['GB'].recovered.total - this.provience['GB'].deceased.total],
        ['pk-pb', this.provience['Punjab'].infected.total - this.provience['Punjab'].recovered.total - this.provience['Punjab'].deceased.total],
        ['pk-is', this.provience['Islamabad'].infected.total - this.provience['Islamabad'].recovered.total - this.provience['Islamabad'].deceased.total]
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
