<template>
  <div class="auth-body">
    <!-- Logo -->
    <AuthNavbar />
    <!-- start -->

    <div class="auth-box">
      <p class="auth-title">
        Let's make your day <br />
        productive
      </p>

      <div class="form">
        <label>user name</label>
        <input
          type="text"
          class="input"
          placeholder="Your username"
          v-model="userInfo.username"
          name="username"
        />
        <label>Password</label>
        <input
          type="password"
          class="input"
          placeholder="********"
          v-model="userInfo.password"
          name="password"
        />
        <span style="color: red">{{loginError}}</span>
        <div
          class="is-flex is-justify-content-space-between button-box is-align-items-center"
        >
          <router-link class="i-have" to="/forget-password"
            >I forget my password</router-link
          >
          <button
            class="button is-primary is-light mt-2"
            @click.prevent="login"
          >
            Login
          </button>
        </div>

        <router-link class="i-have" to="/signup"
          >Bro I dont have account</router-link
        >
      </div>
    </div>
  </div>
</template>
<script>
import AuthNavbar from '@/components/AuthNavbar';
// import validators
import { ValidationActions } from './assets/js/validators';
// import maps
import { mapActions, mapGetters } from 'vuex';
export default {
  data() {
    return {
      userInfo: {
        username: '',
        password: '',
      },
      validated: false,
    };
  },
  components: {
    AuthNavbar,
  },
  methods: {
    ...mapActions({
      createToken: 'authentication/createToken',
    }),
    validate() {
      let validate = new ValidationActions(this.userInfo);
      validate.validateEmpty();
      this.validated = validate.getValidation();
      return this.validated;
    },
    login() {
      if (this.validate()) {
        this.createToken(this.userInfo);
      }
    },
  },

  mounted() {
    let validate = new ValidationActions(this.userInfo);
    validate.validateInputs();
    this.validated = validate.getValidation();
  },

  computed: {
    ...mapGetters({
      loginError: 'authentication/loginErrorGetter',
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
