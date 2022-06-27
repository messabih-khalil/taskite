<template>
  <div class="auth-body">
    <!-- Logo -->
    <AuthNavbar />
    <!-- start -->
    <div class="auth-box">
      <p class="auth-title">Let's get your account back</p>

      <div class="form">
        <label>email</label>
        <input
          type="email"
          class="input"
          placeholder="Please Enter Your Eamil"
          v-model="userInfo.email"
          name="email"
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
        email: '',
      },
      validated: false,
    };
  },
  components: {
    AuthNavbar,
  },
  methods: {
    ...mapActions({
      forgetPassword : 'authentication/forgetPassword'
    }),
    validate() {
      let validate = new ValidationActions(this.userInfo);
      validate.validateEmpty();
      this.validated = validate.getValidation();

      return this.validated;
    },
    send() {
      if(this.validate()){
        this.forgetPassword(this.userInfo.email)
      }
    },
  },

  mounted() {
    let validate = new ValidationActions(this.userInfo);
    validate.validateInputs();
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
