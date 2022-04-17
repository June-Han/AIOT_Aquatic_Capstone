<template>
  <div class="home">
    <img alt="AIOT_Capstone" src="../assets/Dolphin.jpg" >
    <HelloWorld msg="Welcome to June's Capstone Test"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>

<style scoped>
img {
  border-radius: 25%;
  border: 5px #333 solid;
  margin-bottom: 1 rem;
  width: 18%;
}
</style>
