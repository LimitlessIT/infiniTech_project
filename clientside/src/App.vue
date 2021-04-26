<template>
  <div id="wrapper">

    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item" style="color:#3298dc">
        <strong>Limtless IT</strong>
        </router-link>

        <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="this.showMobileMenu = !this.showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu" v-bind:class="this.showMobileMenu ?  'is-active': ''">
        <div class="navbar-start">
          <router-link to="/pc" class="navbar-item">Pc</router-link>
          <router-link to="/phone" class="navbar-item">Phone</router-link>

          <div class="navbar-item">
            <form method="get" action="/search">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" placeholder="Search products" name="query">
              </div>
              <div class="control">
                <button class="button is-primary">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                </button>
              </div>
            </div>
            </form>
          </div>

          
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/signup" class="button is-primary mr-2" v-if="!this.$store.state.isAthenticated">Signup</router-link>
              <router-link to="/login" class="button is-light mr-2" v-if="!this.$store.state.isAthenticated">Log in</router-link>
              <router-link to="/my-account" class="button is-light mr-2" v-else>My Account</router-link>
              <router-link to="/cart">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
            
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>
  

  <section class="m-5">
    <router-view/>
  </section>

  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2021</p>
  </footer>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      },
      brands: [],
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if(token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for(let i = 0;i<this.cart.items.length;i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  },
  
  
}
</script>


<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring::after {
  content: "";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.is-loading-bar {
  height: 0;
  overflow: hidden;
  --webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}



</style>
