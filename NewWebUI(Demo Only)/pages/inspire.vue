<template>
  <div>
    <v-select
            :items="people"
            label="Select"
            single-line
    ></v-select>
    <v-tabs
            v-model="active"
            color="secondaryDark"
            dark
            slider-color="PrimaryDark"
            centered = 'true'

    >
      <v-tab
              v-for="n in date"
              :key="n"
              ripple
      >
        {{ n }}
      </v-tab>
      <v-tab-item
              v-for="n in 3"
              :key="n"
      >
        <v-container grid-list-md text-xs-center>
            <v-layout row wrap v-for="j in 2">
              <v-flex xs12 sm4 md2 v-for="i in 6">
                <v-card class='CardBox' raised>
                  <v-card-media src='/asad.jpg' height='100px'>
                  </v-card-media>
                  <v-card-text>
                    <div>15 minutes ago</div>
                    <div> Omer Khan</div>
                  </v-card-text>
                </v-card>
              </v-flex>
            </v-layout>
        </v-container>

      </v-tab-item>
    </v-tabs>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        active: null,
        date: ['24 Hours', '48 Hours', '7 Days', 'Custom'],
        people: ['Filter people', 'Asad Umar', 'Omer Khan', 'Known', 'unKnown']
      }
    },
    methods: {
      next () {
        const active = parseInt(this.active)
        this.active = (active < 2 ? active + 1 : 0).toString()
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

