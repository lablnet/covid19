import {createApp} from 'vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import 'bootstrap'
import {get_country} from "@/countryHelper";
import {routeConfig} from "@/config/routeConfig"

let App = require(`@/App.vue`).default

let _country = get_country()
// eslint-disable-next-line no-prototype-builtins
if (_country != null && routeConfig.hasOwnProperty(_country)) {
  // @ts-ignore
  App = require(`@/views/App/${_country}.vue`).default
}

import './assets/scss/app.scss'

createApp(App).use(store).use(router).mount('#app')
