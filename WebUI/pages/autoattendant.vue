<template>
  <div>
      <v-card style="margin-top: 2%">
          <table class="table">
              <thead>
              <tr>
                  <th class="apa">No</th>
                  <th class="apa">Name</th>
                  <th class="apa">Playbar</th>
                  <th class="apa">Active</th>
                  <th class="apa">Delete</th>
                  <th class="apa">Recipent</th>
                  <th class="apa"></th>

              </tr>
              </thead>
              <tbody>
              <tr v-for="i in items">
                  <td class="apa">{{i.No}}</td>
                  <td class="apa"> {{i.Name}} </td>
                  <td class="apa">
                      <audio controls>
                          <source :src="'http://'+ serverName + '/data/audio/' + i.src" type="audio/mp3">
                      </audio>
                  </td>
                  <td class="apa">
                      <div style="padding-left: 40%">
                        <v-switch v-model="i.active" @click.native="toggle(i)" color="primary"></v-switch>
                      </div>
                  </td>
                  <td class="apa">
                      <v-btn error @click.native="del(i)">
                          Delete
                      </v-btn>
                  </td>
                  <td class="apa">{{i.personName}}</td>
                  <td class="apa">
                      <v-icon v-if="doup(i)" error>warning</v-icon>
                  </td>
              </tr>
              </tbody>
          </table>

          <v-dialog v-model="dialog" width="500px">
              <v-btn absolute
                     dark
                     fab
                     bottom
                     right
                     style="right: 0.5%;"
                     slot="activator"
                     success><v-icon large>add</v-icon>
              </v-btn>
              <v-card class="outer">
                  <v-container grid-list-md>
                      <dropzone :options="options"
                                align="left"
                                v-on:vdropzone-success="x"
                                id="foo">
                      </dropzone>
                      &#8203
                      <v-form>

                          <v-text-field
                                  label="File Name"
                                  v-model="fileName"
                                  :disabled="true"
                                  required
                          ></v-text-field>


                          <v-text-field
                                  label="Clip Name"
                                  v-model="clipName"
                                  required
                          ></v-text-field>

                          <v-select
                                  v-bind:items="p"
                                  v-model="person"
                                  label="for"
                                  single-line
                                  bottom
                                  required
                          ></v-select>
                          <v-btn
                                  @click.native="submit()"
                                  primary
                                  large
                          >
                              submit
                          </v-btn>
                      </v-form>
                  </v-container>
              </v-card>
          </v-dialog>
      </v-card>
  </div>
</template>

<script>
    import axios from 'axios';
    import Dropzone from 'nuxt-dropzone'
    import 'dropzone/dist/dropzone.css'

    export default {
        components: {
            Dropzone
        },
        beforeMount() {
            var lib = require('../init.js');

            if(lib.SN() == 'r') this.serverName = location.hostname;
            else this.serverName = lib.SN();

            this.port = lib.port()

            axios.get('http://' + this.serverName + ':' + this.port + '/audio')
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.items = response.data;
                    //console.log(response.data);
                })

            axios.get('http://' + this.serverName + ':' + this.port + '/peopleNames')
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.p = response.data;
                    //console.log(response.data);
                })

            this.options.url = 'http://' + this.serverName + ':' + this.port + '/upload'
        },
        data () {
            return {
                serverName: null,
                port: null,
                options: {
                    url: "http://httpbin.org/anything",
                    maxFiles: 1
                },
                items: [],
                p: [],
                fileName: null,
                person: null,
                clipName: null,
                dialog: false

            }
        },
        methods: {
            toggle(i)
            {
                var r = -1

                if(i.active)
                    r = 1;
                else
                    r = 0;

                var p = 'http://' + this.serverName + ':' + this.port +'/audio/' + i.No + '/' + r
                console.log(p)

                axios.post(p).then(response => {});
            },
            x(file, res)
            {
                console.log(file.name);
                this.fileName = file.name;
            },
            submit()
            {
                var q = ''
                if(this.fileName == null)
                    q+="No file\n";

                if(this.clipName == null)
                    q+="No clip name\n";

                if(this.person == null)
                    q+="No person selected\n"

                if(q == '')
                {
                    var p = 'http://' + this.serverName + ':' + this.port +'/audio/' + this.fileName + '/' + this.clipName + '/' + this.person.id;

                    console.log(p);

                    axios.post(p)
                        .then(response => {
                            axios.get('http://' + this.serverName + ':' + this.port + '/audio')
                                .then(response => {
                                    this.items = response.data;
                                    this.dialog = false;
                                })
                        })
                        .catch(e => {
                        })
                }
                else
                {
                    alert(q)
                }
            },
            del(i)
            {
                var p = 'http://' + this.serverName + ':' + this.port + '/audio/' + i.No + '/' +i.src;
                axios.delete(p).then(response => {
                    axios.get('http://' + this.serverName + ':' + this.port + '/audio')
                        .then(response => {
                            this.items = response.data;
                        })
                })
            },
            doup(i)
            {
                var name = i.personName
                var count = 0;

                for(var i = 0; i<this.items.length; i++)
                {
                    if(this.items[i].personName == name && this.items[i].active)
                    {
                        count++;
                    }
                }

                if(count == 1)
                    return false;
                else if(count > 1)
                    return true;
            }

        },
    }
</script>

<style>
    .outer {
        width: 100%;
        text-align: center;
    }

    #forum {
        width: 30%;
        display: inline-block;
        padding: 2%;

    }
    #dz {
        width: 30%;
        display: inline-block;
        padding: 0%;
        position: relative;
        bottom: 50px;
    }
    .apa {
        font-size: 25px !important;
        text-align: center;
    }
</style>