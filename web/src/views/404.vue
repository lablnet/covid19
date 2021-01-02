<template>
<div style="margin-bottom: 99px;">
    <div class="container mt-6 mb-6 text-center">
        <h1 class="title" style="font-size: 8em">404</h1>
        <h2 class="subtitle mt-2" style="font-size: 1.7em">PAGE NOT FOUND</h2>
        <p class="content mt-2" style="font-size: 1em">The page you are looking for was moved, removed,</p>
        <p class="content mb-5" style="font-size: 1em">renamed or might never existed.</p>

        <span class="mt-6">
            <router-link class="content text-primary mt-6" to="/" style="font-size: 1.2em">Go Home</router-link>
        </span>
    </div>
</div>
</template>

<script lang="js">
export default {
    name: "404",
    mounted() {
        window.scrollTo(0, 0)
    }
}
</script>
