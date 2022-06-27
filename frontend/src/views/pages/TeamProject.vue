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
          <!-- team project -->
          <!-- <h3 class="title">Team project</h3> -->
          <!-- filter project -->
          <div class="filter-projects">
            <div class="is-flex is-align-items-center" style="width: 100%">
              <!-- start date -->
              <div class="mr-2" style="width: 100%">
                <span>By start date : </span>
                <input type="date" class="input mt-2" v-model="start_date" />
              </div>
              <!-- end date -->
              <div class="mr-2" style="width: 100%">
                <span>By end date : </span>
                <input type="date" class="input mt-2" v-model="end_date" />
              </div>
            </div>
            <!-- button filter -->
            <button
              class="button is-info is-outlined is-flex is-align-items-center"
              @click.prevent="filter"
            >
              <i class="ri-filter-2-line mr-2"></i>
              <span>Filter</span>
            </button>
          </div>
          <!-- team project items -->
          <h5 class="title mt-4" style="margin-bottom: 0">Projects :</h5>
          <div
            class="team-projects mt-4"
            v-for="project in projects"
            :key="project.pk"
          >
            <div class="project">
              <div class="title-and-status">
                <!-- project title -->
                <span class="project-title">{{ project.title }}</span>
                <!-- project status -->
                <div class="status">
                  <!-- new project -->
                  <div
                    class="new-project-status"
                    v-if="project.status == 'new'"
                  >
                    <p>New</p>
                  </div>
                  <!-- in progress -->
                  <div
                    class="in-progress-project-status"
                    v-if="project.status == 'inProgress'"
                  >
                    <p>In progress</p>
                  </div>

                  <!-- completed -->
                  <div
                    class="completed-project-status"
                    v-if="project.status == 'done'"
                  >
                    <p>Completed</p>
                  </div>
                </div>
              </div>
              <!-- project description -->
              <div class="description mt-3">
                <span>{{ project.description }}</span>
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
              <!-- project deadline -->
              <div class="project-deadline mt-3">
                {{ project.start_date }} To {{ project.end_date }}
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
// import maps
import { mapActions, mapGetters } from 'vuex';
export default {
  data() {
    return {
      projects: [],
      filterProjects: [],
      start_date: null,
      end_date: null,
    };
  },
  components: {
    Panel,
    Navbar,
  },
  methods: {
    // map action methods
    ...mapActions({
      getTeamProjectAction: 'project/getTeamProjectAction',
    }),
    // filter project
    filter() {
      let dates = {
        start_date: this.start_date,
        end_date: this.end_date,
      };
      this.projects = this.filterProject(dates);
    },
  },
  computed: {
    ...mapGetters({
      getTeamProject: 'project/getTeamProject',
      filterProject: 'project/filterProject',
    }),
  },
  async created() {
    await this.getTeamProjectAction();
    this.projects = this.getTeamProject;
  },
};
</script>

<style scoped>
.title {
  color: var(--font-color);
}

.filter-projects {
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
  width: 100%;
  color: var(--font-color);
}

input[type='date'] {
  background: var(--main-dark-color);
  border: none;
  color: var(--font-color);
}

/* project items */
.new-project-status,
.in-progress-project-status,
.completed-project-status {
  padding: 0.5rem;
  border-radius: 10px;
  width: fit-content;
  color: var(--font-color);
}

.new-project-status {
  background-color: #14cdfb;
}
.in-progress-project-status {
  background-color: purple;
}
.completed-project-status {
  background-color: rgb(0, 255, 64);
}

.title-and-status {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: var(--font-color);
}

.project-title {
  /* font-weight: 600; */
  font-size: 1.1rem;
}

.project {
  background-color: var(--main-dark-color);
  padding: 1rem;
  border-radius: 10px;
}

.description {
  color: var(--font-grey-color);
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

.project-deadline {
  color: var(--font-color);
}

@media only screen and (max-width: 520px) {
  .filter-projects {
    flex-direction: column;
    align-items: flex-start;
  }
  .filter-projects button {
    margin-top: 1rem;
    width: 100%;
  }
}
</style>
