import { RouteRecordRaw } from 'vue-router'
import {get_country} from "@/countryHelper"
import routeConfig from "@/config/routeConfig"

let country = get_country()
const routes: Array<RouteRecordRaw> = routeConfig[country]

export default routes
