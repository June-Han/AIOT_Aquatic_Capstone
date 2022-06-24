<template>
  <div class="usageExample">
    <h1>{{msg}}</h1>
    <h2>Intended Usage Example</h2>
    <h3 class="text">About:</h3>
    <div class = "text"> 
        Intended usage is to monitor different areas of coral clusters from images taken across several cameras. 
        These images will then be used as input for the machine learning model to identify and classify the coral health conditions. <br/>
        The results will be reported to this user interface, where each image classification for 
        different coral clusters from different cameras would be shown in one grid each as shown below.
    </div>
    <div id="imageGrid">
        <div class="gridItem">
            <img alt="AIOT_Capstone" src="../assets/coralExample/healthy1.jpg" />
            <div class="font-weight-bold">Prediction: Healthy </div>
            <div class="font-weight-bold">Probability: 96.637 % </div>
        </div>
        <div class="gridItem">
            <img alt="AIOT_Capstone" src="../assets/coralExample/bleached1.jpg" />
            <div class="font-weight-bold">Prediction: Bleached </div>
            <div class="font-weight-bold">Probability: 95.685 % </div>
        </div>
        <div class="gridItem">
            <img alt="AIOT_Capstone" src="../assets/coralExample/healthy2.jpg" />
            <div class="font-weight-bold">Prediction: Healthy</div>
            <div class="font-weight-bold">Probability: 98.654 % </div>
        </div>
        <div class="gridItem">
            <img alt="AIOT_Capstone" src="../assets/coralExample/bleached2.png" />
            <div class="font-weight-bold">Prediction: Bleached</div>
            <div class="font-weight-bold">Probability: 97.438 % </div>
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'intendedUsage',
  props: {
    msg: String,
  }
}
</script>

<style scoped>
#imageGrid {
    display: flex;
    flex-wrap: wrap;
    margin: auto;
}

.gridItem {
    max-width: 500px;
    border: 1px solid steelblue;
    margin: auto;
    padding: 30px;
    border-radius: 5px;
}
.text{
    text-align: left;
    margin: 10px 30px 20px 30px;
}

img{
    width: 400px;
    height: 400px;
}
</style>