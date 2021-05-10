<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <h1 class="title mt-3"><b>LAB TESTS</b></h1>
        </div>
        <div class="col-md-4">
          <p class="content mt-3"><b>Last Update:</b> 9 May, 2021</p>
        </div>
      </div>
      <p class="content mt-3 mb-5">
        Details about labs facilities designated for COVID-19 test
      </p>

      <div class="card mt-3">
        <div class="card-header">
          <h3 class="subtitle">Tests Capacity</h3>
        </div>
        <div class="container">
          <div class="row mt-3 mb-3">
            <div class="col-md-6">
              <div class="container">
                <h1 class="title twelve mt-2"><b>TOTAL FACILITIES</b></h1>
                <h1 class="title eight ml-2 mt-2"><b>{{totallabs}}</b></h1>
              </div>
            </div>
          </div>
          <table class="table table-bordered">
            <thead>
            <tr>
              <th>Region</th>
              <th>Facilities</th>
            </tr>
            </thead>
            <tbody class="content">
            <tr>
              <td>Islamabad</td>
              <td>{{ region.Islamabad.total }}</td>
            </tr>
            <tr>
              <td>Punjab</td>
              <td>{{ region.Islamabad.total }}</td>
            </tr>
            <tr>
              <td>Sindh</td>
              <td>{{ region.Sindh.total }}</td>
            </tr>
            <tr>
              <td>KPK</td>
              <td>{{ region.KPK.total }}</td>
            </tr>
            <tr>
              <td>AJK</td>
              <td>{{ region.AJK.total }}</td>
            </tr>
            <tr>
              <td>Balochistan</td>
              <td>{{ region.Balochistan.total }}</td>
            </tr>
            <tr>
              <td>Gilgit Baltistan</td>
              <td>{{ region.GB.total }}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="card mt-3">
        <div class="card-header">
          <h3 class="subtitle">All Testing Labs</h3>
        </div>
        <div class="container">
          <table class="table table-bordered">
            <thead>
            <tr>
              <th><b>Name</b></th>
              <th><b>Province</b></th>
              <th><b>Sector</b></th>
            </tr>
            </thead>
            <tbody class="content">
            <tr v-for="lab in labs" :key="lab" >
              <td>{{lab.name}}</td>
              <td>{{lab.provience}}</td>
              <td>{{lab.sector}}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
export default {
  name: "Quarantine",
  mounted() {
    // eslint-disable-next-line no-undef
    this.labs = labs
    window.scrollTo(0, 0)
    this.calculate()
  },
  data() {
    return {
      totallabs: 0,
      total: 0,
      region: {
        "Islamabad": {
          "total": 0,
        },
        "Punjab": {
          "total": 0,
        },
        "AJK": {
          "total": 0,
        },
        "KPK": {
          "total": 0,
        },
        "Sindh": {
          "total": 0,
        },
        "Balochistan": {
          "total": 0,
        },
        "GB": {
          "total": 0,
        },
      },
      labs: [],
    }
  },
  methods: {
    calculate() {
      let punjab = {
        "total": 0,
      }
      let isb = {
        "total": 0,
      }
      let gb = {
        "total": 0,
      }
      let kpk = {
        "total": 0,
      }
      let Balochistan = {
        "total": 0,
      }
      let ajk = {
        "total": 0,
      }
      let sindh = {
        "total": 0,
        "beds": 0,
      }

      for (let index in this.labs) {
        let lab = this.labs[index]
        if (lab.provience === "Fedral") {
          isb.total += 1
        }
        if (lab.provience === "Baluchistan") {
          Balochistan.total += 1
        }
        if (lab.provience === "KP") {
          kpk.total += 1
        }
        if (lab.provience === "Punjab") {
          punjab.total += 1
        }
        if (lab.provience === "Sindh") {
          sindh.total += 1
        }
        if (lab.provience === "AJK") {
          ajk.total += 1
        }
        if (lab.provience === "GB") {
          gb.total += 1
        }
        this.totallabs++;
      }
      this.region = {
        "Islamabad": isb,
        "Punjab": punjab,
        "AJK": ajk,
        "KPK": kpk,
        "Sindh": sindh,
        "Balochistan": Balochistan,
        "GB": gb,
      }
    }
  },
}
</script>
