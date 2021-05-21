var routeConfig: any = {
  "pk": [
    {
      path: '/',
      name: 'Home',
      component: () => import('../views/Pakistan/Home.vue'),
      meta: {
        title: 'Home',
      },
    },
    {
      path: '/quarantine',
      name: 'Quarantine',
      component: () => import('../views/Pakistan/Quarantine.vue'),
      meta: {
        title: 'Quarantine',
      },
    },
    {
      path: '/labs',
      name: 'Labs',
      component: () => import('../views/Pakistan/Labs.vue'),
      meta: {
        title: 'Labs',
      },
    },
    {
      path: '/forecast',
      name: 'Forecast',
      component: () => import('../views/Pakistan/forecast.vue'),
      meta: {
        title: 'Forecast',
      },
    },
    {
      path: '/compare-region',
      name: 'Compare',
      component: () => import('../views/Pakistan/comparison/Region.vue'),
      meta: {
        title: 'Region Comparison',
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
      component: () => import(/* webpackChunkName: "about" */ '../views/Pakistan/Map.vue'),
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
      component: () => import(/* webpackChunkName: "about" */ '../views/Pakistan/Request.vue'),
      meta: {
        title: 'Request',
      },
    },

    // you must copy this route at end.
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: () => import(/* webpackChunkName: "about" */ '../views/404.vue'),
      meta: {
        title: '404',
      },
    },
  ],
  "tw": []
}

export default routeConfig
