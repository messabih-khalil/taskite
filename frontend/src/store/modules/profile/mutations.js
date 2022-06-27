export default {
  // add data to user profile

  userProfile(state, payload) {
    state.userProfile = payload;
  },

  // commit invitation state

  commitInvitaion(state , payload){
    state.invitations = payload
  }
};
