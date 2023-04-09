// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
      },
    ],
  },
  {
    path: '/users',
    component: () => import ('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Users',
        component: () => import('@/views/Users.vue')
      },
    ],
  },
  {
    path: '/authors',
    component: () => import ('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Authors',
        component: () => import('@/views/Authors.vue')
      },
    ]
  },
  {
    path: '/works',
    component: () => import ('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Works',
        component: () => import('@/views/Obras.vue')
      },
    ]
  },
  {
    path: '/exemplaries',
    component: () => import ('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Exemplaries',
        component: () => import('@/views/Exemplaries.vue')
      },
    ]
  },
  {
    path: '/loans',
    component: () => import ('@/layouts/default/Default.vue'),
    children: [
      {
        path: '',
        name: 'Loans',
        component: () => import('@/views/Loans.vue')
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
