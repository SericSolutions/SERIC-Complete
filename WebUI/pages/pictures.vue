<template>
    <v-card>
        <div class="container">
            <v-snackbar
                    :timeout="timeout"
                    :top="y === 'top'"
                    :bottom="y === 'bottom'"
                    :right="x === 'right'"
                    :left="x === 'left'"
                    :multi-line="mode === 'multi-line'"
                    :vertical="mode === 'vertical'"
                    v-model="snackbar"
            >
                <v-icon success v-if="toastSuccess">done</v-icon>
                <v-icon error v-else>warning</v-icon>
                {{ text }}<v-btn flat primary @click.native="snackbar = false">Close</v-btn>
            </v-snackbar>

            <!--<div>
                <v-btn
                        error large
                        @click.native="deleteAll()"
                >
                    Delete all
                </v-btn>

                <v-btn
                        warning large
                        @click.native="takePictureWithFR()"
                        :loading="loading"
                        :disabled="loading"
                >
                    Take Picture with FR <br> (slow)
                </v-btn>

                <v-btn
                        success large
                        @click.native="takePictureWithOutFR()"
                        :loading="loading1"
                        :disabled="loading1"
                >
                    Take Picture without FR <br> (fast)
                </v-btn>

                <v-btn
                        primary large
                        @click.native="buzz()"
                >
                    Ring Bell
                </v-btn>
            </div>
            -->
            <table class="table">
                <thead>
                <tr>
                    <th class="apa">Date</th>
                    <th class="apa">Time</th>
                    <th class="apa">Person</th>
                    <!--<th class="apa">Name</th>-->
                    <th class="apa">
                        <v-btn flat @click.native="likeFilter()" style="font: inherit;
                        color: inherit;
                        text-transform: none"
                        :primary = "filterd">
                            Favorite
                        </v-btn>
                    </th>
                    <th class="apa">Link</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="i in items">
                    <!--<td class="apa">{{i.pictureName}}</td>-->
                    <td class="apa">{{epochToDate(i.date)}}</td>
                    <td class="apa">{{epochToTime(i.date)}}</td>
                    <td class="apa">{{i.personName}}</td>
                    <td style="font-size: 35px; text-align: center;" @click="fav(i)">
                        <v-btn flat icon large :primary="i.fav == 1 ? true: false">
                            <v-icon large>thumb_up</v-icon>
                        </v-btn>

                    </td>
                    <td class="apa">
                        <app-View :item="i"></app-View>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
        <v-card>
            <v-speed-dial
                    absolute top right
                    v-model="fab"
                    direction = "left"
            >
                <v-btn
                        fab icon dark flat
                        slot="activator"
                        class = "blue darken-2"
                        v-model="fab"
                        :loading="loading"
                        :disabled="loading"
                >
                    <v-icon>add</v-icon>
                    <v-icon>close</v-icon>
                </v-btn>

                <v-btn
                            fab dark
                            class="red"
                            @click.native="deleteAll()"

                >
                            <v-icon>delete</v-icon>
                    </v-btn>

                <v-btn
                        warning fab dark
                        @click.native="takePictureWithFR()"
                >
                    <v-icon>camera_front</v-icon>
                </v-btn>

                <v-btn
                        success fab dark
                        @click.native="takePictureWithOutFR()"
                >
                    <v-icon>photo_camera</v-icon>
                </v-btn>

                <v-btn
                        fab dark primary
                        @click.native="buzz()"
                >
                    <v-icon>volume_up</v-icon>
                </v-btn>

            </v-speed-dial>
        </v-card>
    </v-card>
</template>

