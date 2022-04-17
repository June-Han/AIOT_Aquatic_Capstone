<template>
    <div>
        <img :src="url" v-if="url" style="max-width: 100%;" />
    </div>
</template>

<script>

export default({
    name: 'Results',
    props: {
        
    }
})
</script>

<style scoped>

</style>
