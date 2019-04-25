const mutations = {
  isVideoUploadInProgress(state, isUploadInProgress) {
    state.isVideoUploadInProgress = isUploadInProgress;
  },
  changePrecisionAlgorithm(state) {
    state.usePreciseAlgorithm = !state.usePreciseAlgorithm;
  }
};

export default mutations;
