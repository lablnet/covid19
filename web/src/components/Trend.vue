<template>
  <div id="trend" />
</template>

<script lang="ts">
import * as d3 from 'd3'

import { Options, Vue } from "vue-class-component";

@Options({
    name: "trend",
    data() {
   return {
     width: 750,
     height: 400,
     margin: {
       top: 50,
       right: 50,
       left: 50,
       bottom: 50,
     },
   };
 },
 methods: {
      init() {
     //We are accessing the div with the id chart using d3's select method and appending svg
     const svg = d3
       .select("#trend")
       .append("svg")
         .attr("width", this.width)
         .attr("height", this.height)
       .append("g")
       .style(
         "transform",
         `translate(${this.margin.left}px, ${this.margin.top}px)`
       );
    }
 }
})
export default class Trend extends Vue {}
</script>
