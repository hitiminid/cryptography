const getters = {
  isUserLogged : state => {
    return state.isUserLogged;
  },
  getUserToken : state => {
    return state.token;
  }
};

export default getters;
