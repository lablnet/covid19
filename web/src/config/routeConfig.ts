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
      path: '/map',
      name: 'Map',
      component: () => import('../views/Pakistan/Map.vue'),
      meta: {
        title: 'Map',
      },
    },
  ],
  "tw": []
}

export {routeConfig}
