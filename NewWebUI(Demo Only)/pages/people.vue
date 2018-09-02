<template>
    <div>
        <h1>People</h1>

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

    </div>
</template>

<script>

</script>