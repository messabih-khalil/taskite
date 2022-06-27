import axios from 'axios';

export default {
  // delete errors
  deleteErrors(state) {
    state.usernameError = '';
    state.emailError = '';
  },

  // add error comes from server side
  addErrors(state, payload) {
    state.usernameError = '';
    state.emailError = '';
    if (payload.user_name) {
      state.usernameError = payload.user_name[0];
    }
    if (payload.email) {
      state.emailError = payload.email[0];
    }
  },

  // add Token and refresh token to state
  addToken(state, payload) {
    state.refreshToken = payload.refresh;
    state.token = payload.access;
    state.isAuthenticated = true;
  },
  // add login error
  loginError(state, payload) {
    state.loginError = '';
    state.loginError = payload;
  },
  // add user id
  addUserId(state, payload) {
    state.userId = payload;
  },
  // delete user id
  deleteUserId(state) {
    state.userId = null;
  },

  // remove token and refresh token from the state
  deleteToken(state) {
    state.refreshToken = null;
    state.token = null;
    state.isAuthenticated = false;
    this.deleteUserId;
  },
};
