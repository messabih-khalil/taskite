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
          <!-- dashboard section -->
          <div class="dashboard">
            <!-- tasks section -->
            <div class="my-box my-tasks">
              <div
                class="header is-flex is-align-items-center is-justify-content-space-between mb-4"
              >
                <span>Number of task</span>
              </div>

              <div class="body">
                <canvas id="myChart2" class="canvas-body"></canvas>
              </div>
            </div>
            <!-- project section -->
            <div class="my-box my-projects">
              <div
                class="header is-flex is-align-items-center is-justify-content-space-between mb-4"
              >
                <span>Tasks And Projects</span>
                <div class="add-new"></div>
              </div>

              <carousel :items-to-show="1">
                <slide class="body">
                  <canvas id="myChart" class="canvas-body"></canvas>
                </slide>
                <slide class="body">
                  <canvas id="myChart4" class="canvas-body"></canvas>
                </slide>
              </carousel>
            </div>

            <!-- latest News -->
            <div class="my-box latest-news">
              <div
                class="header is-flex is-align-items-center is-justify-content-space-between mb-4"
              >
                <span>Latest News</span>
                <div class="add-new"></div>
              </div>

              <div class="body">
                <div
                  class="news-cards mb-3"
                  v-for="news in newsData"
                  :key="news.id"
                >
                  <a class="news-card" :href="news.url">
                    <!-- news title -->
                    <div class="news-title">
                      <p>{{ news.title }}</p>
                    </div>
                    <!-- news date  -->
                    <div class="news-date is-flex is-align-items-center">
                      <i class="ri-calendar-todo-fill mr-2 mt-2 mb-2"></i>
                      <p>{{ news.publishedAt }}</p>
                    </div>
                    <!-- news image -->
                    <div class="news-image">
                      <img :src="news.urlToImage" alt="" />
                    </div>
                    <!--  -->
                  </a>
                </div>
              </div>
            </div>
            <!-- Daily productivity -->
            <div class="my-box graphs">
              <div
                class="header is-flex is-align-items-center is-justify-content-space-between mb-4"
              >
                <span>Productivity</span>
                <div class="add-new"></div>
              </div>
              <div class="canvas">
                <canvas id="myChart3" class="canvas-body"></canvas>
              </div>
            </div>
            <p class="mg show-mg">.</p>
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
import graphs from './assets/js/graphs';

// import library
import axios from 'axios';
// impot carousel
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide } from 'vue3-carousel';
// import maps
import { mapActions } from 'vuex';

export default {
  data() {
    return {
      newsData: [],
    };
  },
  components: {
    Panel,
    Navbar,
    Carousel,
    Slide,
  },
  methods: {
    ...mapActions({
      userId : 'authentication/userID'
    }),
    async getNews() {
      let news = await axios.get(
        'https://newsapi.org/v2/top-headlines?country=us&apiKey=005ec99fa0f84c988e14860b17239607'
      );
      this.newsData = news.data.articles;
    },
  },
  mounted() {
    graphs();

    this.getNews();
  },

  // async created() {
  //   await this.userId()
  // },
};
</script>

<style scoped>
@import './assets/css/dashboard.css';
</style>
