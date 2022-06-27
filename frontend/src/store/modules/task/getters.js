export default {
  // filter new
  newTasks(state) {
    return state.tasks.filter((task) => task.status == 'new');
  },
  // filter in progress tasks
  inProgressTasks(state) {
    return state.tasks.filter((task) => task.status == 'inProgress');
  },
  // filter completed tasks
  completedTasks(state) {
    return state.tasks.filter((task) => task.status == 'done');
  },
  // get task
  getTask: (state) => (id) => {
    return state.tasks.filter((task) => task.pk === id);
  },
};