<script>
    import View from '~/components/View.vue';
    import axios from 'axios';


    export default {
        beforeMount() {
            var lib = require('../init.js');

            if(lib.SN() == 'r') this.serverName = location.hostname;
            else this.serverName = lib.SN();

            this.port = lib.port()
            axios.get('http://' + this.serverName + ':' + this.port)
                .then(response => {
                    // JSON responses are automatically parsed.
                    this.items = response.data;
                    //console.log(response.data);
                })
                .catch(e => {
                    this.errors.push(e);
                })
        },
        components: {
                'app-View': View
            },
        data () {
            return {
                serverName: null,
                port: null,
                items: [],
                loader : null,
                loading : false,
                filterd : false,
                snackbar: false,
                y: 'top',
                x: null,
                mode: '',
                timeout: 6000,
                text: '',
                toastSuccess: null,
                oldItems: null,
                fab: false,
            }
        },
        methods: {
            likeFilter(){
                if(this.oldItems == null)
                {
                    this.oldItems = this.items;
                    this.items = this.items.filter(item => item.fav == 1);
                    this.filterd = true
                }
                else {
                    this.items = this.oldItems;
                    this.oldItems = null;
                    this.filterd = false
                }

            },
            epochToDate: function(UNIX_timestamp) {
                var a = new Date(UNIX_timestamp * 1000);
                return a.toDateString();
            },
            epochToTime: function(UNIX_timestamp) {
                var date = new Date(UNIX_timestamp * 1000);

                var hours = date.getHours();
                var minutes = date.getMinutes();
                var ampm = hours >= 12 ? 'PM' : 'AM';
                hours = hours % 12;
                hours = hours ? hours : 12; // the hour '0' should be '12'
                minutes = minutes < 10 ? '0' + minutes : minutes;
                var strTime = hours + ':' + minutes + ' ' + ampm;
                return strTime;
            },

                fav(x)
            {
                x.fav = !x.fav;

                var r = -1

                if(x.fav)
                    r = 1;
                else
                    r = 0;

                var p = 'http://' + this.serverName + ':' + this.port +'/fav/' + x.pictureName + '/' + r


                axios.post(p)
                    .then(response => {
                    })
                    .catch(e => {
                    })


            },
            takePictureWithFR()
            {
                this.loading = true;

                var p = 'http://' + this.serverName + ':' + this.port +'/picture/1';

                axios.get(p)
                    .then(response => {
                        // JSON responses are automatically parsed.
                        if(this.items.length < 1)
                            this.items.push(response.data[0]);
                        else
                            this.items.unshift(response.data[0]);
                        //console.log(response.data);
                        //console.log(this.items);
                        this.loading = false;
                        this.toast("Took a picture With FR",true);

                    })
                    .catch(e => {
                        this.errors.push(e)
                        this.loading = false;
                    })
            },
            takePictureWithOutFR()
            {
                this.loading = true;

                var p = 'http://' + this.serverName + ':' + this.port +'/picture/0';

                axios.get(p)
                    .then(response => {
                        // JSON responses are automatically parsed.
                        if(this.items.length < 1)
                            this.items.push(response.data[0]);
                        else
                            this.items.unshift(response.data[0]);
                        //console.log(response.data);
                        //console.log(this.items);
                        this.loading = false;
                        this.toast("Took a picture without FR",true)

                    })
                    .catch(e => {
                        this.errors.push(e)
                        this.loading = false;
                    })
            },
            deleteAll()
            {
                var p = 'http://' + this.serverName + ':' + this.port + '/del';

                if (confirm('Are you sure you want to Delete ALL pictures?')) {
                    axios.delete(p)
                        .then(response => {
                            this.items = [];
                            this.toast("Deleted All", true)
                        })
                }
            },
            buzz()
            {
                var p = 'http://' + this.serverName + ':' + this.port + '/buzz';

                axios.get(p).then(response => {
                    this.toast("Bell Activated", true)
                });
            },
            toast(text, success)
            {
                this.snackbar = true;
                this.text = text;
                this.toastSuccess = success;
            }
        },
    }
</script>


<style>
    .apa {
        font-size: 25px !important;
        text-align: center;
    }
</style>