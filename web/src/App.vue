<template>
  <div>

    <nav class="navbar navbar-expand-lg nav">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">COVID-19</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <svg fill="#000000" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24px" height="24px">
            <path d="M 0 2 L 0 4 L 24 4 L 24 2 Z M 0 11 L 0 13 L 24 13 L 24 11 Z M 0 20 L 0 22 L 24 22 L 24 20 Z"/>
          </svg>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                   <span v-for="item in nav" :key="item">
                     <li class="nav-item" v-if="item['type'] === 'route' && item['hasdropdown'] === false">
                        <router-link class="nav-link" :to="{path: '' + item['slug']}">{{ item['name'] }}</router-link>
                    </li>
                     <li class="nav-item" v-if="item['type'] === 'url' && item['hasdropdown'] === false">
                        <a class="nav-link" :href="item['slug']" target="_blank">{{ item['name'] }}</a>
                    </li>
                     <li class="nav-item dropdown" v-if="item['hasdropdown'] === true">
                       <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                          data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        {{ item['name'] }}
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <span v-for="dropdown in item['dropdown']" :key="dropdown">
                                <div v-if="dropdown['type'] === 'divider'" class="dropdown-divider"></div>
                                <router-link v-if="dropdown['type'] === 'route'" class="dropdown-item"
                                             :to="{path: '' + dropdown['slug']}">{{ dropdown['name'] }}</router-link>
                              <a v-if="dropdown['type'] === 'url'" class="dropdown-item" :href="dropdown['slug']"
                                 target="_blank">{{ dropdown['name'] }}</a>
                            </span>
                        </div>
                    </li>
                   </span>
          </ul>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </div>
      </div>
    </nav>
    <router-view/>

    <footer class="footer text-center justify-content-center">
      <p class="content-about"><b>Disclaimer:</b> Error and Omissions expected</p>
      <p class="content-about" style="font-size: 11px">
        Information displayed here is carefully calibrated and is updated automatically based on reporting of Government
        officials Site(s).
      </p>
      <p class="content-about mt-2">
      <ol>
        <li>
          <router-link class="nav-link" to="/about">About</router-link>
        </li>
        <li>
          <router-link class="nav-link" to="/feedback">Feedback</router-link>
        </li>
        <li>
          <a class="nav-link" href="https://github.com/lablnet/covid19/blob/main/DATA_REQUEST.md" target="_blank">Data Request</a>
        </li>
      </ol>
      </p>
      <p class="content-about mt-2 mb-3">
        Copyright © 2020-2021 - <b>AlphaSoftHub Pvt Ltd & Contributors</b> <a href="https://github.com/lablnet/covid19"
                                                                              target="_blank">Source Code</a>.
      </p>
      <div class="">
        <select
          class="form-control mb-3 country_picker"
          v-model="selectedCode"
          @change="changeCountry"
        >
          <label class="content">Select country:</label>
          <option disabled>Select Country:</option>
          <option
            v-for="country in countries"
            :value="country.code"
            :key="country"
          >
            {{ country.name }}
          </option>
        </select>
      </div>

    </footer>
  </div>
</template>

<script lang="js">
import navbarConfig from "@/config/navbarConfig"
import {get_country} from "@/countryHelper"
import CountryList from "@/config/CountriesList"

export default {
  name: "app",
  watch: {
    $route(to, from) {
      let country = this.getCountryNameByCode(get_country())
      let base = `COVID-19 ${country} Dashboard`
      let title = ""
      if (typeof to.meta.title == "string")
        title = `${to.meta.title} - ${base}`
      else if (typeof to.meta.title == "function")
        title = `${to.meta.title(to)} - ${base}`
      else title = base
      document.title = title
    },
  },
  mounted() {
    this.countries = CountryList
    this.selectedCountry = localStorage.getItem('country')
    this.selectedCode = this.selectedCountry
    this.nav = navbarConfig[get_country()]
    this.scrollTop()
  },
  data() {
    return {
      top: false,
      nav: {},
      countries: [],
      selectedCountry: null,
      selectedCode: null,
    }
  },
  created() {
    window.addEventListener('scroll', this.handleScroll);
  },
  methods: {
    getCountryNameByCode(code) {
      for (let c in CountryList) {
        if (CountryList[c].code === code) return CountryList[c].name
      }
      return ""
    },
    changeCountry() {
      localStorage.setItem("country", this.selectedCode)
      // we need to reload the page, because we load data files in index.html
      location.reload()
    },
    scrollTop() {
      window.scrollTo(0, 0);
    },
    handleScroll(event) {
      if (document.body.scrollTop > 150 || document.documentElement.scrollTop > 150) {
        this.top = true
      } else {
        this.top = false
      }
    },
  }
}
</script>
