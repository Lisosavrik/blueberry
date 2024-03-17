<template>
    <div class="page">
        <div class="main_component">
            <confirm-img/>
            <confirm-text/>
        </div>
    </div>
</template>

<script lang="ts">
import ConfirmImg from "../components/confirmImg.vue";
import ConfirmText from "../components/confirmText.vue";

export default{
    components:{ 
        ConfirmImg,
        ConfirmText
    }
}
</script>

<style scoped>

.page{
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.main_component{
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    border-radius: 25px;
    width: fit-content;
    padding: 2%;
}

@media screen and (max-width:426px){
        .main_component{
        scale: 0.8;
    }
}

@media screen and (min-width: 320px), (max-height: 600px) {
    
}

</style>