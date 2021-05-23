import {RouteRecordRaw} from 'vue-router'
import {get_country} from "@/countryHelper"
import routeConfig from "@/config/routeConfig"

// @ts-ignore
let routes: Array<RouteRecordRaw> = routeConfig[get_country()]
routes.push(
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
