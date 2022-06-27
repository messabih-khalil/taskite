import actions from './actions'
import mutations from './mutations'
import getters from './getters'


export default {
    namespaced: true,
    state : {
        userId : null,
        token : null,
        refreshToken : null,
        isAuthenticated : false,
        usernameError : '',
        emailError:'',
        loginError:'',
        userProfile :null,
    },
    mutations,
    actions,
    getters
  }
  