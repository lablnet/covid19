import { createRouter, createWebHistory } from 'vue-router'
import routes from "./routes"

// Nprogress
const Nprogress = require('nprogress')
// Nprogress CSS
import 'nprogress/nprogress.css';

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
    Nprogress.start()
    next()
})

router.afterEach((to, from) => {
  // Complete the animation of the route progress bar.
  Nprogress.done()
})

export default router
