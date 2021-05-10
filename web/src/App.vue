<template>
<div>
    <nav class="navbar navbar-expand-lg nav">
        <div class="container-fluid">
            <router-link class="navbar-brand" to="/">COVID-19</router-link>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <svg fill="#000000" xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 24 24" width="24px" height="24px"><path d="M 0 2 L 0 4 L 24 4 L 24 2 Z M 0 11 L 0 13 L 24 13 L 24 11 Z M 0 20 L 0 22 L 24 22 L 24 20 Z"/></svg>
            </button>
            <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link class="nav-link" to="/">Home</router-link>
                    </li>
                  <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      Deep Dive
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                      <router-link class="dropdown-item" to="/quarantine">Quarantine Facilities</router-link>
                    </div>
                  </li>
                    <li class="nav-item">
                        <a class="nav-link" href="https://ncoc.gov.pk/covid-vaccination-en.php" target="_blank">Vaccine</a>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/map">Map</router-link>
                    </li>
                </ul>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </div>
        </div>
    </nav>
    <router-view />

    <footer class="footer text-center justify-content-center">
        <p class="content-about"><b>Disclaimer:</b> Error and Omissions expected</p>
        <p class="content-about text-danger">The testing capacity in Pakistan is very low, the real cases can be much higher.</p>
        <p class="content-about" style="font-size: 11px">
            Information displayed here is carefully calibrated and is updated automatically based on reporting of Government officials Site(s).
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
                    <router-link class="nav-link" to="/request">Data Request</router-link>
                </li>
            </ol>
        </p>
        <p class="content-about mt-2 mb-3">
          Copyright © 2020-2021 - <b>AlphaSoftHub Pvt Ltd</b> <a href="https://github.com/lablnet/covid19-parser" target="_blank">Source Code</a>.
        </p>
    </footer>
</div>
</template>

<script lang="js">
export default {
    name: "app",
    watch: {
        $route(to, from) {
            let title = "COVID-19 Pakistan Dashboard"
            if (typeof to.meta.title == "string")
                title = `${to.meta.title} - COVID-19 Pakistan Dashboard`
            else if (typeof to.meta.title == "function")
                title = `${to.meta.title(to)} - COVID-19 Pakistan Dashboard`
            document.title = title
        },
    },
    mounted() {
        this.scrollTop()
    },
    data() {
        return {
            top: false
        }
    },
    created() {
        window.addEventListener('scroll', this.handleScroll);
    },
    methods: {
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
