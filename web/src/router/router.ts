import { createWebHistory, createRouter } from 'vue-router'


const HomePage = () => import('../components/HomePage.vue')
const ListPersons = () => import('../components/ListPersons.vue')
const AddPerson = () => import('../components/AddPerson.vue')

const routes = [
    { path: '/', component: HomePage, name: 'home' },
    { path: '/list', component: ListPersons, name: 'list' },
    { path: '/add', component: AddPerson, name: 'add' },
    { path: '/healthz', component: HomePage, name: 'readiness'}
  ]
  
export const router = createRouter({
    history: createWebHistory(),
    routes,
  })