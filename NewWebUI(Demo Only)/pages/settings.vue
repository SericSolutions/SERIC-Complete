<template>
    <v-container grid-list-md text-xs-center fluid>
        <v-card>
            <v-layout row wrap v-for="j in 2" fluid>
                <v-flex xs12 sm6 md6 lg3 v-for="i in 4">
                    <v-card class="CardBox1" raised>
                        <v-card-title primary-title>
                            <div>
                                <v-icon xLarge class="center">settings</v-icon>
                                <h3 class="headline mb-1 center">Setting</h3>
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
            </v-layout>
        </v-card>
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