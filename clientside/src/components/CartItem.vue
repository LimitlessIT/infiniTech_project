<template>
    <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.name }}</router-link></td>
        <td>${{ item.product.price}}</td>
        <td>
            {{ item.quantity }}
            <a @click="decrementQuantity(item)" style="margin: 2px;"><i class="fas fa-minus-square"></i></a>
            <a @click="incrementQuantity(item)" style="margin: 2px;"><i class="fas fa-plus-square"></i></a>
        </td>
        <td>${{ getItemTotal(item).toFixed(2)}}</td>
        <td><button class="button is-danger del-item" @click="revomeFromCart(item)">x</button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartItem',
    data() {
        return {
            item: this.intialItem
        }
    },
    props: {
        intialItem: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        decrementQuantity(item) {
            item.quantity--
            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }
            this.updateCart()
        },
        incrementQuantity(item) {
            item.quantity++
            this.updateCart()
        },
        revomeFromCart(item){
            this.$emit('removeFromCart', item)
            this.updateCart()
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        }
    }
}
</script>

<style scoped>
.del-item {
    border-radius: 50%;
    width: 16px;
    height: 30px;
}
</style>