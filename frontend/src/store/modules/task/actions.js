import axios from 'axios';

export default {
  // get all tasks from server side
  async getTasks(context, data) {
    await axios
      .get('tasks/')
      .then((response) => {
        // commit tasks state
        context.commit('commitTasks', response.data);
      })
      .catch((error) => {
      });
  },
  // change tasks status
  // change status to new
  async newTask(context, id) {
    await axios
      .put(`tasks/status/${id}/`, {
        status: 'new',
      })
      .then()
      .catch((error) => {
        alert('error');
      });
  },
  // change status to in progress
  async inProgressTask(context, id) {
    await axios
      .put(`tasks/status/${id}/`, {
        status: 'inProgress',
      })
      .then()
      .catch((error) => {
        alert('error');
      });
  },
  // change status to done
  async completedTask(context, id) {
    await axios
      .put(`tasks/status/${id}/`, {
        status: 'done',
      })
      .then()
      .catch((error) => {
        alert('error');
      });
  },
  // edit task
  async editTask(context, task) {
    await axios
      .put(`tasks/${task.pk}/`, {
        title: task.title,
        description: task.description,
        start_time: task.start_time,
        end_time: task.end_time,
      })
      .then((response) => {})
      .catch((error) => {});
  },
  // delete task
  async deleteTask(context, id) {
    const deleteTask = await axios.delete(`tasks/${id}/`);
  },
  // create task
  async createTask(context, task) {
    let taskData;
    await axios
      .post('tasks/', {
        title: task.title,
        description: task.description,
        start_time: task.start_time,
        end_time: task.end_time,
      })
      .then((response) => {
        taskData = response.data;
      });
    return taskData;
  },
};
