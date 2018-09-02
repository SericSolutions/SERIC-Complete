<template>
  <div>

  </div>
</template>

<script>
    import axios from 'axios';


    export default {
        beforeMount() {
            var lib = require('../init.js');

            if(lib.SN() == 'r') this.serverName = location.hostname;
            else this.serverName = lib.SN();

            this.port = lib.port()
        },
        data () {
            return {
                serverName: null,
                port: null
            }
        },
        methods: {

        },
    }
</script>


<style>
  
</style>
