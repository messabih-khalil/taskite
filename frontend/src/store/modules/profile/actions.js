import axios from 'axios';

export default {
  // get user profile
  async getProfile(context) {
    // get profile from server side
    await axios
      .get('profiles/')
      .then((response) => {
        context.commit('userProfile', response.data);
      })
      .catch((error) => {});
  },

  // edite profiel
  async editProfile(context, data) {
    await axios
      .put('profiles/', data)
      .then((response) => {
        context.commit('userProfile', response.data);
      })
      .catch((error) => {});
  },
  async editProfileImage(context, data) {
    let image;
    await axios.post(
      'profiles/image/',
      data,
      {
        headers: {
          'Content-Type': 'image/png',
        },
      }
    ).then((response)=>{
      image = response.data["photo_url"]
    });
    return image
  },

  // search friends
  async searchAction(context, username) {
    let profiles;
    await axios.get(`profiles/search/${username}/`).then((response) => {
      profiles = response.data;
    });
    return profiles;
  },
  // send invitation
  async sendInvitation(context, username) {
    let response = await axios.post('friends/add/', {
      friend_name: username,
    });
  },
  // get invitations
  async getInvitationsAction(context) {
    await axios.get('friends/inv/').then((response) => {
      context.commit('commitInvitaion', response.data);
    });
  },
  // accept invitation
  async acceptInvitationAction(context, username) {
    let response = await axios.post('friends/inv/accept/', {
      invitation_from: username,
    });
  },
  // refuse invitation
  async refuseInvitaionAction(context, username) {
    let response = await axios.delete('friends/inv/delete/', {
      data: {
        friend_name: username,
      },
    });
  },
  // delete in progress status friend (invitation sended but not yet accepted or exist friend)
  async deleteFriendAction(context, username) {
    let response = await axios.delete('friends/delete/', {
      data: {
        friend_name: username,
      },
    });
  },
};
