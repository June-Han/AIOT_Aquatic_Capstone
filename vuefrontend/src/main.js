import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

/*App and router from vue files, 
#app is id from the division in index.html*/
createApp(App).use(router).mount('#app')
