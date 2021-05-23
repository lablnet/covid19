<template>
  <div id="trend"/>
</template>

<script lang="ts">
import * as d3 from 'd3'

import {Options, Vue} from "vue-class-component";

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
  methods: {}
}
})
export default class Trend extends Vue {
}
</script>
