import { RouteRecordRaw } from 'vue-router'
import {get_country} from "@/countryHelper"
import routeConfig from "@/config/routeConfig"

let country = get_country()
let routes: Array<RouteRecordRaw> = routeConfig[country]
routes.push(
    {
      path: '/loading',
      name: 'loading',
      component: () => import(/* webpackChunkName: "about" */ '../views/loading.vue'),
      meta: {
        title: 'Loading...',
      },
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: () => import(/* webpackChunkName: "about" */ '../views/404.vue'),
      meta: {
        title: '404',
      },
    },
  )

export default routes
