<template>
    <v-container grid-list-md text-xs-center >

        <v-layout row wrap>
            <v-card>
                <div>
                    <v-flex>
                        <img :src='src' class='boldoutline'>
                    </v-flex>
                </div>
            </v-card>

            <v-flex>
                <v-card class='CardBox' raised>
                    <v-card-media src='/asad.jpg' height='400px'>
                    </v-card-media>
                    <v-card-title primary-title>
                        <div>
                            <h1 class='headline'>Today, 9:00 PM</h1>
                        </div>
                    </v-card-title>
                </v-card>
            </v-flex>

        </v-layout>

        <v-layout row wrap>
                <v-flex xs12 sm6 md3 v-for='i in 4'>
                    <v-card class='CardBox1' raised >
                        <v-card-title primary-title>
                            <div>
                                <v-icon xLarge class='center'>settings</v-icon>
                                <h3 class='headline mb-1 center'>Setting #{{((5)+ i) - 5}}</h3>
                                <div>Asad came home possessed by a demon, do i let him in? </div>
                            </div>
                        </v-card-title>
                        <div class='center'>
                            <v-card-actions>
                                <v-btn flat color='orange'>Yes</v-btn>
                                <v-btn flat color='orange'>Hell No</v-btn>
                            </v-card-actions>
                            <v-card-actions v-if='j === 2'>
                                <v-switch></v-switch>
                            </v-card-actions>
                        </div>
                    </v-card>
                </v-flex>
            </v-layout>
    </v-container>
</template>


<script>
  import axios from 'axios'

  export default {
    beforeMount () {
      this.serverName = 'asadpi.local'
      this.port = 8081
      this.start()
    },
    beforeDestroy () {
      this.stop()
    },
    data () {
      return {
        serverName: null,
        port: null,
        src: '',
        src2: null
      }
    },
    methods: {
      start () {
        setTimeout(function () {
        }, 5000)
        var q = 'http://' + this.serverName + ':' + this.port + '/video/1'
        console.log(q)
        console.log(q)
        axios.get(q).then(response => {
          this.src = 'http://' + this.serverName + ':' + (this.port - 1) + '/?action=stream'
          this.src2 = 'http://' + this.serverName + ':' + (this.port - 1) + '/?action=snapshot'
        })
      },
      stop () {
        var q = 'http://' + this.serverName + ':' + this.port + '/video/0'
        console.log(q)
        axios.get(q).then(response => {
          this.src = '/wait.jpg'
        })
      }
    }
  }
</script>

<style>
    .CardBox1{
        margin: 0px;
    }
    .center{
        display: flex;
        justify-content: center;
    }
</style>