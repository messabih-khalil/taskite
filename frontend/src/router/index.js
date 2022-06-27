import { nextTick } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import store from '../store/modules/authentication/index'
const routes = [
  // dashboard view
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/pages/Dashboard.vue'),
     meta : {
      requireAuth : true
    }
  },
  // tasks view
  {
    path: '/tasks',
    name: 'Tasks',
    component: () => import('../views/pages/Tasks.vue'),
    meta : {
      requireAuth : true
    }
  },
  // project view
  {
    path: '/projects',
    name: 'Projects',
    component: () => import('../views/pages/Projects.vue'),
    meta : {
      requireAuth : true
    }
  },
  // project view
  {
    path: '/team',
    name: 'TeamProject',
    component: () => import('../views/pages/TeamProject.vue'),
    meta : {
      requireAuth : true
    }
  },
  // register view
  {
    path: '/signup',
    name: 'Register',
    component: () => import('../views/authentication/Register.vue'),
    meta : {
      requireAuth : false
    }
  },
  // login view
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/authentication/Login.vue'),
    meta : {
      requireAuth : false
    }
  },
  // ForgetPassword view
  {
    path: '/forget-password',
    name: 'ForgetPassword',
    component: () => import('../views/authentication/ForgetPassword.vue'),
    meta : {
      requireAuth : false
    }
  },
  // New password view
  {
    path: '/password/reset/confirm/:id/:token',
    name: 'NewPassword',
    component: () => import('../views/authentication/NewPassword.vue'),
    meta : {
      requireAuth : false
    }
  },
  // confirm email view
  {
    path: '/confirm/email',
    name: 'ConfirmEmail',
    component: () => import('../views/authentication/ConfirmEmail.vue'),
    meta : {
      requireAuth : false
    }
  },
  // confirm email message view
  {
    path: '/activate/:id/:token',
    name: 'ConfirmEmailMessage',
    component: () => import('../views/authentication/ConfirmEmailMessage.vue'),
    meta : {
      requireAuth : false
    }
  },
  // profile page
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('../views/pages/ProfileSettings.vue'),
    meta : {
      requireAuth : true
    }
  },
  {
    path: '/:pathMatch(.*)*',
    component: () => import('../views/NotFoundPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to , from , next)=>{
  if(!to.meta.requireAuth && store.state.isAuthenticated == true){
    next('/dashboard')
  }else if(to.meta.requireAuth && store.state.isAuthenticated == false){
    next('/login')
  }else{
    next()
  }
  
})

export default router;
