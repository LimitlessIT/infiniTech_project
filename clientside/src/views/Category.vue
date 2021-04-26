<template>
    <div class="page-category mb-5">
        <div class="columns is-multiline m-5">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>
            <ProductBox v-for="product in category.products" v-bind:key="product.id" v-bind:product="product" />
        </div>
        
    </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
    name: 'Category', 
    data() {
        return {
            category: {
                products: []
            }
        }
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getCategory()
    },
    watch: {
        $route(from, to) {
            if(to.name == 'Category') {
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory() {
            const categorySlug = this.$route.params.category_slug
            this.$store.commit('setIsLoading', true)
            await axios
                    .get(`/api/v1/products/${categorySlug}`)
                    .then(response => {
                        this.category = response.data
                        document.title = category.name
                    })
                    .catch(errors => {
                        console.log(errors)
                    })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>