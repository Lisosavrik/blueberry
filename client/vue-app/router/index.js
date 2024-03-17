import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
    { path: '/confirm', component: import("../src/views/haveToConfirm.vue")},
    { path: '/login', component: import("../src/views/loginPage")},
    { path: '/signup', component: import("../src/views/signupPage")},
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

export { router };