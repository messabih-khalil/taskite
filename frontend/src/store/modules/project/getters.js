export default {
  // get new project
  getNewProjects(state) {
    return state.projects.filter((project) => project.status == 'new');
  },
  // get in progress project
  getProgressProjects(state) {
    return state.projects.filter((project) => project.status == 'inProgress');
  },

  // get completed project
  getCompletedProjects(state) {
    return state.projects.filter((project) => project.status == 'done');
  },
  // get friends in team project
  getProject: (state) => (id) => {
    return state.projects.filter((project) => project.pk === id);
  },
  // get friends
  getFriends(state) {
    return state.friends;
  },

  // get team project
  getTeamProject(state) {
    return state.teamProject;
  },
  // filter by date
  filterProject: (state) => (dates) => {
    var startDate = new Date(dates.start_date).toLocaleDateString();
    var endDate = new Date(dates.end_date).toLocaleDateString();
    if (dates.end_date == null && dates.start_date == null) {
      return state.teamProject;
    }
    if (dates.start_date == null) {
      var resultProjectsData = state.teamProject.filter((project) => {
        var date = new Date(project.end_date).toLocaleDateString();
        return date == endDate;
      });
      return resultProjectsData;
    } else if (dates.end_date == null) {
      var resultProjectsData = state.teamProject.filter((project) => {
        var date = new Date(project.start_date).toLocaleDateString();
        return date === startDate;
      });
      return resultProjectsData;
    } else {
      var resultProjectsData = state.teamProject.filter((project) => {
        var start_date = new Date(project.start_date).toLocaleDateString();
        var end_date = new Date(project.end_date).toLocaleDateString();
        return startDate >= start_date && endDate <= end_date;
      });
      return resultProjectsData;
    }
  },
};
