<template>
  <div class="auth-body">
    <!-- Logo -->
    <AuthNavbar />
    <!-- start -->
    <div class="auth-box">
      <p class="auth-title">Let's start with creating account</p>

      <div class="form">
        <label>Username</label>
        <input
          type="text"
          class="input"
          placeholder="Username"
          name="username"
          v-model="userInfo.username"
        />
        <span style="color:red">{{ getNameError }}</span>
        <br>
        <label>Email</label>
        <input
          type="email"
          class="input"
          placeholder="Enter your Email"
          name="email"
          v-model="userInfo.email"
        />
        <span style="color:red">{{ getEmailError }}</span>
        <br>
        <label>Password</label>
        <input
          type="password"
          class="input"
          placeholder="Password"
          name="password"
          v-model="userInfo.password"
        />
        <span>Notice : Please use at least a capital letter and a number</span>
        <br />
        <label>Repeat password</label>
        <input
          type="password"
          class="input"
          placeholder="Repeat password"
          name="repeatPassword"
          v-model="userInfo.repeatPassword"
        />
        <div
          class="is-flex is-justify-content-space-between button-box is-align-items-center"
        >
          <router-link class="i-have" to="/login"
            >Bro I have account</router-link
          >
          <button
            class="button is-primary is-light mt-2"
            @click.prevent="signup"
          >
            Sign up
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AuthNavbar from '@/components/AuthNavbar';
// import validators
import { ValidationActions } from './assets/js/validators';
// import maps
import { mapActions } from 'vuex';
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      userInfo: {
        username: '',
        email: '',
        password: '',
        repeatPassword: '',
      },
      validated: false,
    };
  },
  components: {
    AuthNavbar,
  },

  methods: {
    ...mapActions({
      signupAction: 'authentication/signupAction',
    }),

    validate() {
      let validate = new ValidationActions(this.userInfo);
      validate.validateEmpty();
      this.validated = validate.getValidation();
      return this.validated;
    },

    signup() {
      // check if validate is return true
      if (this.validate()) {
        // send user data to signupAction
        this.signupAction(this.userInfo);
      }
    },
  },

  mounted() {
    let validate = new ValidationActions(this.userInfo);
    validate.validateInputs();
    validate.validatePassword();
    this.validated = validate.getValidation();
  },
  computed: {
    ...mapGetters({
      getNameError: 'authentication/getNameError',
      getEmailError: 'authentication/getEmailError',
    }),
  },
};
</script>

<style scoped>
@import './assets/css/global.css';
input::placeholder {
  color: rgb(95, 95, 95);
  opacity: 1;
}
</style>
