<template>
  <div>
    <v-card>
        <v-layout row justify-center>
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
                <v-card>
                    <v-card-title>
                        <span class="headline">User Register</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container grid-list-md>
                            <v-layout wrap>
                                <v-flex xs12>
                                    <dropzone :options="options"
                                              v-on:vdropzone-success="onUpload"
                                              id="foo"></dropzone>
                                </v-flex>

                                <v-flex xs12>
                                    <v-text-field label="Name" required v-model="nameBox"></v-text-field>
                                </v-flex>
                            </v-layout>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn flat @click.native="dialog = false">Close</v-btn>
                        <v-btn flat @click.native="submit()"
                               :disabled="uploadFlag"
                               :loading="loading1"
                        >Submit</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-layout>

      <table class="table">
        <thead>
        <tr>
          <th class="apa">ID</th>
          <th class="apa">Name</th>
          <th class="apa">Open Door</th>
          <th class="apa">Pictures</th>
          <th class="apa">Delete</th>
          <th class="apa">Add Picture</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="i in items">
          <td class="apa">{{i.id}}</td>
          <td class="apa">{{i.personName}}</td>
          <td class="apa">
            <div style="padding-left: 40%">
              <v-switch v-model="i.OpenDoor" @click.native="toggle(i)" color="primary"></v-switch>
            </div>
          </td>
          <td class="apa">
            <app-View :n="i"></app-View>
          </td>
          <td class="apa">
            <v-btn flat
                   error
                   icon
                   @click.native = "deletePerson(i)"><v-icon large>delete</v-icon>
            </v-btn>
          </td>
          <td class="apa">
              <RUD :person="i"></RUD>
          </td>
        </tr>
        </tbody>
      </table>
    </v-card>
  </div>
</template>

<script>
    import axios from 'axios';
    import View from '~/components/ViewPeople.vue'
    import RUD from '~/components/ReinforceUploadDialog.vue'
    import Dropzone from 'nuxt-dropzone'
    import 'dropzone/dist/dropzone.css'


    export default {
        beforeMount() {
            var lib = require('../init.js');

            if(lib.SN() == 'r') this.serverName = location.hostname;
            else this.serverName = lib.SN();

            this.port = lib.port();

            axios.get('http://' + this.serverName + ':' + this.port + "/people")
                .then(response => {
                    this.items = response.data;
                })
                .catch(e => {
                    this.errors.push(e);
                })

            this.options.url = `http://${this.serverName}:${this.port}/peoplePictureUpload`
        },
        components: {
            'app-View': View,
            RUD,
            Dropzone

        },
        data () {
            return {
                serverName: null,
                port: null,
                items: [],
                options: {
                    url: "http://httpbin.org/anything",
                    maxFiles: 1,
                    dictDefaultMessage: 'Drag and drop 1 photo of new user'
                },
                nameBox: null,
                uploadFlag: true,
                fileName: null,
                dialog: false,
                loading1: false,
            }
        },
        methods: {
            findAndRemove(array, property, value)
            {
                array.forEach(function(result, index) {
                    if(result[property] === value) {
                        array.splice(index, 1);
                    }
                });
            },
            deletePerson(person)
            {
                var id = person.id;
                var request = `http://${this.serverName}:${this.port}/people/${id}`;

                if (confirm('Are you sure you want to Delete this person?')) {
                    axios.delete(request)
                        .then(response => {
                            this.findAndRemove(this.items, 'id', id);
                        })
                }
            },
            toggle(person)
            {
                var r = -1

                if(person.OpenDoor)
                    r = 1;
                else
                    r = 0;

                var request = `http://${this.serverName}:${this.port}/OpenDoor/${person.id}/${r}`
                axios.post(request)

            },
            submit()
            {
                var request =  `http://${this.serverName}:${this.port}/picture/${this.nameBox}/${this.fileName}`
                this.loading1 = true;
                axios.post(request).then(response => {
                    axios.get('http://' + this.serverName + ':' + this.port + "/people")
                        .then(response => {
                            this.items = response.data;
                            this.loading1 = false;
                            this.dialog = false;
                        })
                        .catch(e => {
                            this.errors.push(e);
                        })
                });
            },
            onUpload(file, res)
            {
                this.uploadFlag = false;
                this.fileName = file.name;
            }

        },
    }
</script>


<style>
  .apa {
    font-size: 25px !important;
    text-align: center;
    align-items: center;
  }
</style>
