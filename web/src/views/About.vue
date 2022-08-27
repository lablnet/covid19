<template>
  <div class="container">
    <h1 class="title mt-3 mx-2">About</h1>
    <div class="card mt-3">
      <div class="card-header">
        <h3 class="subtitle">Overview</h3>
      </div>
      <div class="container">
        <p class="content-about mt-4 mx-2">
          The sole purpose of this dashboard is to make the general public aware of the current situation about COVID-19
          virus outbreak in Pakistan.
        </p>
        <p class="content-about mt-2 mx-2">
          We have tried to sketch a clear picture for you in the simplest and the easiest manner so that you can explain
          everything to others in a convenient way, saving time and eliminating misconceptions about COVID-19.
        </p>
        <p class="content-about mt-2 mx-2">
          If you have any idea/suggestion to improve this dashboard, please write to mumerfarooqlablnet01@gmail.com
        </p>
        <p class="content-about mt-2 mx-2">Yours, </p>
        <p class="content-about mt-2 mx-2 mb-3">Serving Humanity.</p>
      </div>
    </div>
    <div class="card mt-3">
      <div class="card-header">
        <h3 class="subtitle">Data Resources</h3>
      </div>
      <div class="container">
        <p class="content-about mt-2 mx-2" v-html="sources">
        </p>
      </div>
    </div>

    <div class="card mt-3 mb-4">
      <div class="card-header">
        <h3 class="subtitle">Team</h3>
      </div>
      <div class="container">
        <p class="content-about mt-4 mx-2">
          Here is our <b>AlphaSoftHub Pvt Ltd</b> team who initially contribute to this project:
        </p>
        <p class="content-about mt-2 mx-2">
        <ul>
          <li><a href="https://github.com/lablnet" target="_blank">Muhammad Umer Farooq</a> <span class="content-about">(Lead Developer)</span>
          </li>
          <li><a href="https://github.com/AmeerHamza0220" target="_blank">Muhammad Ameer Hamza</a> <span
            class="content-about">(Data Scientist)</span></li>
          <li><a href="https://github.com/Usman-Naeem" target="_blank">Muhammad Usman Naeem</a> <span
            class="content-about">(Python Developer)</span></li>
          <li><a href="https://github.com/Zain-ul-Abdin1417" target="_blank">Zain ul Abdin</a> <span
            class="content-about">(Python Developer)</span></li>
        </ul>
        </p>
        <p class="content-about mt-4 mx-2">Other Contributors and Contribution status:</p>
        <div v-if="!loading">
          <ul class="card contribution-card" v-for="items in contributors" :key="items">
            <a :href="items.link" target="_blank">
              <img :src="items.pic " class="image rounded-circle" style="width: 50px; height: 50px"/>
              <h3 class="title name">{{ items.name ?? "Unknown" }}</h3>
              <p class="content contribution">{{ items.contributions }} Contributions</p>
            </a>
          </ul>
        </div>
        <div v-else>
          <div class="spinner-border mt-4 mb-3 ml-4"></div>
        </div>

        <p class="content mt-2 mb-2">You can contribute data of your country for more info <a
          href="https://github.com/lablnet/covid19/blob/main/CONTRIBUTING.md" target="_blank"> click here </a></p>
      </div>
    </div>
    <div class="card mt-3 mb-4">
      <div class="card-header">
        <h3 class="subtitle"> Support / Donate</h3>
      </div>
      <div class="container">
        <p class="content-about mt-4 mx-2">
          Donated amount will be used for the improvement of dashboard.
        </p>
        <p class="content-about mt-2 mx-2">
          If you like this project; Donate coffee?
          here is the bitcoin address. </p> <br/>
        <pre><code>37x6PA4qtPu2fQnYdW5U7jztYhbchASpBV</code></pre>
        <p class="content-about mt-2 mx-2"> Thank, you so much.
        </p>
      </div>
    </div>
  </div>
</template>
<script lang="js">
var showdown = require('showdown')

export default {
  name: "About",
  mounted() {
    window.scrollTo(0, 0)
    this.getContributors()
    this.getSources()
  },
  data() {
    return {
      sources: "",
      contributors: [],
      loading: true,
    }
  },
  methods: {
    async getSources() {
      const response = await fetch("https://api.github.com/repos/lablnet/covid19/contents/source.md")
      const s = await response.json()
      var converter = new showdown.Converter();
      var md = atob(s.content)
      var html = converter.makeHtml(md);
      this.sources = html

    },
    async getContributors() {
      let that = this
      fetch("https://api.github.com/repos/lablnet/covid19/contributors").then((resp) => resp.json())
        .then(async (data) => {
            let items = []
            for (let index in data) {
              const response = await fetch(`https://api.github.com/users/${data[index].login}`)
              const user = await response.json()
              if (data[index].login !== 'alphasofthub-bot' && data[index].login !== 'dependabot[bot]') {
                items.push(
                  {
                    "name": user.name,
                    "pic": data[index].avatar_url,
                    "link": data[index].html_url,
                    "contributions": data[index].contributions
                  }
                )
              }
            }
            that.contributors = items
            that.loading = false
          }
        ).catch(function (error) {
      })
    }
  }
}
</script>
