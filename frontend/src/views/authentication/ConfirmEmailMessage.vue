<template>
  <div class="auth-body">
    <!-- Logo -->
    <AuthNavbar />
    <!-- start -->
    <div class="auth-box">
      <div class="auth-title">
        <i class="ri-user-smile-line"></i>
        <p>Congratulations now you can activate your account</p>
      </div>
      <div class="is-flex is-justify-content-center is-align-items-center">
        <button
          class="button is-success is-light mt-1"
          @click.prevent="activate"
        >
          Activate My Account
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import AuthNavbar from '@/components/AuthNavbar';
// import getters
import { mapActions } from 'vuex';
export default {
  components: {
    AuthNavbar,
  },
  methods: {
    ...mapActions({
      activateAccount: 'authentication/activateAccount',
    }),
    activate() {
      const data = {
        uid: this.$route.params.id,
        token: this.$route.params.token,
      }
      this.activateAccount(data);
    },
  },
};
</script>
<style scoped>
@import './assets/css/global.css';
.ri-user-smile-line {
  color: greenyellow;
  font-size: 3.5rem;
  font-weight: 400;
}
</style>
