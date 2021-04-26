<template>
    <div class="page-checkout mb-5">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in cart.items" :key="item.product.id">
                            <td>{{ item.product.name }}</td>
                            <td>{{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td clospan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>{{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-grey mb-4">* all fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="fields">
                            <label>First Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="firstname">
                            </div>
                        </div>
                        <div class="fields">
                            <label>Last Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="lastname">
                            </div>
                        </div>
                        <div class="fields">
                            <label>Email</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>
                        <div class="fields">
                            <label>Phone</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="fields">
                            <label>Address</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>
                        <div class="fields">
                            <label>Zip code</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>
                        <div class="fields">
                            <label>Place</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>
                    </div>

                    <div class="notification is-danger mt-4" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <hr>

                    <div>
                        
                    </div>

                    <div>
                        <hr>
                        <div id="card-element" class="mb-5" style="width: 400px;"></div>
                        <button class="button is-primary" @click="submitForm">Pay</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            firstname: '',
            lastname: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout'
        this.cart = this.$store.state.cart
        if(this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51IjHaPJmgIN4ypxtNieCMUxAFUxc3dMPuti56vvXn0w9KO8CgZACGlq96gsNBSxpVjmbJbJoktW1g3uw4k6cJMH300rc6WmUti')
            const elements = this.stripe.elements()
            this.card = elements.create('card', {hidePostalCode: true})
            console.log(this.card)
            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []

            if(this.firstname === '') {
                this.errors.push('First name field is missing')
            }
            if(this.lastname === '') {
                this.errors.push('Last name field is missing')
            }
            if(this.email === '') {
                this.errors.push('Email field is missing')
            }
            if(this.phone === '') {
                this.errors.push('Phone field is missing')
            }
            if(this.address === '') {
                this.errors.push('Address field is missing')
            }
            if(this.zipcode === '') {
                this.errors.push('Zip code field is missing')
            }
            if(this.place === '') {
                this.errors.push('Place field is missing')
            }

            if(!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                this.stripe.createToken(this.card).then(result => {
                    if(result.error) {
                        this.$store.commit('setIsLoading', false)
                        this.errors.push('Something went wrong! Please try again')

                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            
            }
        },
        async stripeTokenHandler(token) {
            const items = []

            for(let i=0; i<this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }

                items.push(obj)
            }

            const data = {
                'firstname': this.firstname,
                'lastname': this.lastname,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id,
            }

            await axios
                    .post('/api/v1/checkout/', data)
                    .then(response => {
                        this.$store.commit('clearCart')
                        this.$store.push('/cart/success')
                    })
                    .catch(error => {
                        this.errors.push('Someting went wrong! Please try again')

                        console.log(error)
                    })

                    this.$store.commit('setIsLoading', false)
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