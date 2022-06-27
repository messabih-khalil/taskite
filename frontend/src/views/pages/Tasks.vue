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
          <div
            class="create-task-button is-flex is-align-items-center"
            @click.prevent="activePopup"
          >
            <i class="ri-add-circle-line mr-2"></i>
            <span>Create a Task</span>
          </div>
          <!-- popup -->
          <div class="popup-section">
            <div class="popup-overlay"></div>
            <div class="popup">
              <header
                class="is-flex is-justify-content-space-between is-align-items-center"
              >
                <p></p>
                <p>Task</p>
                <p></p>
                <i
                  class="ri-close-circle-line close-popup"
                  @click.prevent="closePopup()"
                ></i>
              </header>
              <section class="popup-body">
                <label>Task name</label>
                <input
                  type="text"
                  class="input"
                  placeholder="task title"
                  v-model="task.title"
                />
                <label>Task Description</label>
                <textarea
                  class="textarea"
                  placeholder="task description"
                  v-model="task.description"
                ></textarea>
                <label>Start time</label>
                <input type="time" class="input" v-model="task.start_time" />
                <label>End time</label>
                <input type="time" class="input" v-model="task.end_time" />
              </section>
              <footer
                class="is-flex is-justify-content-space-between is-align-items-center"
              >
                <p></p>
                <button
                  class="button is-primary is-light mt-5"
                  @click.prevent="updateTask()"
                  id="editButton"
                  v-if="task.pk"
                >
                  Send
                </button>
                <button
                  class="button is-primary is-light mt-5"
                  @click.prevent="createTask()"
                  id="createButton"
                  v-if="task.pk == null"
                >
                  Create
                </button>
              </footer>
            </div>
          </div>

          <!--  -->
          <div class="tasks-status">
            <!-- to do -->
            <div class="to-do">
              <div class="task-status-title">
                <span>To Do</span>
                <span class="line-style"></span>
              </div>

              <!-- task boxes -->

              <div class="task-boxes" id="toDo" @add="newStatus">
                <div
                  v-for="task in tasks.newTasks"
                  :key="task.pk"
                  id="newTasksBoxes"
                >
                  <div class="task-box" v-bind:id="task.pk">
                    <div
                      class="task-title-and-action is-flex is-justify-content-space-between is-align-items-center"
                    >
                      <!-- task title -->
                      <span class="task-title"> {{ task.title }} </span>
                      <!-- task action -->
                      <div class="actions">
                        <!-- edit -->
                        <i
                          class="ri-pencil-line mr-2"
                          @click.prevent="editTask(task.pk)"
                        ></i>
                        <!-- delete -->
                        <i
                          class="ri-close-circle-line"
                          @click.prevent="deleteTask(task.pk)"
                        ></i>
                      </div>
                    </div>
                    <!-- task description -->
                    <div class="task-description mt-2">
                      <p>
                        {{ task.description }}
                      </p>
                    </div>
                    <!-- task delay -->
                    <div class="task-delay is-flex is-align-items-center mt-2">
                      <i class="ri-time-line mr-2"></i>
                      <p>{{ task.start_time }} - {{ task.end_time }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- In Progress -->
            <div>
              <div class="task-status-title">
                <span>In Progress</span>
                <span class="line-style" style="background: purple"></span>
              </div>

              <!-- task boxes -->

              <div class="task-boxes" id="inProgress" @add="inProgressStatus">
                <div v-for="task in tasks.inProgressTasks" :key="task.pk">
                  <div class="task-box" v-bind:id="task.pk">
                    <div
                      class="task-title-and-action is-flex is-justify-content-space-between is-align-items-center"
                    >
                      <!-- task title -->
                      <span class="task-title"> {{ task.title }} </span>
                      <!-- task action -->
                      <div class="actions">
                        <!-- edit -->
                        <i
                          class="ri-pencil-line mr-2"
                          @click.prevent="editTask(task.pk)"
                        ></i>
                        <!-- delete -->
                        <i
                          class="ri-close-circle-line"
                          @click.prevent="deleteTask(task.pk)"
                        ></i>
                      </div>
                    </div>
                    <!-- task description -->
                    <div class="task-description mt-2">
                      <p>
                        {{ task.description }}
                      </p>
                    </div>
                    <!-- task delay -->
                    <div class="task-delay is-flex is-align-items-center mt-2">
                      <i class="ri-time-line mr-2"></i>
                      <p>{{ task.start_time }} - {{ task.end_time }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- done -->
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
                <div v-for="task in tasks.completedTasks" :key="task.pk">
                  <div class="task-box" v-bind:id="task.pk">
                    <div
                      class="task-title-and-action is-flex is-justify-content-space-between is-align-items-center"
                    >
                      <!-- task title -->
                      <span class="task-title"> {{ task.title }} </span>
                      <!-- task action -->
                      <div class="actions">
                        <!-- edit -->
                        <i
                          class="ri-pencil-line mr-2"
                          @click.prevent="editTask(task.pk)"
                        ></i>
                        <!-- delete -->
                        <i
                          class="ri-close-circle-line"
                          @click.prevent="deleteTask(task.pk)"
                        ></i>
                      </div>
                    </div>
                    <!-- task description -->
                    <div class="task-description mt-2">
                      <p>
                        {{ task.description }}
                      </p>
                    </div>
                    <!-- task delay -->
                    <div class="task-delay is-flex is-align-items-center mt-2">
                      <i class="ri-time-line mr-2"></i>
                      <p>{{ task.start_time }} - {{ task.end_time }}</p>
                    </div>
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
      tasks: {
        newTasks: null,
        inProgressTasks: null,
        completedTasks: null,
      },
      task: {
        title: '',
        description: '',
        start_time: '',
        end_time: '',
      },
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
    // get task data
    async gettingTask(id) {
      let task = await this.getTask(id);
      this.task = task[0];
    },
    editTask(id) {
      actions.editPopup();
      this.gettingTask(id);
    },
    // update task
    async updateTask() {
      await this.editTaskAction(this.task);
      this.closePopup();
      this.task = {
        title: '',
        description: '',
        start_time: '',
        end_time: '',
      };
    },
    // delete task
    async deleteTask(id) {
      await this.deleteTaskAction(id);
      const task = document.getElementById(id);
      task.remove();
    },
    // create task
    async createTask() {
      const task = await this.createTaskAction(this.task);
      document.getElementById('newTasksBoxes').innerHTML += `
        <div class="task-box" v-bind:id=${task.pk}>
                    <div
                      class="task-title-and-action is-flex is-justify-content-space-between is-align-items-center"
                    >
                      <!-- task title -->
                      <span class="task-title"> ${task.title} </span>
                      <!-- task action -->
                      <div class="actions">
                        <!-- edit -->
                        <i
                          class="ri-pencil-line mr-2"
                          @click.prevent="editTask(${task.pk})"
                        ></i>
                        <!-- delete -->
                        <i
                          class="ri-close-circle-line"
                          @click.prevent="deleteTask(${task.pk})"
                        ></i>
                      </div>
                    </div>
                    <!-- task description -->
                    <div class="task-description mt-2">
                      <p>
                        ${task.description}
                      </p>
                    </div>
                    <!-- task delay -->
                    <div class="task-delay is-flex is-align-items-center mt-2">
                      <i class="ri-time-line mr-2"></i>
                      <p>${task.start_time} - ${task.end_time}</p>
                    </div>
                  </div>
        `;

      this.task = {
        title: '',
        description: '',
        start_time: '',
        end_time: '',
      };
    },
    // actions
    ...mapActions({
      // get all tasks action
      getTasks: 'task/getTasks',
      // change status action
      newTask: 'task/newTask',
      inProgressTask: 'task/inProgressTask',
      completedTask: 'task/completedTask',
      // edit task action
      editTaskAction: 'task/editTask',
      // delete action
      deleteTaskAction: 'task/deleteTask',
      // create task
      createTaskAction: 'task/createTask',
    }),
    // change status of tasks
    //  change status to new
    async newStatus(event) {
      await this.newTask(event.item.children[0].id);
    },
    // change status to in progress
    async inProgressStatus(event) {
      await this.inProgressTask(event.item.children[0].id);
    },
    // change status to done
    async doneStatus(event) {
      await this.completedTask(event.item.children[0].id);
    },
  },
  computed: {
    // getters
    ...mapGetters({
      newTasks: 'task/newTasks',
      inProgressTasks: 'task/inProgressTasks',
      completedTasks: 'task/completedTasks',
      // get task
      getTask: 'task/getTask',
    }),
  },
  async created() {
    await this.getTasks();
    this.tasks.newTasks = this.newTasks;
    this.tasks.inProgressTasks = this.inProgressTasks;
    this.tasks.completedTasks = this.completedTasks;
    dragAndDrop();
  },
};
</script>

<style scoped>
@import './assets/css/tasksAndProject.css';
</style>
