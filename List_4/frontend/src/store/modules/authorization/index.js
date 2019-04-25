import actions from './actions';
import mutations from './mutations';
import getters from './getters';

const defaultState = {
  token: '',
  username: '',
  isUserLogged: false
};

export default {
  state: defaultState,
  actions,
  mutations,
  getters
};
