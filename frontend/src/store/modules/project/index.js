import actions from './actions';
import mutations from './mutations';
import getters from './getters';

export default {
  namespaced: true,
  state: {
    projects: null,
    friends: null,
    teamProject : null,
  },
  mutations,
  actions,
  getters,
};
