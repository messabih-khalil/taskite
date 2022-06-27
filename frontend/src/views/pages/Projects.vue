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
          <!-- create button -->
          <div
            class="create-task-button is-flex is-align-items-center"
            @click.prevent="activePopup()"
          >
            <i class="ri-add-circle-line mr-2"></i>
            <span>Create a Project</span>
          </div>
          <!-- popup -->
          <div class="popup-section">
            <div class="popup-overlay"></div>
            <div class="popup">
              <header
                class="is-flex is-justify-content-space-between is-align-items-center"
              >
                <p></p>
                <p>Project</p>
                <p></p>
                <i
                  class="ri-close-circle-line close-popup"
                  @click.prevent="closePopup()"
                ></i>
              </header>
              <section class="popup-body">
                <label>Project name</label>
                <input
                  type="text"
                  class="input"
                  placeholder="Project name"
                  v-model="project.title"
                />
                <label>Project Description</label>
                <textarea
                  class="textarea"
                  placeholder="Project description"
                  v-model="project.description"
                ></textarea>
                <!-- friend box -->
                <span>Team</span>
                <div class="friends-box mt-2">
                  <!-- search -->
                  <div class="search-friends mb-3">
                    <input type="text" placeholder="Find your friend" />
                    <i class="ri-search-2-line"></i>
                  </div>
                  <div class="boxes-of-friends">
                    <div
                      class="friend-box"
                      v-bind:id="user.username"
                      v-for="user in friends"
                      :key="user.username"
                      @click.prevent="toggleFriend(user.username)"
                    >
                      <!-- friend image -->
                      <div class="image is-32x32">
                        <img class="is-rounded" :src="user.photo_url" />
                      </div>
                      <p class="username ml-2">{{ user.username }}</p>
                    </div>
                  </div>
                </div>
                <!-- dead line project -->
                <div class="is-flex is-align-items-center dead-line mt-2">
                  <div>
                    <label for="">From </label>
                    <input
                      type="date"
                      class="input"
                      v-model="project.start_date"
                    />
                  </div>
                  <div class="ml-2">
                    <label for="">To</label>
                    <input
                      type="date"
                      class="input"
                      v-model="project.end_date"
                    />
                  </div>
                </div>
              </section>
              <footer
                class="is-flex is-justify-content-space-between is-align-items-center"
              >
                <p></p>
                <button
                  class="button is-primary is-light mt-5"
                  @click.prevent="updateProject"
                  v-if="project.pk != null"
                >
                  Update
                </button>
                <button
                  class="button is-primary is-light mt-5"
                  @click.prevent="createProject"
                  v-if="project.pk == null"
                >
                  Create
                </button>
              </footer>
            </div>
          </div>
          <!--  -->
          <div class="tasks-status">
            <!-- to do -->
            <div>
              <div class="task-status-title">
                <span>To Do</span>
                <span class="line-style"></span>
              </div>

              <!-- task boxes -->

              <div class="task-boxes" id="toDo" @add="newStatus">
                <div
                  v-for="project in projects.newProject"
                  :key="project.pk"
                  id="newProject"
                >
                  <div class="task-box" v-bind:id="project.pk">
                    <div
                      class="task-title-and-action is-flex is-justify-content-space-between is-align-items-center"
                    >
                      <!-- task title -->
                      <span class="task-title"> {{ project.title }} </span>
                      <!-- task action -->
                      <div class="actions">
                        <!-- edit -->
                        <i
                          class="ri-pencil-line mr-2"
                          @click.prevent="editPopup(project.pk)"
                        ></i>
                        <!-- delete -->
                        <i
                          class="ri-close-circle-line"
                          @click.prevent="deleteProject(project.pk)"
                        ></i>
                      </div>
                    </div>
                    <!-- task description -->
                    <div class="task-description mt-2">
                      <p>
                        {{ project.description }}
                      </p>
                    </div>
                    <!-- team project -->
                    <div class="project-team mt-1 mb-1">
                      <div
                        class="is-flex is-align-items-center"
                        v-for="user in project.users_profile"
                        :key="user.username"
                      >
                        <div class="image">
                          <img :src="user.photo_url" />
                        </div>
                      </div>
                    </div>
                    <!-- task delay -->
                    <div class="task-delay is-flex is-align-items-center mt-2">
                      <i class="ri-calendar-event-fill mr-2"></i>
                      <p>{{ project.start_date }} / {{ project.end_date }}</p>
                    </div>
                    <!-- more details -->
                    <button
                      class="button is-info is-outlined more-details-button mt-3"
                    >
                      More Details
                    </button>
                  </div>
                </div>
              </div>
            </div>
            <!-- In Progress -->
            <div>
              <div class="task-status-title">
                <span>In Progress</span>
                <span class="line-style blue" style="background: purple"></span>
              </div>

              <!-- task boxes -->

              <div class="task-boxes" id="inProgress" @add="inProgressStatus">
                <div v-for="project in projects.inProgress" :key="project.pk">
                  <div class="task-box" v-bind:id="project.pk">
                    <div
                      class="task-title-and-action is-flex is-justify-content-space-between is-align-items-center"
                    >
                      <!-- task title -->
                      <span class="task-title"> {{ project.title }} </span>
                      <!-- task action -->
                      <div class="actions">
                        <!-- edit -->
                        <i
                          class="ri-pencil-line mr-2"
                          @click.prevent="editPopup(project.pk)"
                        ></i>
                        <!-- delete -->
                        <i class="ri-close-circle-line"></i>
                      </div>
                    </div>
                    <!-- task description -->
                    <div class="task-description mt-2">
                      <p>
                        {{ project.description }}
                      </p>
                    </div>
                    <!-- team project -->
                    <div
                      class="project-team mt-1 mb-1"
                      v-for="user in project.users_profile"
                      :key="user.username"
                    >
                      <div class="image is-48x48">
                        <img :src="user.photo_url" />
                      </div>
                    </div>
                    <!-- task delay -->
                    <div class="task-delay is-flex is-align-items-center mt-2">
                      <i class="ri-calendar-event-fill mr-2"></i>
                      <p>{{ project.start_date }} / {{ project.end_date }}</p>
                    </div>
                    <!-- more details -->
                    <button
                      class="button is-info is-outlined more-details-button mt-3"
                    >
                      More Details
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <div>
              <div class="task-status-title">
                <span>Done</span>
                <span
                  class="line-style"
                  style="background: rgb(0, 255, 64)"
                ></span>
              </div>

              <!-- task boxes -->

              <div class="task-boxes" id="done" @add="doneStatus">
                <div v-for="project in projects.completed" :key="project.pk">
                  <div class="task-box" v-bind:id="project.pk">
                    <div
                      class="task-title-and-action is-flex is-justify-content-space-between is-align-items-center"
                    >
                      <!-- task title -->
                      <span class="task-title"> {{ project.title }} </span>
                      <!-- task action -->
                      <div class="actions">
                        <!-- edit -->
                        <i
                          class="ri-pencil-line mr-2"
                          @click.prevent="editPopup(project.pk)"
                        ></i>
                        <!-- delete -->
                        <i class="ri-close-circle-line"></i>
                      </div>
                    </div>
                    <!-- task description -->
                    <div class="task-description mt-2">
                      <p>
                        {{ project.description }}
                      </p>
                    </div>
                    <!-- team project -->
                    <div
                      class="project-team mt-1 mb-1"
                      v-for="user in project.users_profile"
                      :key="user.username"
                    >
                      <div class="image is-48x48">
                        <img :src="user.photo_url" />
                      </div>
                    </div>
                    <!-- task delay -->
                    <div class="task-delay is-flex is-align-items-center mt-2">
                      <i class="ri-calendar-event-fill mr-2"></i>
                      <p>{{ project.start_date }} / {{ project.end_date }}</p>
                    </div>
                    <!-- more details -->
                    <button
                      class="button is-info is-outlined more-details-button mt-3"
                    >
                      More Details
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Panel from '@/components/Panel.vue';
import Navbar from '@/components/Navbar.vue';
// import from pages/assets/js
import dragAndDrop from './assets/js/dragAndDrop';
import { actions } from './assets/js/actions';
// import library

