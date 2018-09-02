<template>
    <v-app :dark="dark">
        <v-navigation-drawer
                :mini-variant.sync="miniVariant"
                :clipped="clipped"
                v-model="drawer"
                fixed
                app
                dark
                class="secondaryDark"
        >
            <v-list class="secondaryDark">
                <v-list-tile
                        router
                        :to="item.to"
                        :key="i"
                        v-for="(item, i) in items"
                        exact
                >
                    <v-list-tile-action>
                        <v-icon v-html="item.icon"></v-icon>
                    </v-list-tile-action>

                    <v-list-tile-content>
                        <v-list-tile-title v-text="item.title"></v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>

        <v-toolbar fixed app dark :clipped-left="clipped" class="primary">

            <v-toolbar-side-icon @click="drawer = !drawer"></v-toolbar-side-icon>

            <v-btn
                    icon
                    flat
                    @click="dark =!dark"
            >
                <v-icon color="red" >lens</v-icon>
            </v-btn>

            <v-toolbar-title v-text="title"></v-toolbar-title>
            <v-spacer></v-spacer>

                <v-btn
                        icon
                        large
                        @click.stop="x()"
                >
                    <v-icon large>speaker_notes</v-icon>
                </v-btn>



        </v-toolbar>

        <v-content >
            <v-container>
                <nuxt />
            </v-container>
        </v-content>

        <v-navigation-drawer
                temporary
                :right="right"
                v-model="rightDrawer"
                fixed
        >
            <v-list>
                <v-list-tile >
                    <v-list-tile-title>
                        Timeline
                    </v-list-tile-title>
                </v-list-tile>

                <v-flex m6>
                    <v-card class="CardBox" raised>
                        <v-card-media src="/asad.jpg" height="150px">
                        </v-card-media>
                        <v-card-title primary-title>
                            <div>
                                <h3 class="headline mb-0">Today, 9:00 PM</h3>
                                <div>Asad came home possessed by a demon, do i let him in? </div>
                            </div>
                        </v-card-title>
                        <v-card-actions>
                            <v-btn flat color="orange">Yes</v-btn>
                            <v-btn flat color="orange">Hell No</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>

                <v-flex  m6>
                    <v-card class="CardBox" raised>
                        <v-card-title primary-title>
                            <div>
                                <h3 class="headline mb-0">Today, 8:45 PM</h3>
                                <div>Asad Tried to call upon satan to help with his existential crisis, do i stop him? </div>
                            </div>
                        </v-card-title>
                        <v-card-actions>
                            <v-btn flat color="orange">Yes</v-btn>
                            <v-btn flat color="orange">Hell No</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>

                <v-flex m6>
                    <v-card class="CardBox" raised>
                        <v-card-media src="/asad.jpg" height="150px">
                        </v-card-media>
                        <v-card-actions>
                            <v-btn flat color="orange">Yes</v-btn>
                            <v-btn flat color="orange">Hell No</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-flex>

                <v-flex m6>
                    <v-card class="CardBox" raised>
                        <v-card-media src="/asad.jpg" height="150px">
                        </v-card-media>
                    </v-card>
                </v-flex>

            </v-list>
        </v-navigation-drawer>

    </v-app>
</template>


<script>
  export default {
    components: {
    },
    data () {
      return {
        c: 'red darken-2',
        clipped: true,
        drawer: true,
        fixed: false,
        dark: false,
        items: [
          { icon: 'home', title: 'Home', to: '/' },
          { icon: 'insert_photo', title: 'Pictures', to: '/inspire' },
          { icon: 'people', title: 'People', to: '/people' },
          { icon: 'settings', title: 'Settings', to: '/settings' }
        ],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'SERIC'
      }
    },
    methods: {
      x () {
        this.rightDrawer = !this.rightDrawer

        if (this.c === 'red darken-2') {
          this.c = 'grey'
        } else {
          this.c = 'red darken-2'
        }
      }
    }
  }
</script>


<style>
    .CardBox{
        /*border: 1px solid black;*/
        margin: 10px;
    }
</style>
