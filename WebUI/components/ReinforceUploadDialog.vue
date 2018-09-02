<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" width="600px">
      <v-btn flat
             slot="activator"
             success
             icon
             @click.native = "next()"><v-icon large>add_circle</v-icon>
      </v-btn>
      <v-card>
        <dropzone :options="options"
                  align="left"
                  v-on:vdropzone-success="x"
                  id="foo"
                  @vdropzone-sending="sendingEvent">
        </dropzone>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
    import axios from 'axios';
    import Dropzone from 'nuxt-dropzone'
    import 'dropzone/dist/dropzone.css'



    export default {
        beforeMount() {
            var lib = require('../init.js');

            if(lib.SN() == 'r') this.serverName = location.hostname;
            else this.serverName = lib.SN();

            this.port = lib.port()
            this.options.url = `http://${this.serverName}:${this.port}/Reinforce`
            this.options.dictDefaultMessage = `Drop picture here to add to ${this.person.personName}'s training data`
        },
        components: {
            Dropzone
        },
        props: ['person'],

        data () {
            return {
                serverName: null,
                port: null,
                options: {
                    url: "http://httpbin.org/anything",
                    dictDefaultMessage: ''
                },
            }
        },
        methods: {
            sendingEvent(file, xhr, formData)
            {
                formData.append('id', this.person.id);
            }
        },
    }
</script>


<style>
  
</style>
