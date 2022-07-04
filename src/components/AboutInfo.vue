<template>
    <div style="padding: 10px 0px 10px 100px">
        <h2 style="text-align: left; margin: auto">{{msg}}</h2>
        <div id="description">
            This project is an AIOT solution focuses not only on increasing awareness of coral bleaching worldwide,
            it also focuses on the preservation of the coral reefs, the cornerstone of marine ecosystems. <br/><br/>
            
            The purpose is for early detection of stressors for coral reefs before coral bleaching phenomenon. It is 
            also for detection of signs of coral bleaching for early mitigation through the use of machine learning and 
            cloud computing. The project also provides data visualization for condition of coral reefs worldwide.
            This would aid in the fast release of results which is an important outcome for policymakers
            who requires reliable data for decision making and also for scientists who need data from widespread area to 
            understand the impact of climate change on coral reefs. <br/><br/>

            This project is created as a final year project for B.Sc(Hons) Computing Science at 
            SIT(Singapore Institute of Technology) and UOG(University of Glasgow) Joint Degree Programme. <br/><br/>
        </div>
        <h2 style="text-align: left; margin: auto">United Nations Sustainable Development Goals: </h2>
        <div id="UNGoals">
            This project mainly aims to aid the following UN Sustainable Development Goals:
            <ul>
                <li>Goal 2: Zero Hunger</li>
                <li>Goal 6: Clean Water and Sanitization</li>
                <li>Goal 14: Life Below Water</li>
            </ul>
        </div>
    </div>    
</template>

<script>

export default {
  name: 'projectInfo',
  props: {
    msg: String,
  },
}
</script>

<style scoped>
#description {
    text-align: left;
    padding: 20px;
    margin-right: 120px;
}

#UNGoals{
    text-align: left;
    padding: 20px;
    margin-right: 120px;
}
</style>