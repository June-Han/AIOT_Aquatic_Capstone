<template>
  <div width="100%" height="100%">
    <h1>{{msg}}</h1>
    <h2> {{title_msg}}</h2>

    <svg id="globe" :width="svg_width" :height="svg_height" fill="url(#oceanGradient)">
      <defs>
          <linearGradient id = "oceanGradient" x1 = "0%" y1 ="0%" x2="100%" y2="0%">
              <stop offset="0%" style="stop-color:rgb(0,0,27); stop-opacity:1"/>
              <stop offset="100%" style="stop-color:rgb(51,122,183); stop-opacity:1"/>
          </linearGradient>
      </defs>
      <g>
        <path v-for="(data, index) in paths" :key="index" :d="data.path" :id='data.id' stroke="#fff" fill="url(#oceanGradient)" stroke-width="1.0" 
            @mouseenter="(event) => {hovered = data; mouseOverHover(event);}"  
            @mouseleave="() => {hovered = null;}"/>
        
        <circle v-for="(item, index) in points" :key="index" r="7" :cx="item.x" :cy="item.y" :fill="pointerColor(item.severity)" stroke="black"
          @mouseenter="() => {pointerHover = item;}"
          @mouseleave="() => {pointerHover = null;}"
          @dblclick="() => {showBleachInfo = true; pointDblClick = item; }"/>
      </g>
    </svg>
    <!--Hover for the countries-->
    <div v-if="hovered" class="hovered" 
      :style = '{
        top: `${hovered.y + 20}px`, //x-axis for drawing
        left: `${hovered.x}px`, //y-axis for drawing
      }'>
        <strong>Name:</strong> {{hovered.data.name}} <br />
    </div>
    <!--Hover for the bleaching points-->
    <div id="pointHover" v-if="pointerHover" class="hovered"
    :style = '{
        top: `${pointerHover.y + 20}px`,
        left: `${pointerHover.x}px`,
      }'>
        <strong>Country:</strong> {{pointerHover.country}} <br />
        <strong>Location:</strong> {{pointerHover.location}} <br />
        <strong>Bleaching Severity:</strong> {{pointerHover.severity}} <br />

        <div style="text-align:right;">
          <small>double click for info</small>
        </div>
    </div>
    <!--Show bleaching info section on double click and double click on info section to close-->
    <div v-if="pointDblClick" v-show="showBleachInfo" class="circleDblClick"
    @dblclick="showBleachInfo = false"
    :style ='{
      top: `20%`,
      left: `80%`,
      height: `100%`
    }'>
      <!-- aligning for scrolls in case of overflow -->
      <div :style="{
        'text-align': `left`,
        margin: `10px`,
        height: `${this.svg_height-150}px`,
        'overflow-x': `auto`,
        'overflow-y': `auto`,
        display: `block`
      }">
          <!--Header for information section-->
          <strong style="font-size: 30px;">Information</strong> <br/> 
          <small>Date: {{this.pointDblClick.date}} </small> <br/>
          <!--Information Section-->
          <table style="width:100%;">
            <tr><td><strong>Bleaching Severity: </strong></td> 
                <td>{{this.pointDblClick.severity}} 
                    <div class="square" :style="{'background-color': pointerColor(this.pointDblClick.severity)}"></div>
                </td>
            </tr>
            <tr><td><strong>Country: </strong></td> <td>{{this.pointDblClick.country}}</td></tr>
            <tr><td><strong>Location: </strong></td> <td>{{this.pointDblClick.location}}</td></tr>
            <tr><td><strong>Coordinates: </strong></td> <td>{{this.pointDblClick.lat}}, {{this.pointDblClick.lon}}</td></tr>
            <tr><td><strong>Mortality: </strong></td> <td>{{this.pointDblClick.mortality}}</td></tr>
            <tr><td><strong>Recovery: </strong></td> <td>{{this.pointDblClick.recovery}}</td></tr>
            <tr><td><strong>Coral Family: </strong></td> <td>{{this.pointDblClick.coralFamily}}</td></tr>
            <tr><td><strong>Coral Species: </strong></td> <td>{{this.pointDblClick.coralSpecies}}</td></tr>
            <tr><td><strong>Survey Type: </strong></td> <td>{{this.pointDblClick.survey_type}}</td></tr>
            <tr><td><strong>Water Temperature: </strong></td> <td>{{this.pointDblClick.water_temp}}</td></tr>
            <tr><td><strong>Remarks: </strong></td> <td>{{this.pointDblClick.remarks}}</td></tr>
          </table>
          <div style="text-align: right; margin: 20px;">
            <small>Source:  {{this.pointDblClick.source}} </small><br/>
          </div>
      </div>
    </div>

  </div>
