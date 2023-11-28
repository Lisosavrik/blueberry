<template>
    <div class="auth_main">
        <login-head/>
        <login-form/>

    </div>
</template>

<script>
import LoginForm from "./components/login_form.vue"
import LoginHead from "./components/login_head.vue"

import { defineComponent } from "vue"
export default defineComponent({
    components: {
        LoginForm,
        LoginHead
    }
}) 

</script> 

<style>
/* єто нужно будет убрать нахуй! */
.auth_main{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
}</style>