<template>
    <v-layout row justify-center>
        <v-dialog v-model="dialog" width="800px">
            <v-btn icon large
                   slot="activator"
                   @click.native="reload()"
            >
                <v-icon large>
                    open_in_new
                </v-icon>
            </v-btn>

            <v-card>
                <v-card-title>
                    <div class="outer">
                        <div class="inner" style="font-size: 2pc">
                            {{name}}
                        </div>
                    </div>
                </v-card-title>

                <v-card-media>
                    <img :src="src" height="100%" width="100%"/>
                </v-card-media>

                <v-card-actions>
                    <div class="outer">

                        <v-btn flat icon
                               :disabled="BD"
                               class = "inner grey lighten-1"
                               @click.native = "prev()">
                            <v-icon large>keyboard_arrow_left</v-icon>
                        </v-btn>

                        <v-btn dark icon
                               @click.native="dialog = false"
                               class = "inner grey darken-3"
                        >
                            <v-icon large> close </v-icon>
                        </v-btn>


                        <a :href="src" download>
                            <v-btn primary dark icon
                                   @click.native="dialog = false"
                                   class = "inner"
                            >
                                <v-icon large>file_download</v-icon>
                            </v-btn>
                        </a>

                        <v-btn error dark icon
                               class = "inner"
                               @click.native = "del()"
                        >
                            <v-icon large>delete_forever</v-icon>
                        </v-btn>

                        <v-btn flat icon
                               :disabled="FD"
                               class = "inner grey lighten-1"
                               @click.native = "next()">
                            <v-icon large>keyboard_arrow_right</v-icon>
                        </v-btn>

                    </div>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </v-layout>
</template>

<script>
    import axios from 'axios';
    export default {
        props: ['n'],
        methods: {
            findAndRemove(array, property, value)
            {
                array.forEach(function(result, index) {
                    if(result[property] === value) {
                        array.splice(index, 1);
                    }
                });
            },
            del()
            {
                var id = this.items[this.i].id;
                var request = `http://${this.server}:${this.port}/peoplePhotos/${id}`;

                if (confirm('Are you sure you want to Delete this picture?')) {
                    axios.delete(request)
                        .then(response => {

                            this.findAndRemove(this.items, 'id', id);
                            this.size--;
                            this.dialog = false
                        })
                }
            },
            next()
            {
                this.i++;
                var next = this.i;
                var id = this.items[next].id;

                this.src = `http://${this.server}/data/enroll/${id}.jpg`;
                this.name = `${this.i+1}/${this.size}`

                this.validate(next)
            },
            prev()
            {
                this.i--;
                var next = this.i;
                var id = this.items[next].id;

                this.src = `http://${this.server}/data/enroll/${id}.jpg`;
                this.name = `${this.i+1}/${this.size}`

                this.validate(next)
            },
            reload()
            {
                this.i = 0;
                var id = this.items[this.i].id;
                this.src = `http://${this.server}/data/enroll/${id}.jpg`;
                this.name = `${this.i+1}/${this.size}`

                this.validate(this.$parent.items.indexOf(this.n));

            },
            validate(index) {
                var size = this.items.length - 1;
                var arr = this.items;
                var i = this.items[this.i];


                if (arr[0] == i)
                    this.BD = true;
                else
                    this.BD = false;

                if (arr[size] == i)
                    this.FD = true;
                else
                    this.FD = false;
            }

        },
        data (){
            return {
                dialog: false,
                name: '',
                src: '',
                FD: false,
                BD: false,
                i: 0,
                size: 0,
                items: {},
                server: '',
                port: 0,
            }
        },
        beforeMount()
        {
            this.server = this.$parent.serverName;
            var server = this.server;
            this.port = this.$parent.port;
            var port = this.$parent.port;
            var id = this.n.id;
            var request = `http://${server}:${port}/peoplePhotos/${id}`

            axios.get(request)
                .then(response => {
                    this.items = response.data;
                    this.size = this.items.length
                    id = this.items[0].id

                    this.name = `${this.i+1}/${this.size}`;
                    this.src = `http://${server}/data/enroll/${id}.jpg`;
                    this.validate(this.$parent.items.indexOf(this.n));
                })
                .catch(e => {
                    this.errors.push(e);
                })


        }

    }
</script>

<style>
    .outer
    {
        width:100%;
        text-align: center;
    }
    .inner
    {
        display: inline-block;
        width: 60px;
        height: 60px;
    }
</style>
