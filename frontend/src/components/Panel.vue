<template>
  <div class="panel-side">
    <i class="ri-close-line" @click.prevent="closePanel()"></i>
    <!-- logo div -->
    <div class="logo">
      <img src="../assets/logo/white-logo.png" alt="" />
    </div>
    <!-- avatar -->
    
    <!-- panel of pages -->
    <div class="panel-menu">
      <ul>
        <!-- list of pages -->
        <router-link class="is-flex is-align-items-center li" to="/dashboard">
          <!-- icon -->
          <i class="ri-dashboard-line mr-2"></i>
          <span class="page-title"> Dashboard </span>
        </router-link>
        <router-link class="is-flex is-align-items-center li" to="/projects">
          <!-- icon -->
          <i class="ri-folder-5-line mr-2"></i>
          <span class="page-title"> Projects </span>
        </router-link>
        <router-link class="is-flex is-align-items-center li" to="/tasks">
          <!-- icon -->
          <i class="ri-task-line mr-2"></i>
          <span class="page-title"> Tasks </span>
        </router-link>
        <router-link class="is-flex is-align-items-center li" to="/team">
          <i class="ri-team-line mr-2"></i>
          <span class="page-title"> Team </span>
        </router-link>
        <router-link class="is-flex is-align-items-center li" to="/settings">
          <!-- icon -->
          <i class="ri-settings-5-line mr-2"></i>
          <span class="page-title"> Settings </span>
        </router-link>

        <button class="button is-danger is-light  logout-button" @click.prevent="logout">Logout</button>

      </ul>
    </div>
    <!-- panel image -->
    <div class="panel-image">
      <img src="../assets/people-task.png" alt="">
    </div>
    <div>

    </div>
  </div>
</template>

<script>
// import maps
import { mapActions } from 'vuex';
export default {
  methods: {
    ...mapActions({
      deleteToken : 'authentication/deleteToken'
    }),
    closePanel() {
      const panel = document.querySelector('.panel-side');
      const burger = document.querySelector('.hello-message');
      const closer = document.querySelector('.ri-close-line');
      panel.classList.remove('show');
      closer.classList.remove('show');
      burger.classList.remove('hide');
    },
    logout(){
      this.deleteToken();
    }
  },
};
</script>


<style scoped>
  @import "./assets/css/panelStyle.css";
</style>
