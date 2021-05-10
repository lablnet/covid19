<template>
<div class="container">
    <h1 class="title mt-3 mx-2">About</h1>
    <div class="card mt-3">
        <div class="card-header">
            <h3 class="subtitle">Overview</h3>
        </div>
        <div class="container">
            <p class="content-about mt-4 mx-2">
                The sole purpose of this dashboard is to make the general public aware of the current situation about COVID-19 virus outbreak in Pakistan.
            </p>
            <p class="content-about mt-2 mx-2">
                We have tried to sketch a clear picture for you in the simplest and the easiest manner so that you can explain everything to others in a convenient way, saving time and eliminating misconceptions about COVID-19.
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
            <p class="content-about mt-4 mx-2">
                Our data fetched automatically, but we trying to make its less error pros. Here are some of resources from where the data is gathered:
            </p>
            <p class="content-about mt-2 mx-2">
                <ul>
                    <li><a href="http://covid.gov.pk/" target="_blank">Official COVID-19 Dashboard</a></li>
                    <li><a href="https://covid19.who.int/" target="_blank">WHO</a></li>
                </ul>
            </p>
          <p class="content-about mt-2 mx-2">Previously, we fetched data from this website:</p>
          <ul>
            <li><a href="https://co.vid19.pk/" target="_blank">https://co.vid19.pk/</a></li>
          </ul>
        </div>
    </div>

    <div class="card mt-3 mb-4">
        <div class="card-header">
            <h3 class="subtitle">Team</h3>
        </div>
        <div class="container">
            <p class="content-about mt-4 mx-2">
                Here is our beloved team members:
            </p>
            <p class="content-about mt-2 mx-2">
                <ul>
                    <li><a href="https://github.com/lablnet" target="_blank">Muhammad Umer Farooq</a> <span class="content-about">(Lead Developer)</span></li>
                    <li><a href="https://github.com/AmeerHamza0220" target="_blank">Muhammad Ameer Hamza</a> <span class="content-about">(Python Developer)</span></li>
                    <li><a href="https://github.com/Usman-Naeem" target="_blank">Muhammad Usman Naeem</a> <span class="content-about">(Python Developer)</span></li>
                    <li><a href="https://github.com/Zain-ul-Abdin1417" target="_blank">Zain ul Abdin</a> <span class="content-about">(Python Developer)</span></li>

                </ul>
            </p>
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
        here is the bitcoin address. </p> <br />
        <img src="https://img.balancebadge.io/btc/37x6PA4qtPu2fQnYdW5U7jztYhbchASpBV.svg" />
      <br />

      <pre><code>37x6PA4qtPu2fQnYdW5U7jztYhbchASpBV</code></pre>
      <p class="content-about mt-2 mx-2"> Thank, you so much.
      </p>
    </div>
  </div>
</div>
</template>
<script lang="js">
export default {
  name: "About",
  mounted() {
    window.scrollTo(0, 0)
  }
}
</script>
