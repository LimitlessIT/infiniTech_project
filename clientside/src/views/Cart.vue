<template>
    <div class="page-cart mb-5">
        <div class="columns is-multiline">
            <div class="comlumn is-12">
                <h1 class="title">Cart</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quatity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <CartItem 
                            v-for="item in cart.items"
                            :key="item.key"
                            :intialItem="item"
                            v-on:removeFromCart="removeFromCart"
                        />
                    </tbody>
                </table>
                <p v-else>You don't have any product in your card...</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Summary</h2>
                <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

                <hr>
                <router-link to="/cart/checkout" class="button is-primary">Proceed to checkout</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    components: {
        CartItem
    },
    mounted() {
        document.title = 'Cart'
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id != item.product.id)
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity * curVal.product.price
            }, 0)
        }
    }
}
</script>