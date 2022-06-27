import axios from 'axios';
import router from '../../../router/index';
export default {
  // sign up new users action
  async signupAction(context, data) {
    await axios
      .post('auth/users/', {
        email: data['email'],
        user_name: data['username'],
        password: data['password'],
      })
      .then((response) => {
        localStorage.setItem('email', JSON.stringify(response.data['email']));
        router.push({ path: '/confirm/email' });
      })
      .catch((err) => {
        if (err.response.status == 400) {
          context.commit('addErrors', err.response.data);
        }
      });
  },
  // activate new user account
  async activateAccount(context, data) {
    await axios
      .post('auth/users/activation/', {
        uid: data.uid,
        token: data.token,
      })
      .then((response) => {
        router.push({ path: '/login' });
      })
      .catch((error) => {
        router.push({ path: '/login' });
      });
  },
  // resend activation
  async resendActivation() {
    await axios
      .post('auth/users/resend_activation/', {
        email: JSON.parse(localStorage.getItem('email')),
      })
      .then((response) => {
        alert('resend Activation');
      });
  },

  //   create token
  async createToken(context, data) {
    await axios
      .post('auth/jwt/create/', {
        user_name: data.username,
        password: data.password,
      })
      .then((response) => {
        // commit the store to add token and refresh token
        context.commit('addToken', response.data);
        // add add token and refresh token to local storage
        localStorage.setItem('token', JSON.stringify(response.data['access']));
        localStorage.setItem(
          'refreshToken',
          JSON.stringify(response.data['refresh'])
        );
        // push the user to dashboard page
        router.push({ path: '/dashboard' });
      })
      .catch((error) => {
        if (error.response.status === 401) {
          context.commit('loginError', error.response.data.detail);
        }
      });
  },

  //   delete token
  deleteToken(context) {
    context.commit('deleteToken');
    localStorage.removeItem('token');
    localStorage.removeItem('refreshToken');
    localStorage.removeItem('user_id');
    router.push({ path: '/login' });
  },

  // get user id
  async userID(context) {
    // get user id from ther server side
    axios
      .get('auth/users/me/')
      .then((response) => {
        // commit user id
        context.commit('addUserId', response.data['id']);
        // add user id to local storage
        localStorage.setItem('user_id', JSON.stringify(response.data['id']));
      })
      .catch((error) => {
      });
  },
  //   forget password
  async forgetPassword(context, email) {
    // send forget password message to gmail
    await axios
      .post('auth/users/reset_password/', {
        email,
      })
      .then((response) => {
        alert('Go to your Email to return your account');
      })
      .catch((error) => {
      });
  },
  //   set new password
  async setNewPassword(context, data) {
    // send new password to server side
    await axios
      .post('auth/users/reset_password_confirm/', {
        uid: data.uid,
        token: data.token,
        new_password: data.new_password,
        re_new_password: data.re_new_password,
      })
      .then((response) => {
        alert('Password change');
        router.push({ path: '/login' });
      })
      .catch((error) => {
      });
  },
};
