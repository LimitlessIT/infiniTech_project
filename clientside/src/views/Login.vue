<template>
    <div class="page-log-in m-6">
        <div>
            <div class="column is-4 is-offset-4">
                <h1 class="title">Login</h1>
            </div>
            <div class="column is-4 is-offset-4">
                <form @submit.prevent="submitForm()">
                    <div class="field">
                        <label >Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>
                    <div class="field">
                        <label >Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>
                    

                    <div class="notification" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-info">Login</button>
                        </div>
                    </div>

                    <hr>
                    Or <router-link to="/signup">click here</router-link> to sign up!
                    
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Login',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Login'
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                    .post('api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = 'Token' + token
                        localStorage.setItem('token', token)
                        this.$store.state.isAthenticated = true
                        const toPath = this.$route.query.to || '/cart'
                        this.$router.push('/cart')
                    })
                    .catch(error => {
                        if(error.response) {
                            for(const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else {
                            this.errors.push('something went wrong. Please try again')
                            console.log(JSON.stringify(error))
                        }
                    })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>