<template>
  <div class="hello">

    <h2>{{ msg }}</h2>

    <input type="file" @change="onFileSelected" class="custom-file-upload">
    <br/>

    <button class="btn btn-primary font-weight-bold" @click="onUpload">Upload</button>

    <div class="container">
      <!--<img :src="imgFile" v-if="imgFile" style="max-width: 100%;" />-->
      <div id="displayImg">
      </div>

      <div v-if="responseData">
        <div class="font-weight-bold">
          Prediction: {{ responseData.predictedTagName}}
        </div>
        <div class="font-weight-bold"> 
          Probability: {{ (this.predictProbability * 100).toFixed(3)}} %
        </div>
      </div>
      <div v-else class="font-weight-bold">
        Please Upload an Image
      </div>

      
      <!-- import from results later [Scrapped, but file there for future self-reference] -->
      <!--
      <div v-if='this.responseData !==null && this.selectedFile !== null'>
        <Results resData = 'responseData'  selectedImage = 'selectedFile'/> 
      </div>
      -->
    </div>

  </div>
</template>

<script>
//Axios to allow ajax requests inside the script
//import axios from 'axios';
import Results from '@/components/Results.vue'

export default {
  name: 'UploadImg',
  components: {
    Results
  },
  props: {
    msg: String
  },
  data () {
    return {
      selectedFile: null,
      imgFile: null,
      responseData: null,
      predictProbability: 0
    }
  },
  methods: {
    onFileSelected(event) {
      console.log(event)
      this.selectedFile = event.target.files[0]
    },
    async onUpload() {
      /*==============================================================
      **formdata sent file as binary and url search params sent data as object file**
      Creation of form data with the selected file from the input 
      (sending this will send the file as a binary object but as part of the multipart/formdata)
      ==============================================================*//*
      const fd = new FormData();
      fd.append('image', this.selectedFile, this.selectedFile.name)

      //Sending the form data as part of Params (it will be sent to the api as an object)
      const data = new URLSearchParams(fd)
      */

      /*==============================================================
      Working version:
      Create a blob from the uploaded image and send as a file
      ==============================================================*/
      const myBlob = new Blob([this.selectedFile], {type: this.selectedFile.type})
      const file = new File([myBlob], this.selectedFile.name)
      const AzureAppFunc= 'http://localhost:7071/api/classify'

      //post request
      const res = await fetch (AzureAppFunc, {
        method: 'POST',
        body: file,
        redirect: 'follow'
      })

      //Response was in readable stream, so the data has to be formatted to json
      //A promise will be returned. In order to access the JSON, need await the response
      this.responseData = await res.json()

      /*
      Condition to retrieve the probability percentage as per the prediction tag name
      Object format:
      {
        created (Date)
        img (Data for base64 conversion)
        predictedTagName (Result from the prediction)
        prediction array (2 tags => 2 rows in array. Each row have 2 columns)
          => probability //e.g. responseData.prediction[1].probability
          => tagName     //e.g. responseData.prediction[1].tagName
      }
      */
      let predictedResult = this.responseData.predictedTagName.toLowerCase();
      this.responseData.prediction.forEach(prediction => {
        if (prediction.tagName.toLowerCase() === predictedResult)
        {
          this.predictProbability = prediction.probability;
          return; //End the loop
        }
      })
    
      /*==============================================================
      This section is to load the uploaded image onto the webpage 
      ==============================================================*/
      /*
      this.imgFile = new Image()
      var reader = new FileReader()
      //when the reader is loaded, the imgFile is assigned the reading/event result(image is read onto the web page)
      reader.onload = (e) => {
        this.imgFile = e.target.result
      }
      //Read the uploaded file form the input as URL using the reader.
      reader.readAsDataURL(this.selectedFile) //console log return this as undefined
      */


      /*==============================================================
      This section is to convert the image from Base64 received from API 
      to an image on frontend without displaying the uploaded image from 
      the direct source
      ==============================================================*/
      this.imgFile = new Image()
      this.imgFile.src = "data:image/png;base64," + this.responseData.img
      this.imgFile.style.width = '100%'

      /*
      Condition to check if there is any child in the div
      If there is none, appendchild, else replacechild otherwise 
      multiple images will appear. 
      */
      const element = document.getElementById("displayImg")
      if (element.hasChildNodes())
      {
        element.replaceChild(this.imgFile, element.childNodes[0])
      }
      else {
        element.appendChild(this.imgFile)
      }
      
      console.log(this.responseData) //Returns a proper JSON object
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.custom-file-upload {
    border: 1px solid steelblue;
    display: inline-block;
    padding: 15px 10%; /* vertical horizontal */
    margin: 10px;
    cursor: pointer;
}

</style>
