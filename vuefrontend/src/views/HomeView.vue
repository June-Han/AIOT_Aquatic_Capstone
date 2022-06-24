<template>
  <div class="home" width="100%" height="100%">
    <h1>AIOT solution for Coral Reef Preservation</h1>

    <img alt="AIOT_Capstone" src="../assets/Dolphin.jpg" />

    <UploadImg msg="Machine Learning Model for Coral Health Classification Demo"/>
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
