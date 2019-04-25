import HTTP from "../../../services/httpService";
import store from "../../../store/store";


const PREFIX = 'http://127.0.0.1:8000/api/';


const actions = {

  isVideoUploadInProgress({commit}, isUploadInProgress) {
    console.log('action');
    commit('isVideoUploadInProgress', isUploadInProgress);
  },

  uploadVideo({commit}, file) {

    const {body} = {
      // id
      // file
    };


    const header = {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer ' + store.getters.getUserToken
      }
    };

    console.log(header);

    HTTP.post(PREFIX + 'videos/', file, header)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      })
  },


  uploadImages({commit}, imagesList) {
    console.log("[BODY]", imagesList);
    // HTTP.post(PREFIX + 'images/', body, header)
    //   .then((response) => {
    //     console.log(response)
    //   })
    //   .catch((error) => {
    //     console.log(error)
    //   })
  },

  sendNewPersonData({commit}, data) {

  }
};

export default actions;
