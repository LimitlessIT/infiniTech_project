<template>
    <div class="page-category">
        <div class="column is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ mark.name }}</h2>
            </div>
        </div>
        <ProductBox v-for="product in mark.products" v-bind:key="product.id" v-bind:product="product" />
    </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
    name: 'Mark', 
    data() {
        return {
            mark: {
                products: []
            }
        }
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getMark()
    },
    watch: {
        $route(from, to) {
            if(to.name == 'Mark') {
                this.getMark()
            }
        }
    },
    methods: {
        async getMark() {
            const markSlug = this.$route.params.mark_slug
            console.log(markSlug)
            this.$store.commit('setIsLoading', true)
            await axios
                    .get(`/api/v1/products/mark/${markSlug}`)
                    .then(response => {
                        this.mark = response.data
                        document.title = mark.name
                    })
                    .catch(errors => {
                        console.log(errors)
                    })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>