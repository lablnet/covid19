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
import axios from 'axios'
import url from "@/url.js"


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
            const link =   url + '/provience'
            const lbls = []
            axios.get(link).then(response => {
                // if (response.status == 200) {
                this.provience = response.data
                // }

                this.getMap()
            })
        },
        getMap() {
            // Prepare demo data
            // Data is joined to map using value of 'hc-key' property by default.
            // See API docs for 'joinBy' for more info on linking data and map.
            var data = [
                ['pk-sd', this.provience.sindh],
                ['pk-ba', this.provience.balochistan],
                ['pk-jk', this.provience.ajk],
                ['pk-na', this.provience.kpk],
                ['pk-gb', this.provience.gb],
                ['pk-pb', this.provience.punjab],
                ['pk-is', this.provience.isb]
            ];

            // Create the chart
            Highcharts.mapChart('map', {
                chart: {
                    map: 'countries/pk/pk-all'
                },

                title: {
                    text: 'Map'
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
