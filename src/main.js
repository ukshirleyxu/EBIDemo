// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview';
import '../static/iviewtheme/index.less';
//import 'iview/dist/styles/iview.css';//we could use our own theme directory:import './assets/my-theme/index.less'; 'index.css' need to be created properly according to iview instruction.
import locale from 'iview/dist/locale/en-US';
import VueResource  from 'vue-resource'


Vue.config.productionTip = false
Vue.use(iView, { locale });
Vue.use(VueResource);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
