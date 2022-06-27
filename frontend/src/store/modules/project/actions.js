import axios from 'axios';

export default {
  // get all projects
  async getAllProjectsAction(context) {
    await axios
      .get('projects/')
      .then((response) => {
        context.commit('commitProjects', response.data);
      })
      .catch((error) => {});
  },
  // get team project
  async getTeamProjectAction(context) {
    await axios
      .get('projects/team/')
      .then((response) => {
        context.commit('commitTeamProjects', response.data);
      })
      .catch((error) => {});
  },
  // get friends
  async getFriendsAction(context) {
    await axios
      .get('friends/')
      .then((response) => {
        context.commit('commitFriends', response.data);
      })
      .catch((error) => {});
  },
  // update project status
  // -> change status to new
  async newProjectAction(context, id) {
    await axios
      .put(`projects/status/${id}/`, {
        status: 'new',
      })
      .then()
      .catch((error) => {});
  },
  // -> change status to in progress
  async inProgressProjectAction(context, id) {
    await axios
      .put(`projects/status/${id}/`, {
        status: 'inProgress',
      })
      .then()
      .catch((error) => {});
  },
  // -> change status to done
  async completedProjectAction(context, id) {
    await axios
      .put(`projects/status/${id}/`, {
        status: 'done',
      })
      .then()
      .catch((error) => {});
  },

  // update project
  async updateProjectAction(context, data) {
    await axios
      .put(`projects/${data.project.pk}/`, {
        title: data.project.title,
        description: data.project.description,
        team: JSON.parse(JSON.stringify(data.team)),
        start_date: data.project.start_date,
        end_date: data.project.end_date,
      })
      .then((response) => {})
      .catch((err) => {});
  },
  // delete project
  async deleteProjectAction(context, id) {
    let deleteProject = await axios.delete(`/projects/${id}/`);
  },
  // post project
  async createProjectAction(context, data) {
    let responseData;
    await axios.post('projects/', data).then((response) => {
      responseData = response.data;
    });
    return responseData;
  },
};
