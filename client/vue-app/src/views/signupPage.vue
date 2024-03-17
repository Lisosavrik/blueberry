<template>
    <div class="page">
        <div class="animation" id="animation"></div>
        <div class="main_component">
            <div class="top_flex">
                <login-logo/>
                <signup-login/>
            </div>
            <signup-form/>
            <signup-verification/>
        </div>
    </div>
</template>

<script land="ts">
import { startAnimation } from "../static/scripts/matter.js"
import LoginLogo from "../components/loginLogo.vue"
import SignupLogin from "../components/signupLogin.vue"
import SignupForm from "../components/signupForm.vue"
import SignupVerification from "../components/emailVerification.vue"

export default{
    components: {
        LoginLogo,
        SignupLogin,
        SignupForm,
        SignupVerification
    },

    mounted() {
        startAnimation();
    }
}

</script>

<style>
@import url("../static/css/authForm.css");
</style>