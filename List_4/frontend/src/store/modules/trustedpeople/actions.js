import HTTP from "../../../services/httpService";
import store from '../../store';


const PREFIX = 'http://127.0.0.1:8000/api/';


const actions = {

  imagesAdded({commit}, eventData) {
    const {name, imageList} = eventData;

    console.log(name);
    console.log(imageList);
    commit('addImages', eventData);
  },

  addImageToNewPersonPanel({commit}, eventData) {
    const {imageList} = eventData;
    console.log(imageList);
    commit('addImagesToNewPersonPanel', eventData);
  },

  createNewPerson({commit}, personName) {
    /*
    * 1) send data to server
    * 2) if server returns 200 add it to list
    */
    commit('createNewPerson', personName);

    const body = prepareNewPersonData();

    HTTP.post(PREFIX + 'images/', body)
      .then((response) => {
        console.log(response);
        // all the stuff with store etc.

      })
      .catch((error) => {
        // console.log(error);
        alert(`Adding person gone wrong.\n${error}`);
        // do nothing and print out error
      });
  },

  deletePerson({commit}, personName) {
    commit('deletePerson', personName);
  },

  deleteNewImage({commit}, image) {
    commit('deleteNewImage', image);
  }
};

function prepareNewPersonData() {
  const newPerson = store.getters.getNewPersonData;
  console.log(newPerson.imageList);
  console.log(newPerson.name);
  return "CONSOLE LOG BODY !!!!!!!!!!!!!!!!!!!";
}

export default actions;
