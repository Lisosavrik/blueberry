import { createApp } from "vue";
import App from "@/App.vue";
import "../vue-app/src/static/css/main.css";

import { router } from "./router/index";

const app = createApp(App);

app.use(router);

app.mount('#app');