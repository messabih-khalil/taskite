<template>
  <router-view />
</template>

<script>
// import maps
import authstore from './store/modules/authentication/index';
export default {
  beforeCreate() {
    let refresh = JSON.parse(localStorage.getItem('refreshToken'));
    let access = JSON.parse(localStorage.getItem('token'));
    let user_id = JSON.parse(localStorage.getItem('user_id'));
    if (refresh && access) {
      authstore.state.token = access;
      authstore.state.refreshToken = refresh;
      authstore.state.isAuthenticated = true;
    }
    authstore.state.userId = user_id;
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

html {
  background-color: #1c1c28;
}
.shadow {
  box-shadow: 0 0px 10px -0.5px #aaaaaa1f;
}
/* for global tags */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Poppins', sans-serif;
}

input:focus {
  outline: none;
}

/* overide margin of carousel */
.content ol {
  margin: 0;
}

/* this for content section in views */
.content-section {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: end;
}

.content-section .content {
  padding: 2rem;
  width: 85%;
  /* z-index: 100; */
}

.navbar-div {
  width: 85%;
}


@media only screen and (max-width: 1250px) {
  .content-section {
    width: 100%;
  }

  .content-section .content {
    padding: 2rem;
    width: 100%;
  }

  .navbar-div {
    width: 100%;
  }
}
</style>
