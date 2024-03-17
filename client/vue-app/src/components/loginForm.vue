<template>
    <div class="logo_main">
        <form action="" method="post" id="login_form" class="auth_form">
            
            <div id="email_field" class="input_field">
                <label for="email_field" class="input_name">Email</label>

                <input 
                    :value="email" 
                    @input="inputEmail"
                    id="email-input" 
                    placeholder=" " 
                    type="email" 
                    required>
            </div>

            <div id="password_field" class="input_field">
                <label for="password_field" class="input_name">Password</label>
                <input 
                :value="password" 
                @input="inputPassword"
                id="password-input" 
                type="password" 
                placeholder=" " 
                required pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$">
            </div>

            <div id="log_in_btn" class="auth_btn">
                    <button type="submit" @click="submitForm"> Log in </button>
            </div>
            <login-forgot-PSWD/>
        </form>
    </div>

</template>

<script lang="ts">
    import LoginForgotPSWD from "./loginForgotPSWD.vue";

    export default {
    
    components: {
        LoginForgotPSWD
    },
    
    
    
    data() {
        return {
        email: '',
        password: '',
        }
    },

    methods: {
        submitForm(){

        },
        
        inputEmail(event){
            this.email= event.target.value
        },
        inputPassword(event){
            this.password = event.target.value
        }
    }
};
        
</script>

<style scoped>

@import url("../static/css/authForm.css");

</style>