
<template>
    <div class="forgot_password">
        <a href="">Forgot password?</a>
    </div>
</template>

<script lang="ts">
    export default {}
</script>

<style>
    .forgot_password a{
    color: black;
    text-decoration: none;
    font-size: 15px;
    transition: color 0.5s;
    }

    .forgot_password{
        transition: scale 0.5s;  
        align-self: flex-start;
    }

    .forgot_password:hover{
        scale: 1.1;
    }

    .forgot_password:hover a{
        color: rgb(83, 132, 177);
    }

</style>
