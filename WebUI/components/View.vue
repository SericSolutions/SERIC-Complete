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
                <v-card-media>
                    <img :src="`http://${server}/${currentItem.link}`" height="100%" width="100%"/>
                </v-card-media>

                <v-card-actions> <!-- style="background-color: grey" -->
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

                    <v-btn icon flat dark
                           :primary = "currentItem.fav == 1 ? true: false"
                           :class = "!currentItem.fav == 1 ? 'inner blue accent-2' : 'inner grey lighten-3'"
                           @click.native = "fav()"
                    >
                        <v-icon large>thumb_up</v-icon>
                    </v-btn>

                    <a :href="`http://${server}/${currentItem.link}`" download>
                        <v-btn dark icon
                               @click.native="dialog = false"
                               class = "inner green lighten-1"
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
        beforeMount()
        {
            this.currentItem = this.item
            this.server = this.$parent.serverName;
            this.port = this.$parent.port;

            this.validate(this.$parent.items.indexOf(this.item));
            window.addEventListener('keydown', this.KeyListener);

        },
        props: ['item'],
        methods: {
            KeyListener(e){
                if(this.dialog) {
                    if (e.key == "ArrowRight")
                        this.next();

                    else if (e.key == "ArrowLeft")
                        this.prev();

                    else if (e.key == "Escape")
                        this.dialog = false;

                    else if (e.key == "Delete")
                        this.del()
                }
            },
            findAndRemove(array, property, value) {
                array.forEach(function(result, index) {
                    if(result[property] === value) {
                        array.splice(index, 1);
                    }
                });
            },
            del()
            {
                var request = `http://${this.$parent.serverName}:${this.$parent.port}/del/${this.currentItem.pictureName}`;

                if (confirm('Are you sure you want to Delete this picture?')) {
                    axios.delete(request)
                        .then(response => {
                            this.findAndRemove(this.$parent.items, 'pictureName', this.currentItem.pictureName);
                            this.dialog = false
                        })
                }
            },
            next()
            {
                try {
                    if(!this.FD) {
                        this.validate(this.$parent.items.indexOf(this.currentItem) + 1);
                        this.currentItem = this.$parent.items[
                        this.$parent.items.indexOf(this.currentItem) + 1
                            ]
                    }

                }
                catch(e) {
                    if(e instanceof TypeError) {
                        console.log("cant go forth");
                        this.FD = true
                    }

                }
            },
            prev()
            {
                try {
                    if(!this.BD) {
                        this.currentItem = this.$parent.items[
                        this.$parent.items.indexOf(this.currentItem) - 1
                            ]
                        this.validate(this.$parent.items.indexOf(this.currentItem));
                    }

                }
                catch(e) {
                    if(e instanceof TypeError) {
                        console.log("cant go back");
                        this.BD = true;
                    }
                }
            },
            reload()
            {
                this.currentItem = this.item
                this.validate(this.$parent.items.indexOf(this.currentItem))

            },
            validate(index)
            {
                var size = this.$parent.items.length - 1;
                var arr = this.$parent.items;
                var i = this.$parent.items[index];


                if(arr[0] == i)
                    this.BD = true;
                else
                    this.BD = false;

                if(arr[size] == i)
                    this.FD = true;
                else
                    this.FD = false;
            },
            fav()
            {
                var request = `http://${this.server}:${this.port}/fav/${this.currentItem.pictureName}/${!this.currentItem.fav? 1:0}`
                axios.post(request)
                    .then(response => {
                        this.currentItem.fav = !this.currentItem.fav
                    })
            },
            intToBool()
            {
                if (this.currentItem.fav)
                    return true;
                else
                    return false;
            }

        },
        data (){
            return {
                server: null,
                port: null,
                dialog: false,
                currentItem: null,
                FD: false,
                BD: false,
            }
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
        margin-left: 6%;
    }
</style>