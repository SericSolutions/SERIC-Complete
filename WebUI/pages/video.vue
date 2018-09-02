<template>
  <v-card>
    <div class="outer1">
      <table class="inner1">
        <tr>
          <td> <img width="720px" height="480px" :src='src' class="boldoutline"> </td>
        </tr>
        <tr>
          <td>
            <v-btn success large @click.native="start()" class="buttons">
              Start
            </v-btn>
            <v-btn error large @click.native="stop()" class="buttons"> Stop </v-btn>
            <a :href="src2" download>
              <v-btn primary large class="buttons">
                Snapshot
              </v-btn>
            </a>
          </td>
        </tr>
      </table>
    </div>
  </v-card>
</template>

<script>
    import axios from 'axios';

    export default {
        beforeMount() {
            var lib = require('../init.js');

            if(lib.SN() == 'r') this.serverName = location.hostname;
            else this.serverName = lib.SN();

            this.port = lib.port();

            this.start()

        },
        beforeDestroy(){
            this.stop();
        },
        data () {
            return {
                serverName: null,
                port: null,
                src: '/wait.jpg',
                src2: null
            }
        },
        methods: {
            start()
            {
                var q = "http://" + this.serverName + ":" + this.port + "/video/1";
                console.log(q);
                axios.get(q).then(response => {
                    this.src = "http://" + this.serverName + ":" + (this.port - 1) + "/?action=stream";
                    this.src2 = "http://" + this.serverName + ":" + (this.port - 1) + "/?action=snapshot";
                });
            },
            stop()
            {
                var q = "http://" + this.serverName + ":" + this.port + "/video/0";
                console.log(q);
                axios.get(q).then(response => {
                    this.src = "/wait.jpg";
                });
            }

        },
    }
</script>


<style>
  .boldoutline
  {
    border: 5px solid black;
  }

  .outer1
  {
    width:100%;
    text-align: center;
  }
  .inner1
  {
    display: inline-block;
  }
  .buttons
  {
    font-size: 50px;
    padding-bottom:10%;
  }

</style>