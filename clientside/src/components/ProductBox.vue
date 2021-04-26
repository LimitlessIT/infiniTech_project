<template>
    <div class="column is-3">
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail">
          </figure>

          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6"><strong class="has-text-success">${{ product.price }}</strong></p>

          <router-link v-bind:to="product.get_absolute_url" class="button is-info mt-4">View detail</router-link>
          <img :src="product.mark_name" class="brand">
        </div>
      </div>
</template>

<script>
export default {
    name: 'ProductBox',
    props: {
        product: Object
    }
}
</script>

<style scoped>
.image img {
  height: 200px;
}
.brand {
  width: 60px;
  float: right;
}
h3 {
  height: 72px !important;
  overflow: hidden !important;
}
</style>