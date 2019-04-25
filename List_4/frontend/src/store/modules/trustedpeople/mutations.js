const mutations = {
  addImages(state, payload) {
    const {name, imageList} = payload;
    let person = state.trustedPeopleData.find(person => person.name === name);
    person.imageList = [...person.imageList, ...imageList];
  },

  addImagesToNewPersonPanel(state, payload) {
    const {imageList} = payload;
    let newPersonData = state.newPersonData;
    newPersonData.imageList = [...newPersonData.imageList, ...imageList];
    state.newPersonData[0] = newPersonData;
  },

  createNewPerson(state, payload) {
    state.newPersonData.name = payload;
    // state.trustedPeopleData.push(state.newPersonData);
    // state.newPersonData = {name: '', imageList: []};
  },

  deletePerson(state, personName) {
    state.trustedPeopleData = state.trustedPeopleData.filter(person => person.name !== personName);
  },

  clearNewPersonData(state) {
    state.newPersonData[0] = {name: '', imageList: []};
  },

  deleteNewImage(state, image) {
    let imageList = state.newPersonData[0].imageList;
    state.newPersonData[0].imageList = imageList.filter(img => img !== image);
  }
};

export default mutations;
