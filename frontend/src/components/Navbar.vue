<template>
  <div>
    <div
      class="navbar is-flex is-align-items-center is-justify-content-space-between"
    >
      <div class="logo-and-burger">
        <div class="hello-message is-flex is-align-items-center">
          <i class="ri-menu-line mr-4" @click.prevent="showPannel()"></i>
          <div class="logo">
            <img src="../assets/logo/white-logo.png" alt="" />
          </div>
        </div>
      </div>

      <!-- search box -->
      <div class="search-box">
        <div class="search shadow">
          <input
            type="text"
            name=""
            id="search_input"
            placeholder="Search ..."
          />
          <i class="ri-search-2-line"></i>
        </div>
        <i
          class="ri-close-fill close-search"
          @click.prevent="closeSearchBox"
        ></i>
        <!-- search result -->
        <div class="search-resault shadow">
          <div
            class="profile-result mb-4 mt-2"
            v-for="profile in profiles.profiles"
            :key="profile.pk"
          >
            <div class="profile-image">
              <img :src="profile.photo_url" alt="" />
            </div>

            <div class="profile-info">
              <div class="username">
                <span>{{ profile.username }}</span>
              </div>

              <div class="contact">
                <a
                  class="ri-github-fill ml-2"
                  style="color: var(--font-color)"
                  :href="profile.github"
                  v-if="profile.github"
                ></a>
                <a
                  class="ri-facebook-circle-fill ml-2"
                  style="color: #1771e6"
                  :href="profile.facebook"
                  v-if="profile.facebook"
                ></a>
                <a
                  class="ri-instagram-fill ml-2"
                  style="color: #ca2b58"
                  :href="profile.instagram"
                  v-if="profile.instagram"
                ></a>
                <a
                  class="ri-twitter-fill ml-2"
                  style="color: #05a3e4"
                  :href="profile.twitter"
                  v-if="profile.twitter"
                ></a>
                <i
                  :class="
                    'ri-indeterminate-circle-line ml-2 not-user-' +
                    profile.username
                  "
                  style="color: red; display: none"
                  @click.prevent="
                    deletefriend(
                      profile.username,
                      `is-user-${profile.username}`,
                      `not-user-${profile.username}`
                    )
                  "
                ></i>
                <i
                  :class="'ri-add-circle-line ml-2 is-user-' + profile.username"
                  style="color: #91d760"
                  @click.prevent="
                    sendInvitation(
                      profile.username,
                      `not-user-${profile.username}`,
                      `is-user-${profile.username}`
                    )
                  "
                ></i>
              </div>
            </div>
          </div>
          <!-- friends in search -->
          <div
            class="profile-result mb-4 mt-2"
            v-for="profile in profiles.friends"
            :key="profile.pk"
          >
            <div class="profile-image">
              <img :src="profile.photo_url" alt="" />
            </div>

            <div class="profile-info">
              <div class="username">
                <span>{{ profile.username }}</span>
              </div>

              <div class="contact">
                <a
                  class="ri-github-fill ml-2"
                  style="color: var(--font-color)"
                  :href="profile.github"
                  v-if="profile.github"
                ></a>
                <a
                  class="ri-facebook-circle-fill ml-2"
                  style="color: #1771e6"
                  :href="profile.facebook"
                  v-if="profile.facebook"
                ></a>
                <a
                  class="ri-instagram-fill ml-2"
                  style="color: #ca2b58"
                  :href="profile.instagram"
                  v-if="profile.instagram"
                ></a>
                <a
                  class="ri-twitter-fill ml-2"
                  style="color: #05a3e4"
                  :href="profile.twitter"
                  v-if="profile.twitter"
                ></a>
                <i
                  :class="
                    'ri-indeterminate-circle-line ml-2 not-friend-' +
                    profile.username
                  "
                  style="color: red"
                  @click.prevent="
                    deletefriend(
                      profile.username,
                      `is-friend-${profile.username}`,
                      `not-friend-${profile.username}`
                    )
                  "
                ></i>
                <i
                  :class="
                    'ri-add-circle-line ml-2 is-friend-' + profile.username
                  "
                  style="color: #91d760; display: none"
                  @click.prevent="
                    sendInvitation(
                      profile.username,
                      `not-friend-${profile.username}`,
                      `is-friend-${profile.username}`
                    )
                  "
                ></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- navbar action -->
      <div class="actions is-flex is-align-items-center">
        <!-- notifications -->
        <div class="dropdown is-right" id="notifaction_dropdown">
          <div class="dropdown-trigger">
            <i
              class="ri-notification-3-line action-icon"
              @click.prevent="toggle('notifaction_dropdown')"
            ></i>
          </div>
          <div class="dropdown-menu" id="dropdown-menu6" role="menu">
            <div class="dropdown-content notification-box shadow">
              <div class="notification-header">
                <span>Inivitations</span>
              </div>
              <!-- notification body -->
              <div
                class="notification-body"
                v-for="profile in invitations"
                :key="profile.pk"
              >
                <!-- message notf -->
                <div
                  :class="
                    'profile-result mb-4 mt-2 invitation-' + profile.username
                  "
                >
                  <div class="profile-image">
                    <img :src="profile.photo_url" alt="" />
                  </div>

                  <div class="profile-info">
                    <div class="username">
                      <span>{{ profile.username }}</span>
                    </div>

                    <!-- actions -->
                    <div>
                      <!-- refuse -->
                      <i
                        class="ri-close-circle-line mr-2"
                        style="color: red; font-size: 1.8rem; cursor: pointer"
                        @click.prevent="refuseInvitation(profile.username)"
                      ></i>
                      <!-- accept -->
                      <i
                        class="ri-checkbox-circle-line"
                        style="
                          color: rgb(145, 215, 96);
                          font-size: 1.8rem;
                          cursor: pointer;
                        "
                        @click.prevent="acceptInvitation(profile.username)"
                      ></i>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <router-link to="/settings" class="ml-4">
          <i class="ri-settings-5-line setting-icon"></i>
        </router-link>
        <i class="ri-login-circle-line ml-4" @click="logout"></i>
      </div>
    </div>
    <!-- footer navbar -->
    <div class="footer-navbar shadow">
      <router-link to="/dashboard">
        <i class="ri-dashboard-line mr-2"></i>
      </router-link>

      <router-link to="/tasks">
        <i class="ri-task-line mr-2"></i>
      </router-link>
      <div class="add" @click.prevent="searchBox">
        <i class="ri-search-2-line"></i>
      </div>
      <router-link to="/projects">
        <i class="ri-folder-5-line mr-2"></i>
      </router-link>

      <router-link to="/goals">
        <i class="ri-focus-2-line mr-2"></i>
      </router-link>
    </div>
  </div>
