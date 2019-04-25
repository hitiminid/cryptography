import Vue from "vue";
import Router from "vue-router";

import routes from "./routes";
// import guardRoute from './guard';

Vue.use(Router);

const router = new Router({
  routes,
  mode: "history"
});

// router.beforeEach(guardRoute);

export default router;
