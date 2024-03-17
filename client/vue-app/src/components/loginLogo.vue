<template>
    <div class="total_logo">
        <a class='total_a' href="">
            <img src="@/static/img/blueberry_logo.png" alt="Blueberry.com" class="logo_img">
            <div class="bb_flex">
                <span class=" logo_title logo_title1">Blue</span>
                <span class="logo_title logo_title2">berry</span>
            </div>
        </a>
    </div>
</template>

<script lang="ts">
    export default {}
</script>

<style>

.logo_title {
    font-size: 24px;
    font-weight: 700;
    color: rgb(31,52,71);
    position: absolute;
}
.logo_title1 {

    left: 82px;
    top: 16px;
}
.logo_title2 {
    top: 49px;
    left: 52px;
}

.total_a{
    display: flex;
    height: fit-content;
    scale: 0.7;
    text-decoration: none;
    position: relative;
    top: 9px;
}

.bb_flex{
    display: flex;
    flex-direction: column;
}

.logo_img{
    width: 80px;
}

@media screen and (max-width:600px) {
    .total_logo{
        position:fixed;
        top: -20px;
        left: 0;
    }
}

@media  screen and (max-width: 321px) {
    .total_logo{
        scale: 0.8;
        top: -24px;
        left: -13px;
    }
}
</style>