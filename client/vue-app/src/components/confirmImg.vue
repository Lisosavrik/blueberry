<template>
    <div class="img_div">
        <img  src="../static/img/blueberry_fly.png" >
        <img class="raspberry" src="../static/img/blueberry_letter.png">
    </div>
</template>

<script>
export default{}
</script>

<style scoped>
.img_div {
    display: flex;
    flex-direction: row;
    justify-content: center;
    height: 20vh;
    margin-bottom: 25px;
    margin-left: 27px;
}

@media screen and (min-width: 320px) and (max-height: 600px) {
    .img_div{
        scale: 1.2;
    }
}
</style>