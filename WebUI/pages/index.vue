<template>
  <v-card style="padding-bottom: 5%">
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-xs-center">
        <h1 class="cts">S.E.R.I.C</h1>
        <h4 class="cts">Smart Embedded Redundant IoT Camera</h4>
      </div>
      <v-card>
        <v-card-text v-if="active" style="background-color: green; text-align: center">
          <h1 style="color: white">ONLINE</h1>
        </v-card-text>
        <v-card-text v-else style="background-color: red; text-align: center">
          <h1 style="color: white">OFFLINE</h1>
        </v-card-text>
      </v-card>
    </v-flex>
    <br>
    <hr>
    <div v-if="active">
      <v-btn flat to="/pictures" class="pad"> <h3 class="cts">Pictures</h3></v-btn>
      <v-btn flat to="/video" class="pad"> <h3 class="cts">Live Video</h3></v-btn>
      <v-btn flat to="/people" class="pad"> <h3 class="cts">People</h3></v-btn>
      <v-btn flat to="/autoattendant" class="pad"> <h3 class="cts">Attendant</h3></v-btn>
    </div>
  </v-layout>
  </v-card>
</template>


<script>
    import axios from 'axios';

    export default {
        beforeMount() {
            var lib = require('../init.js');

            if(lib.SN() == 'r') this.serverName = location.hostname;
            else this.serverName = lib.SN();

            this.port = lib.port()

            axios.post('http://' + this.serverName + ':' + this.port)
                .then(response => {
                    console.log(response.data.done)
                    if(response.data.done == "yes")
                        this.active = true;
                })
        },
        data (){
            return {
                active: false,
                serverName: null,
                port: null
            }
        }

    }
</script>

<style>
  .cts {
    font-family: 'Courier 10 Pitch';
    color: black;
  }
  .pad
  {
    border: 1px solid;
    padding-bottom:3%;
    padding-top:5%;
  }

</style>
