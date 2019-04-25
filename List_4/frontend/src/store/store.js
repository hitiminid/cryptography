import Vuex from 'vuex';
import Vue from 'vue';
import modules from './modules/';

Vue.use(Vuex);


const store = new Vuex.Store({
  modules
});


export default store;
