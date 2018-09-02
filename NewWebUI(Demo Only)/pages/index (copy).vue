<template>
    <v-container grid-list-md>
        <v-layout column>
            <v-card>
                <v-flex>
                    <v-layout row v-for="j in 2">
                        <v-card v-for="i in 5" flat>
                            <v-flex md12>
                                <v-card class="CardBox1" raised>
                                    <v-card-title primary-title>
                                        <div>
                                            <v-icon xLarge class="center">settings</v-icon>
                                            <h3 class="headline mb-1 center">Setting # {{((j*5)+ i) - 5}}</h3>
                                            <div>Asad came home possessed by a demon, do i let him in? </div>
                                        </div>
                                    </v-card-title>
                                    <div class="center">
                                        <v-card-actions v-if="j == 1">
                                            <v-btn flat color="orange">Yes</v-btn>
                                            <v-btn flat color="orange">Hell No</v-btn>
                                        </v-card-actions>

                                        <v-card-actions v-if="j == 2">
                                            <v-switch value input-value="true"></v-switch>
                                        </v-card-actions>
                                    </div>
                                </v-card>
                            </v-flex>
                        </v-card>
                    </v-layout>
                        <v-btn
                                absolute
                                dark
                                fab
                                bottom
                                right
                                color="blue darken-2"
                                style="right: -2%; bottom: -8%"
                        >
                            <v-icon>add</v-icon>
                        </v-btn>
                </v-flex>
            </v-card>
        </v-layout>



    </v-container>
</template>

<script>
  export default {
    components: {
    },
    data: () => ({
      switch1: true,
      lorem: `Lorem ipsum dolor sit amet, mel at clita quando. Te sit oratio vituperatoribus, nam ad ipsum posidonium mediocritatem, explicari dissentiunt cu mea. Repudiare disputationi vim in, mollis iriure nec cu, alienum argumentum ius ad. Pri eu justo aeque torquatos.`
    })
  }
</script>

<style>
    .CardBox1{
        margin: 8px;
    }
    .center{
        display: flex;
        justify-content: center;
    }
</style>