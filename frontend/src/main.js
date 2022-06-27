import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import authstore from './store/modules/authentication/index';

createApp(App).use(store).use(router).mount('#app');


axios.defaults.baseURL = 'http://127.0.0.1:8000/';
if (authstore.state.token != null) {
  axios.defaults.headers.common['Authorization'] = `Bearer ${authstore.state.token}`;
} else {
  axios.defaults.headers.common['Authorization'] = '';
}