import {RouteRecordRaw} from 'vue-router'
import {get_country} from "@/countryHelper"
import {routeConfig} from "@/config/routeConfig"

let countries = routeConfig['pk']
// eslint-disable-next-line no-prototype-builtins
if (routeConfig.hasOwnProperty(get_country())) {
  // @ts-ignore
  countries = routeConfig[get_country()]
}
let routes: Array<RouteRecordRaw> = countries
routes.push(
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
    meta: {
      title: 'About',
    },
  },
  {
    path: '/feedback',
    name: 'Feedback',
    component: () => import('../views/Feedback.vue'),
    meta: {
      title: 'Feedback',
    },
  },
  {
    path: '/:pathMatch(.*)*',
    name: '404',
    component: () => import('../views/404.vue'),
    meta: {
      title: '404',
    },
  },
)

export default routes