</template>

<script>
import * as d3 from "d3";
import * as d3Collection from 'd3-collection';

export default ({
  name: "coralGlobe",
  props: {
    msg: String,
  },
  data() {
    return {
        title_msg: "Global Coral Bleaching Data Visualization",
        svg_height: 1000,
        svg_width: 1500,
        paths: [],
        points: [],
        hovered: null,
        pointerHover: null,
        pointDblClick: null,
        showBleachInfo:false
    };
  },
  created() {
    this.fetchAndCreate();
  },
  methods: {
    //Fetch and manipulate data for Map creation
    async fetchAndCreate() {
        Promise.all([d3.json("./CoralBleaching.json"), d3.json("./world.geojson")]).then(([coralData, mapData]) => {
            let topoMapData = mapData.features;

            let projection = d3.geoMercator().fitSize([this.svg_width, this.svg_height], mapData);
            var geopath = d3.geoPath().projection(projection);


            //Create paths to draw the map
            this.paths = topoMapData.map(feature => {
                //Map and projection
                return {
                  id: feature.id,
                  name: feature.properties.name,
                  path: geopath(feature)
                }
            })
            
            //Filter data for visualisation
            coralData.forEach(feature => {
              //Collect the points for the visualization (Javascript has latitude and longitude in opposite ways)
              let pointProjection = projection([feature.lon, feature.lat]);
              if (isNaN(pointProjection[0]) != true && isNaN(pointProjection[1]) != true) {
                this.points.push(
                  {
                    id: feature.id,
                    severity: feature.bleaching_severity.toLowerCase(),
                    x: pointProjection[0],
                    y: pointProjection[1],
                    lat: feature.lat,
                    lon: feature.lon,
                    country: feature.country,
                    location: feature.location,
                    date: this.toMonthName(feature.month) + " " + feature.year,
                    coralFamily: feature.coral_family,
                    coralSpecies:feature.coral_species,
                    mortality: feature.mortality,
                    recovery: feature.recovery,
                    survey_type: feature.survey_type,
                    water_temp: feature.water_temperature,
                    remarks: feature.remarks,
                    source: feature.source
                  }
                )
              }
              else {
                console.log(feature);
              } 
            })
        })

    },
    //Convert digits to month strings
    toMonthName(num){
      const date = new Date();
      date.setMonth(num - 1);
      return date.toLocaleString('en-US', {
        month: 'long',
      });
    },
    //Mouseover for the map
    mouseOverHover(event) {
      const currentData = this.hovered;
      //Add in the x and y coordinates for current data
      this.hovered = {
        x: event.x,
        y: event.y,
        data: currentData
      }
    },
    //Return appropriate color based on bleaching severity
    pointerColor(severity) {
      let colorScale = d3.scaleOrdinal()
                        .domain(["severity unknown","no bleaching","low","medium", "high"])
                        .range(["lightgray", "green", "yellow", "orange", "red" ])
      
      return colorScale(severity);
    },
  },
})

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hovered {
  position: absolute;
  padding: 5px 10px;
  background-color: #fff;
  box-shadow: 0 0 5px #cfcfcf;
  transform: translate(-50%);
  pointer-events: none;
  line-height: 1.6;
  width: 240px;
}

.circleDblClick {
  position: absolute;
  padding: 5px 10px;
  background-color: #fff;
  box-shadow: 0 0 5px #cfcfcf;
  float:right;
  line-height: 1.6;
  width: 30%;
}

path:hover {
  stroke-width: 2px;
  fill: rgb(214, 214, 214);
}

circle:hover {
  stroke-width: 4px;
  fill: rgb(99, 62, 200);
}

#pointHover {
  text-align: left;
}
.square {
  height: 50px;
  width: 50px;
  outline: 1px solid black;
}

</style>