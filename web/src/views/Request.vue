<template>
<div class="container mb-5">
    <h1 class="title mt-3 mx-2">Data Request</h1>
    <div class="card mt-3">
        <div class="container">
            <p class="content mt-2">The date we use in our website available publicly, you can download it and use it as you want, but the data is not property of AlphaSoftHub or us.</p>
          <ul>
            <li><a href="https://lablnet.github.io/covid19-parser/data/cases.csv"  target="_blank">Pakistan</a></li>
            <li><a href="https://lablnet.github.io/covid19-parser/data/global.csv" target="_blank">Global</a></li>
          </ul>
          <p class="content mt-2 mb-2">For more info about sources: please <a href="https://github.com/lablnet/covid19-parser/blob/master/source.md" target="_blank">click here</a></p>
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