// import maps

import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      projects: {
        newProject: null,
        inProgress: null,
        completed: null,
      },
      project: {
        title: '',
        description: '',
        users_profile: [],
        start_date: '',
        end_date: '',
      },
      team: [],
      friends: [],
    };
  },
  components: {
    Panel,
    Navbar,
  },
  methods: {
    activePopup() {
      actions.activePopup();
    },
    closePopup() {
      actions.closePopup();
    },
    async editPopup(id) {
      actions.editPopup();
      // get project data
      await this.getProjectData(id);
      // adding border color to friends team
      this.addingBorderColorToTeam();
    },
    // get team inside the project
    async getProjectData(id) {
      this.project = await this.getProject(id)[0];
      // get all users inside the project by username
      this.project.users_profile.map((user) => this.team.push(user.username));
      // get friends
      this.getMyFriend();
    },
    // get all projects
    addingBorderColorToTeam() {
      this.team.map((username) =>
        document.getElementById(username).classList.add('team-friend')
      );
    },
    // get my team project

    // get my friend
    getMyFriend() {
      this.friends = this.getFriends;
    },
    // create project

    async createProject() {
      let data = {
        ...this.project,
        team: JSON.parse(JSON.stringify(this.team)),
      };
      await this.createProjectAction(data);
      window.location.reload();
    },
    // update project
    async updateProject() {
      // update project action
      let data = {
        project: this.project,
        team: this.team,
      };
      await this.updateProjectAction(data);
      this.closePopup();
      this.project = {
        title: '',
        description: '',
        start_date: '',
        end_date: '',
      };
    },
    // add or remove friend from team project
    toggleFriend(username) {
      let friend = document.getElementById(username);
      // toggle friend
      friend.classList.toggle('team-friend');
      // check if div has class name team-friend or not
      if (friend.classList.contains('team-friend')) {
        this.team.push(username);
      } else {
        let usernameIndex = this.team.indexOf(username); //get  "car" index
        //remove car from the colors array
        this.team.splice(usernameIndex, 1);
      }
    },

    // delete project
    async deleteProject(id) {
      await this.deleteProjectAction(id);
      document.getElementById(id).remove();
    },
    // change status project
    // -> change project to new project
    async newStatus(event) {
      await this.newProjectAction(event.item.children[0].id);
    },
    // -> change project to in progress project
    async inProgressStatus(event) {
      await this.inProgressStatusAction(event.item.children[0].id);
    },
    // -> change project to completed project
    async doneStatus(event) {
      await this.doneStatusAction(event.item.children[0].id);
    },

    // use map actions
    ...mapActions({
      getAllProjectsAction: 'project/getAllProjectsAction',
      getTeamProjectAction: 'project/getTeamProjectAction',
      getFriendsAction: 'project/getFriendsAction',
      newProjectAction: 'project/newProjectAction',
      inProgressStatusAction: 'project/inProgressProjectAction',
      doneStatusAction: 'project/completedProjectAction',
      updateProjectAction: 'project/updateProjectAction',
      deleteProjectAction: 'project/deleteProjectAction',
      createProjectAction: 'project/createProjectAction',
    }),
  },
  async created() {
    // get all tasks
    await this.getAllProjectsAction();
    this.projects.newProject = this.getNewProjects;
    this.projects.inProgress = this.getProgressProjects;
    this.projects.completed = this.getCompletedProjects;
    // get my friends
    await this.getFriendsAction();
    this.friends = this.getFriends;
    // get team projects
    await this.getTeamProjectAction();
  },
  computed: {
    // use map getters
    ...mapGetters({
      // get new project
      getNewProjects: 'project/getNewProjects',
      // get in progress project
      getProgressProjects: 'project/getProgressProjects',
      // get completed project
      getCompletedProjects: 'project/getCompletedProjects',
      // get project
      getProject: 'project/getProject',
      // get friends
      getFriends: 'project/getFriends',
      // get filtred friends from team
      filterFriends: 'project/filterFriends',
    }),
  },
  mounted() {
    dragAndDrop();
  },
};
</script>

<style scoped>
@import './assets/css/tasksAndProject.css';
.project-team {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}
.image {
  display: flex;
  align-items: center;
  justify-items: center;
  border-radius: 50%;
  height: 30px;
  width: 30px;
  overflow: hidden;
}
.image img {
  object-fit: cover;
  height: 30px;
  width: 30px;
}

.dead-line > div {
  width: 50%;
}
</style>
