import { createRouter, createWebHistory } from 'vue-router'


import Home from '../views/Home.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Mark from '../views/Mark.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp'
import Login from '../views/Login'
import MyAccount from '../views/MyAccount'
import Checkout from '../views/Checkout'
import Success from '../views/Success'


import store from '../store'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/:category_slug/:product_slug', 
    name: 'Product', 
    component: Product,
  },
  {
    path: '/:category_slug', 
    name: 'Category', 
    component: Category,
  },
  {
    path: '/mark/:mark_slug', 
    name: 'Mark', 
    component: Mark,
  },
  
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requireLogin) && !store.state.isAthenticated) {
    next({ name: 'Login', query: {to: to.path} })
  } else {
    next()
  }
}) 

export default router
