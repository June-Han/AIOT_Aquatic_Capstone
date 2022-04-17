<template>
  <div class="hello">

    <h1>{{ msg }}</h1>

    <input type = "file" @change="onFileSelected">

    <button @click="onUpload">Upload</button>

    <div class="container">
      <img :src="imgFile" v-if="imgFile" style="max-width: 100%;" />
      <p></p>
      <!-- import from results later -->
    </div>

  </div>
</template>

<script>
//Axios to allow ajax requests inside the script
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data () {
    return {
      selectedFile: null,
      responseData: null,
      imgFile: null
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
      ==============================================================*/
      const fd = new FormData();
      fd.append('image', this.selectedFile, this.selectedFile.name)

      //Sending the form data as part of Params (it will be sent to the api as an object)
      const data = new URLSearchParams(fd)

      /*==============================================================
      Working version:
      Create a blob from the uploaded image and send as a file
      ==============================================================*/
      const myBlob = new Blob([this.selectedFile], {type: this.selectedFile.type})
      const file = new File([myBlob], this.selectedFile.name)

      //post request
      const res = await fetch ('http://localhost:7071/api/classify', {
        method: 'POST',
        body: file,
        redirect: 'follow'
      })

      //Response was in readable stream, so the data has to be formatted to json
      //A promise will be returned. In order to access the JSON, need await the response
      this.responseData = await res.json()

      /*==============================================================
      This section is to load the uploaded image onto the webpage 
      ==============================================================*/
      this.imgFile = new Image()
      var reader = new FileReader()
      //when the reader is loaded, the imgFile is assigned the reading/event result(image is read onto the web page)
      reader.onload = (e) => {
        this.imgFile = e.target.result
      }
      //Read the uploaded file form the input as URL using the reader.
      reader.readAsDataURL(this.selectedFile) //console log return this as undefined
      
      console.log(this.responseData) //Returns a proper JSON object
      console.log(this.responseData.predictedTagName) //returns 'With Mask'
      console.log(this.responseData.prediction[0]) //Returns a JSON with probability and Tag name
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
</style>
