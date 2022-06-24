<template>
    <div>
        <img :src="imgData" v-if="displayImg()" style="max-width: 100%;" />
        <img v-else/>
        <div v-if="responseData">
        <div class="font-weight-bold">
            Prediction: {{ resData.predictedTagName}}
        </div>
        <div class="font-weight-bold"> 
            Probability: {{ (resData.prediction[0].probability * 100).toFixed(3)}} %
        </div>
        </div>
        <div v-else class="font-weight-bold">
            Please Upload an Image
        </div>
    </div>
</template>

<script>

export default({
    name: 'Results',
    props: {
        imgData: null,
        resData: String
    },
    data () {
        return {
            selectedImage: null
        }
    },
    computed: {
        displayImg() {
            console.log(typeof selectedImage)
            this.imgData = new Image()
            var reader = new FileReader()

            //when the reader is loaded, the imgFile is assigned the reading/event result(image is read onto the web page)
            reader.onload = (e) => {
                this.imgData = e.target.result
            }

            //Read the uploaded file form the input as URL using the reader.
            reader.readAsDataURL(this.selectedImage) //console log return this as undefined
        }
    }
})
</script>

<style scoped>

</style>
