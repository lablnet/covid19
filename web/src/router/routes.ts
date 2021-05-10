import { RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue'),
    meta: {
      title: 'Home',
    },
  },
  {
    path: '/quarantine',
    name: 'Quarantine',
    component: () => import('../views/Quarantine.vue'),
    meta: {
      title: 'Quarantine',
    },
  },
  {
    path: '/labs',
    name: 'Labs',
    component: () => import('../views/Labs.vue'),
    meta: {
      title: 'Labs',
    },
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
    meta: {
      title: 'About',
    },
  },
  {
    path: '/map',
    name: 'Map',
    component: () => import(/* webpackChunkName: "about" */ '../views/Map.vue'),
    meta: {
      title: 'Map',
    },
  },
  {
    path: '/feedback',
    name: 'Feedback',
    component: () => import(/* webpackChunkName: "about" */ '../views/Feedback.vue'),
    meta: {
      title: 'Feedback',
    },
  },
  {
    path: '/request',
    name: 'request',
    component: () => import(/* webpackChunkName: "about" */ '../views/Request.vue'),
    meta: {
      title: 'Request',
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
]

export default routes
