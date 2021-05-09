<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-8">
          <h1 class="title mt-3"><b>QUARANTINE FACILITIES</b></h1>
        </div>
        <div class="col-md-4">
          <p class="content mt-3"><b>Last Update:</b> 9 May, 2021</p>
        </div>
      </div>
      <p class="content mt-3 mb-5">
        Details about quarantine facilities designated for COVID-19 treatment
      </p>

      <div class="card mt-3">
        <div class="card-header">
          <h3 class="subtitle">Quarantine Capacity</h3>
        </div>
        <div class="container">
          <div class="row mt-3 mb-3">
            <div class="col-md-6">
               <div class="container">
                <h1 class="title twelve mt-2"><b>TOTAL FACILITIES</b></h1>
                 <h1 class="title eight ml-2 mt-2"><b>{{totalCenters}}</b></h1>
              </div>
            </div>
            <div class="col-md-6">
              <div class="container">
                <h1 class="title twelve mt-2"><b>TOTAL BEDS</b></h1>
                <h1 class="title eight ml-2 mt-2"><b> {{ total }} </b></h1>
              </div>
            </div>
          </div>
          <table class="table table-bordered">
            <thead>
            <tr>
              <th>Region</th>
              <th>Facilities</th>
              <th>Beds</th>
            </tr>
            </thead>
            <tbody class="content">
              <tr>
                <td>Islamabad</td>
                <td>{{ region.Islamabad.total }}</td>
                <td>{{ region.Islamabad.beds }}</td>
              </tr>
              <tr>
                <td>Punjab</td>
                <td>{{ region.Islamabad.total }}</td>
                <td>{{ region.Punjab.beds }}</td>
              </tr>
              <tr>
                <td>Sindh</td>
                <td>{{ region.Sindh.total }}</td>
                <td>{{ region.Sindh.beds }}</td>
              </tr>
              <tr>
                <td>KPK</td>
                <td>{{ region.KPK.total }}</td>
                <td>{{ region.KPK.beds }}</td>
              </tr>
              <tr>
                <td>AJK</td>
                <td>{{ region.AJK.total }}</td>
                <td>{{ region.AJK.beds }}</td>
              </tr>
              <tr>
                <td>Balochistan</td>
                <td>{{ region.Balochistan.total }}</td>
                <td>{{ region.Balochistan.beds }}</td>
              </tr>
              <tr>
                <td>Gilgit Baltistan</td>
                <td>{{ region.GB.total }}</td>
                <td>{{ region.GB.beds }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="card mt-3">
        <div class="card-header">
          <h3 class="subtitle">All Quarantine Centers</h3>
        </div>
        <div class="container">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th>Name</th>
                <th>Beds</th>
                <th>Province</th>
              </tr>
            </thead>
            <tbody class="content">
              <tr v-for="center in centers" :key="center" >
                <td v-if="center.name !== 'GRAND TOTAL'">{{center.name}}</td>
                <td v-if="center.name !== 'GRAND TOTAL'">{{center.beds}}</td>
                <td v-if="center.name !== 'GRAND TOTAL'">{{center.provience}}</td>
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
    this.centers = quarantines
    window.scrollTo(0, 0)
    this.calculate()
  },
  data() {
    return {
      totalCenters: 0,
      total: 0,
      region: {
        "Islamabad": {
          "total": 0,
          "beds": 0,
        },
        "Punjab": {
          "total": 0,
          "beds": 0,
        },
        "AJK": {
          "total": 0,
          "beds": 0,
        },
        "KPK": {
          "total": 0,
          "beds": 0,
        },
        "Sindh": {
          "total": 0,
          "beds": 0,
        },
        "Balochistan": {
          "total": 0,
          "beds": 0,
        },
        "GB": {
          "total": 0,
          "beds": 0,
        },
      },
      centers: [],
    }
  },
  methods: {
    calculate() {
      let punjab = {
        "total": 0,
        "beds": 0,
      }
      let isb = {
        "total": 0,
        "beds": 0,
      }
      let gb = {
        "total": 0,
        "beds": 0,
      }
      let kpk = {
        "total": 0,
        "beds": 0,
      }
      let Balochistan = {
        "total": 0,
        "beds": 0,
      }
      let ajk = {
        "total": 0,
        "beds": 0,
      }
      let sindh = {
        "total": 0,
        "beds": 0,
      }

      for (let index in this.centers) {
        let center = this.centers[index]
        if (center.provience === "Islamabad") {
          isb.total += 1
          isb.beds += parseInt(String(center.beds).replace(",", ""))
        }
        if (center.provience === "Balochistan") {
          Balochistan.total += 1
          Balochistan.beds += parseInt(String(center.beds).replace(",", ""))
        }
        if (center.provience === "KPK") {
          kpk.total += 1
          kpk.beds += parseInt(String(center.beds).replace(",", ""))
        }
        if (center.provience === "Punjab") {
          punjab.total += 1
          punjab.beds += parseInt(String(center.beds).replace(",", ""))
        }
        if (center.provience === "Sindh") {
          sindh.total += 1
          sindh.beds += parseInt(String(center.beds).replace(",", ""))
        }
        if (center.provience === "AJK") {
          ajk.total += 1
          ajk.beds += parseInt(String(center.beds).replace(",", ""))
        }
        if (center.provience === "GB" && center.name !== "GRAND TOTAL") {
          gb.total += 1
          gb.beds += parseInt(String(center.beds).replace(",", ""))
        }
        if (center.name !== "GRAND TOTAL") {
          this.totalCenters++;
          this.total += parseInt(String(center.beds).replace(",", ""))
        }
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
