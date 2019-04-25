import actions from './actions';
import mutations from './mutations';
import getters from './getters';

const defaultState = {
  isVideoUploadInProgress: false,
  usePreciseAlgorithm: false
};

export default {
  state: defaultState,
  actions,
  mutations,
  getters
};
