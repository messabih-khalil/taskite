<template>
  <div>
    <div class="is-flex">
      <!-- left panel -->
      <div class="pannel">
        <Panel />
      </div>
      <!-- content -->
      <div class="content-section">
        <!-- Navbar -->
        <div class="navbar-div">
          <Navbar />
        </div>
        <!-- content section -->
        <div class="content">
          <!-- settings section -->
          <div class="settings-section">
            <div class="settings">
              <!-- profile image -->
              <div class="profile-images">
                <!-- background image -->
                <div class="back-image">
                  <img src="../../assets/background.png" alt="" />
                </div>
                <div class="image-and-userdata">
                  <div class="image-username is-flex is-align-items-center">
                    <div
                      class="image-box is-flex is-align-items-center is-justify-content-center"
                    >
                      <div class="image-circle">
                        <img
                          :src="userProfileData.photo_url"
                          id="profileImage"
                        />
                      </div>
                      <i class="ri-camera-line" @click.prevent="editImage"></i>
                      <input
                        type="file"
                        src=""
                        alt=""
                        class="is-hidden"
                        id="uploadImage"
                        v-on:change="submitImage"
                        accept="image/*"
                      />
                    </div>

                    <div class="data-box ml-4">
                      <span class="username">{{
                        userProfileData.username
                      }}</span>
                      <p class="mt-2">
                        Update your photo and personal details.
                      </p>
                    </div>
                  </div>
                  <!-- save and cancel button-->
                  <div class="settings-action">
                    <router-link class="button is-info is-outlined mr-3" to="/dashboard">
                      Cancle
                    </router-link>
                    <button class="button is-info" @click="editData">
                      Save
                    </button>
                  </div>
                </div>
              </div>
              <!-- personal info -->
              <div class="personal-info mt-5">
                <!-- header -->

                <!-- first name and last name inputs -->
                <div class="info-box mt-3">
                  <div class="data-title">Nick Name</div>
                  <input
                    type="text"
                    class="input mt-2 mb-2"
                    v-model="userProfileData.nick_name"
                    placeholder="Entre your nick name"
                  />
                </div>

                <!-- external links -->
                <div class="external-links">
                  <div class="info-box mt-3">
                    <div class="data-title">Facebook</div>
                    <input
                      type="text"
                      class="input mt-2 mb-2"
                      v-model="userProfileData.facebook"
                      placeholder="Entre your facebook"
                    />
                  </div>
                  <div class="info-box mt-3">
                    <div class="data-title">Instagram URL:</div>
                    <input
                      type="text"
                      class="input mt-2 mb-2"
                      v-model="userProfileData.instagram"
                      placeholder="Entre your instagram"
                    />
                  </div>
                  <div class="info-box mt-3">
                    <div class="data-title">Twitter URL:</div>
                    <input
                      type="text"
                      class="input mt-2 mb-2"
                      v-model="userProfileData.twitter"
                      placeholder="Entre your twitter"
                    />
                  </div>
                  <div class="info-box mt-3">
                    <div class="data-title">Github URL:</div>
                    <input
                      type="text"
                      class="input mt-2 mb-2"
                      v-model="userProfileData.github"
                      placeholder="Entre your github"
                    />
                  </div>
                </div>

                <!-- change password -->
                <!-- <div class="change-password">
                  <header>
                    <button class="button is-link is-light">
                      Edit Password
                    </button>
                  </header>
                </div> -->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import components
