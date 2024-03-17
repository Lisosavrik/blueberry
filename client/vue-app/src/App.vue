<template>
    <div>
        <router-view></router-view>
    </div>
</template>

<script>
import { RouterView, RouterLink } from "vue-router";

import { defineComponent } from "vue"
export default defineComponent({
    components: {
        RouterView,
        RouterLink,
    }
}) 
</script> 

<style scoped>
</style>