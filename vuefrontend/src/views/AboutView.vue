<template>
  <div class="about" width="100%" height="100%">
    <h1>{{title_msg}}</h1>

    <projectInfo msg="About this project: "/>

    <h3>The project is built with: </h3>
    <div id="imgFlow">
      <img title="Vue JS" alt="Vue_JS" src="../assets/vue.png" />
      <img title="D3 JS" alt="D3_JS" src="../assets/d3.png" />
      <img title="Azure Function" alt="AzureFunction" src="../assets/azure_function.png" />
      <img title="Flask" alt="flask" src="../assets/flask.png" />
      <img title="Tensorflow" alt="tensorflow" src="../assets/tensor.png" />
      <img title="Azure Custom Vision" alt="Custom Vision" src="../assets/customvision.png" />
    </div>
    
  </div>
</template>

<script>
import projectInfo from '@/components/AboutInfo.vue'

export default {
  name: 'AboutView',
  components: {
    projectInfo
  },
  data(){
    return {
      title_msg: "AIOT solution for Coral Reef Preservation",
    }
  }
}
</script>

<style scoped>
img {
  border-radius: 10%;
  margin-bottom: 1 rem;
  width: 10%;
}

#imgFlow {
  margin: auto;
  display: flex;
  flex-flow: wrap;
  align-items: center;
  justify-content: center;
}

</style>
