import { createStore } from 'vuex'
import authentication from './modules/authentication/index'
import profile from './modules/profile/index'
import task from './modules/task/index'
import project from './modules/project/index'


export default createStore({
  modules: {
    authentication,
    profile,
    task,
    project,
  }
})
