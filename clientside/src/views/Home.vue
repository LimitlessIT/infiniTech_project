<template>
  <div class="home">
    <section class="hero is-medium is-black mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to Limtless IT
        </p>
        <p class="subtitle">
          Your best solution to buy high quality low price phones and pcs
        </p>
      </div>
    </section>

    <div class="columns is-multiline m-5">
      <div class="column is-12">
        <h2 class="is-size-4">Latest products</h2>
      </div>
      <ProductBox v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product" />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'
export default {
  name: 'Home',
  data() {
    return {
      latestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'Home'
  }, 
  methods: {
    getLatestProducts() {
      axios
      .get('/api/v1/latest-product/')
      .then(response => {
        this.latestProducts = response.data
      })
      .catch(errors => {
        console.log(errors)
      })
    }
  }
}
</script>

<style scoped>
</style>
