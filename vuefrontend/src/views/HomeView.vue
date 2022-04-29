<template>
  <div class="home">

    <img alt="AIOT_Capstone" src="../assets/Dolphin.jpg" >

    <UploadImg msg="Welcome to June's Capstone Test"/>
  </div>
</template>

<script>
// @ is an alias to /src
import UploadImg from '@/components/Uploads.vue'

export default {
  name: 'HomeView',
  components: {
    UploadImg
  }
}
</script>

<style scoped>
img {
  border-radius: 25%;
  border: 5px #333 solid;
  margin-bottom: 1 rem;
  width: 10%;
}
</style>
