<template>
    <v-container grid-list-md text-xs-center fluid>
        <v-layout row wrap>
            <v-flex column xs12 md4 v-for="i in ppl">
                <v-card>
                    <v-card-media height="325px">
                        <img :src="i.img">
                    </v-card-media>
                    <v-card-text>
                        <h1 >{{i.name}}</h1>
                    </v-card-text>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>


<script>
  export default {
    components: {
    },
    data: () => ({
      switch1: true,
      ppl: [
        {name: 'Asad Umar', img: 'asad2.jpg'},
        {name: 'Abdullah Nafees', img: 'abd.jpg'},
        {name: 'Rehan Qazi', img: 'rehan.jpg'},
        {name: 'Rauf Butt', img: 'rauf.jpg'},
        {name: 'Dr Nazim Ashraf', img: 'nazim.jpg'}
      ]
    })
  }
</script>