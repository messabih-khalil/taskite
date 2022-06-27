<template>
  <div class="auth-body">
    <!-- Logo -->
    <AuthNavbar />
    <!-- start -->
    <div class="auth-box">
      <p class="auth-title">Let's make your account active</p>

      <div class="form" style="text-align: center; color: white">
        <p>
          Plese go to your email to confirm
          <br />
          your account
        </p>

        <div
          class="is-flex is-justify-content-space-between button-box is-align-items-center"
        >
          <p></p>
          <button class="button is-primary is-light mt-3" @click.prevent="resendActivation()">
            Resend confirmation
          </button>
          <p></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AuthNavbar from '@/components/AuthNavbar';
// import maps
import { mapActions } from 'vuex';
export default {
  components: {
    AuthNavbar,
  },
  methods : {
    ...mapActions({
      resendActivation: 'authentication/resendActivation',
    }),

  }
};
</script>

<style scoped>
@import './assets/css/global.css';
.access {
  bottom: -37px;
}
</style>
