<template>
  <div class="auth-body">
    <!-- Logo -->
    <AuthNavbar />
    <!-- start -->

    <div class="auth-box">
      <p class="auth-title">Let's get your account back</p>

      <div class="form">
        <label>New Password</label>
        <input
          type="password"
          class="input"
          placeholder="Enter New Password"
          v-model="userInfo.password"
          name="password"
        />
        <label>Repeat Password</label>
        <input
          type="password"
          class="input"
          placeholder="Repeat Password"
          v-model="userInfo.repeatPassword"
          name="repeatPassword"
        />

        <div
          class="is-flex is-justify-content-space-between button-box is-align-items-center"
        >
          <p></p>
          <button class="button is-primary is-light mt-2" @click.prevent="send">
            Send
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
export default {
  data() {
    return {
      userInfo: {
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
      setNewPassword: 'authentication/setNewPassword',
    }),
    validate() {
      let validate = new ValidationActions(this.userInfo);
      validate.validateEmpty();
      this.validated = validate.getValidation();
      return this.validated;
    },
    send() {
      const data = {
        uid: this.$route.params.id,
        token: this.$route.params.token,
        new_password: this.userInfo.password,
        re_new_password: this.userInfo.repeatPassword,
      };
      if (this.validate()) {
        this.setNewPassword(data);
      }
    },
  },

  mounted() {
    let validate = new ValidationActions(this.userInfo);
    validate.validateInputs();
    validate.validatePassword();
    this.validated = validate.getValidation();
  },
};
</script>
<style scoped>
@import './assets/css/global.css';
.access {
  bottom: -37px;
}

input::placeholder {
  color: rgb(95, 95, 95);
  opacity: 1;
}
</style>
