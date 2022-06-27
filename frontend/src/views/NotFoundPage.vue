<template>
  <div>
    <AuthNavbar />
    <!-- not found section -->
    
    <div class="notfound">
      <div class="notfound-image-message">
        <div class="notfound-image">
          <img src="../assets/404NotFound.png" alt="" />
        </div>
        <div class="notfound-text">
          <span>There's NOTHING here</span>
          <p>
            ...maybe the page you're looking for is not found or never existed.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import AuthNavbar from '@/components/AuthNavbar';
export default {
  components: {
    AuthNavbar,
  },
};
</script>
<style scoped>
@import './authentication/assets/css/global.css';

.notfound {
  display: flex;
  max-width: 1200px;
  width: 90%;
  margin: 0 auto;
  height: 100vh;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.notfound-text span {
  font-size: 2.5rem;
  color: white;
  font-weight:bold;
}

.notfound-text p{
    color:white;

}
</style>
