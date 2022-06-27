export default {
  // return username from state
  getNameError(state) {
    return state.usernameError;
  },
  // return email from state
  getEmailError(state) {
    return state.emailError;
  },
  // retrun login errors
  loginErrorGetter(state) {
    return state.loginError;
  },
  // return token 
  getToken(state){
    return state.token
  }
};
