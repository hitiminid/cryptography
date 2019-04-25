import localStorageService from '../../../services/localStorageService';

const mutations = {
  login(state, payload) {
    const {username, token} = payload;
    state.isUserLogged = true;
    state.token = token;
    localStorageService.set('authorizationToken', token);
  },

  logout(state) {
    state.isUserLogged = false;
    state.token = '';
    localStorageService.remove('authorizationToken');
  }
};

export default mutations;
