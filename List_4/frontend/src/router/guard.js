import store from "../store/store";

const guardRoute = (to, from, next) => {
  // if (to.matched.some(element => element.meta.requiresLogin)) {
  //   if (verifyToken()) {
  //     next();
  //   } else {
  //     next({name: 'Home'});
  //   }
  // } else if (to.matched.some(element => element.meta.onlyForAnonymous)) {
  //   if (verifyToken()) {
  //     next({name: 'Home'});
  //   } else {
  //     next();
  //   }
  // } else {
  //   verifyToken();
  next();
  // }
};

const verifyToken = () => {
  store.dispatch("verifyToken");
  return store.getters.isUserLogged;
  // return true;
};

export default guardRoute;
