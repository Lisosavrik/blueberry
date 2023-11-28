<template>
    <div class="logo_main">
        <form action="" method="post" id="login_form" class="auth_form auth_form_local">
            
            <div id="email_field" class="input_field">
                <label for="email_field" class="input_name">Email</label>

                <input 
                    v-bind:value="email" 
                    @input="inputEmail"
                    id="email-input" 
                    placeholder=" " 
                    type="email" 
                    required
                >
            </div>

            <div id="password_field" class="input_field">
                <label for="password_field" class="input_name">Password</label>
                <input 
                v-bind:value="password" 
                @input="inputPassword"
                id="password-input" 
                type="password" 
                placeholder=" " 
                required pattern="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$">
            </div>

            <div id="log_in_btn" class="auth_btn auth_btn-local">
                    <button type="submit" @click="submitForm"> Log in </button>
            </div>

        </form>
    </div>

</template>

<script lang="ts">
    export default {
    
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

<style>

    .logo_main{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    }

    .auth_form_local{
        gap: 20px;
    }
    .auth_form_local:invalid .auth_btn-local button{
        background-color: lightslategray;
    }

</style>