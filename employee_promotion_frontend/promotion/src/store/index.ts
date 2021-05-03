import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex);

const store = new Vuex.Store({
    modules: {
      
    },
    state: {},
    mutations: {},
    actions: {},
    plugins: [createPersistedState()]
});

export default store;
