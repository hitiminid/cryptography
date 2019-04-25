import HTTP from '../../../services/httpService';
import localStorageService from '../../../services/localStorageService';

const PREFIX = 'http://localhost:8000/api/';

const actions = {

  async registerUser({commit}, userData) {
    const {username, email, password} = userData;
    try {
      const result = await HTTP.post(PREFIX + 'users/', {
        username,
        email,
        password
      });
      const {displayName, token} = result.data;
      console.log('registered user: ', {displayName, token});
      commit('login', {displayName, token});
    } catch (e) {
      alert('Somenthing went wrong!');
    }
  },

  async performUserLogin({commit}, user) {
    const {username, password} = user;
    console.log(`Creating token for username: ${username}, password: ${password}`);

    try {
      const {data: {token}} = await HTTP.post(PREFIX + 'authorization/obtain', {
        username,
        password
      });
      commit('login', {username, token});
      console.log('Logged in successfully with username', username);
    } catch (e) {
      alert("Unable to login with following credentials!");
    }
  },

  async verifyToken({commit}) {
    const token = localStorageService.get('authorizationToken');
    console.log('performing token verification');
    if (token !== null) {
      const body = {
        token: token
      };
      try {
        const response = await HTTP.post(PREFIX + 'authorization/verify', body);
        const {username, token} = {username: response.data.username, token: response.data.token};
        commit('login', {username, token});
      } catch (e) {
        commit('logout');
      }
    } else {
      commit('logout');
      console.log("No token found");
    }
  },

  refreshToken({commit}) {
    HTTP.post(PREFIX + 'api/authorization/refresh', {})
      .then(function (response) {
      })
      .catch(function (error) {
      })
  },
};

export default actions;