</template>

<script>
// import maps
import { mapActions, mapGetters } from 'vuex';
export default {
  data() {
    return {
      profiles: [],
      invitations: [],
    };
  },
  methods: {
    // import maps
    ...mapActions({
      searchAction: 'profile/searchAction',
      deleteToken: 'authentication/deleteToken',
      getInvitationsAction: 'profile/getInvitationsAction',
      sendInvitationAction: 'profile/sendInvitation',
      acceptInvitationAction: 'profile/acceptInvitationAction',
      refuseInvitaionAction: 'profile/refuseInvitaionAction',
      deleteFriendAction: 'profile/deleteFriendAction',
    }),
    // show and hide drop downs
    toggle(id) {
      let dropdown = document.getElementById(`${id}`);
      let dropdowns = document.querySelectorAll('.dropdown');

      if (dropdown.classList.contains('is-active') == false) {
        dropdowns.forEach((e) => {
          e.classList.remove('is-active');
        });
        dropdown.classList.add('is-active');
      } else {
        dropdowns.forEach((e) => {
          e.classList.remove('is-active');
        });
      }
    },
    // show and close left panel
    showPannel() {
      const panel = document.querySelector('.panel-side');
      const burger = document.querySelector('.hello-message');
      const closer = document.querySelector('.ri-close-line');
      panel.classList.add('show');
      closer.classList.add('show');
      burger.classList.add('hide');
    },
    // close search box
    closeSearchBox() {
      document.querySelector('.search-box').classList.remove('show-search');
      document.querySelector('.search-resault').style.display = 'none';
    },
    // open search box
    searchBox() {
      document.querySelector('.search-box').classList.add('show-search');
    },
    //  get search profiles

    async search(value) {
      this.profiles = await this.searchAction(value);
      document.querySelector('.search-resault').style.display = 'block';
    },
    // logout
    logout() {
      this.deleteToken();
    },
    // send inv
    async sendInvitation(username, active, disable) {
      await this.sendInvitationAction(username);
      document.querySelector(`.${active}`).style.display = 'inline-block';
      document.querySelector(`.${disable}`).style.display = 'none';
    },
    // accept inv
    async acceptInvitation(username) {
      await this.acceptInvitationAction(username);
      document.querySelector(`.invitation-${username}`).remove();
    },
    // refuse inv
    async refuseInvitation(username) {
      await this.refuseInvitaionAction(username);
      document.querySelector(`.invitation-${username}`).remove();
    },
    // delete friend or invitation request
    async deletefriend(username, active, disable) {
      await this.deleteFriendAction(username);
      document.querySelector(`.${active}`).style.display = 'inline-block';
      document.querySelector(`.${disable}`).style.display = 'none';
    },
  },
  computed: {
    ...mapGetters({
      getInvitations: 'profile/getInvitations',
    }),
  },
  async created() {
    await this.getInvitationsAction();
    this.invitations = this.getInvitations;
  },
  mounted() {
    let input = document.querySelector('#search_input');
    input.addEventListener('keyup', (e) => {
      // if value is not empty send request
      if (input.value !== '') {
        this.search(input.value);
      } else {
        document.querySelector('.search-resault').style.display = 'none';
      }
    });
  },
};
</script>

<style scoped>
@import './assets/css/navbarStyle.css';
</style>
