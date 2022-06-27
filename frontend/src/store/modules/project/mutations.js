export default {
    // commit projects
    commitProjects(state , payload){
        state.projects = payload
    },
    // commit friends
    commitFriends(state , payload){
        state.friends = payload
    },
    // commit team projects
    commitTeamProjects(state , payload){
        state.teamProject = payload
    },

}