import Panel from '@/components/Panel.vue';
import Navbar from '@/components/Navbar.vue';
// import maps
import { mapActions, mapGetters } from 'vuex';
export default {
  data() {
    return {
      userProfileData: {
        username: '',
        nick_name: '',
        facebook: '',
        instagram: '',
        twitter: '',
        github: '',
      },
    };
  },
  components: {
    Panel,
    Navbar,
  },
  methods: {
    ...mapActions({
      getProfile: 'profile/getProfile',
      editProfile: 'profile/editProfile',
      editProfileImage: 'profile/editProfileImage',
    }),
    // edite user profile data
    editData() {
      this.editProfile({
        nick_name: this.userProfileData.nick_name,
        facebook: this.userProfileData.facebook,
        instagram: this.userProfileData.instagram,
        twitter: this.userProfileData.twitter,
        github: this.userProfileData.github,
      });
    },
    // edite user profile image
    editImage() {
      const uploadImage = document.getElementById('uploadImage');

      uploadImage.click();
    },
    isFileImage(file) {
      return file && file['type'].split('/')[0] === 'image';
    },
    async submitImage() {
      const formData = new FormData();
      const uploadImage = document.getElementById('uploadImage');
      if (this.isFileImage(uploadImage.files[0])) {
        formData.append('image', uploadImage.files[0]);
        let image = await this.editProfileImage(formData);
        document.querySelector('#profileImage').src = image;
      }
    },
  },
  computed: {
    ...mapGetters({
      userProfile: 'profile/userProfile',
    }),
  },
  async created() {
    await this.getProfile();
    this.userProfileData = this.userProfile;
  },
};
</script>

<style scoped>
.profile-images {
  position: relative;
  width: 100%;
}

.profile-images .back-image {
  width: 100%;
  height: 250px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 100px 0 0 0px;
  overflow: hidden;
}

.profile-images .back-image img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.image-and-userdata {
  margin-top: -3rem;
  margin-left: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.image-and-userdata .data-box {
  color: white;
}

.image-and-userdata .data-box .username {
  font-size: 24px;
  font-weight: bold;
}

.image-and-userdata .data-box:nth-child(2) {
  font-size: 20px;
}

.image-box {
  position: relative;
}

.image-circle {
  width: 200px;
  height: 200px;
  overflow: hidden;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.image-circle img {
  object-fit: cover;
  height: 200px;
  width: 200px;
}

.image-box i {
  position: absolute;
  right: 0;
  bottom: 5px;
  font-size: 22px;
  color: white;
  cursor: pointer;
}

/* Personal Info Styling */

.info-box {
  width: 100%;
  display: grid;
  grid-template-columns: 30% 70%;
  align-items: center; /* left and right */
}

.info-box input {
  background: #090d107e;
  border: none;
  color: white;
}

.info-box .data-title {
  border: none;
  color: white;
  font-size: 18px;
  font-weight: 500;
}

/* security section styling */

.change-password header button {
  width: 200px;
  margin-top: 1rem;
  margin-bottom: 3rem;
}

input::placeholder {
  color: rgb(95, 95, 95);
  opacity: 1;
}

@media only screen and (max-width: 880px) {
  .image-and-userdata {
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
    margin-left: 0;
  }

  .image-username {
    justify-content: flex-start;
  }

  .settings-action {
    display: flex;
    justify-content: end;
    width: 100%;
  }
}

@media only screen and (max-width: 600px) {
  .settings-action {
    margin-top: 1.5rem;
  }

  .image-and-userdata {
    margin-left: 0;
  }
  .image-and-userdata .image-username {
    /* flex-direction: column; */
    width: 100%;
    margin-left: 0;
  }
}

@media only screen and (max-width: 450px) {
  .info-box {
    grid-template-columns: 1fr;
  }

  .info-box input {
    margin-top: 2rem;
  }

  .image-and-userdata .data-box p {
    display: none;
  }

  .profile-images .back-image {
    height: 150px;
    border-radius: 20px 0 0 0;
  }

  .image-circle {
    width: 150px;
    height: 150px;
  }
  .image-circle img {
    width: 150px;
    height: 150px;
  }

  .image-username {
    flex-direction: column;
  }
}

@media only screen and (max-width: 390px) {
  .image-and-userdata .image-username {
    flex-direction: column;
  }
}
</style>
