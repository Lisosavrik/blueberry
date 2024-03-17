<template>
    <div class="page">
        <div class="main_component">
            <div class="top_flex">
                <login-logo/>
                <login-sign-up/>
            </div>
            <login-form/>
        </div>
    </div>
</template>

<script lang="ts">

    import LoginForm from "../components/loginForm.vue"
    import LoginSignUp from "../components/loginSignUp.vue"
    import LoginLogo from "../components/loginLogo.vue"

export default {
    components: {
        LoginForm,
        LoginSignUp,
        LoginLogo
    }
}

</script>


<style scoped>
@import url("../static/css/authForm.css");

</style>
