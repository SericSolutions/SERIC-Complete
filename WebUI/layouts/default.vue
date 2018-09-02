<template>
  <v-app light toolbar footer>
    <v-navigation-drawer
      persistent
      :mini-variant="miniVariant"
      :clipped="clipped"
      v-model="drawer"
      dark
    >
      <v-list>
        <v-list-tile
          router
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
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
    <v-toolbar fixed>
      <!--<v-toolbar-side-icon @click.native.stop="drawer = !drawer"></v-toolbar-side-icon>-->
      <v-btn
        icon
        @click.native.stop="miniVariant = !miniVariant"
      >
        <v-icon v-html="miniVariant ? 'chevron_right' : 'chevron_left'"></v-icon>
      </v-btn>
     <!-- <v-btn
        icon
        @click.native.stop="clipped = !clipped"
      >
        <v-icon>web</v-icon>
      </v-btn>-->
      <v-toolbar-title v-text="title"></v-toolbar-title>
    </v-toolbar>
    <main>
      <v-container fluid>
        <nuxt />
      </v-container>
    </main>
  </v-app>
</template>

<script>
  export default {
    data () {
      return {
        clipped: true,
        drawer: true,
        fixed: false,
        items: [
          { icon: 'widgets', title: 'Welcome', to: '/' },
          { icon: 'insert_photo', title: 'Pictures', to: '/pictures' },
          { icon: 'videocam', title: 'Video', to: '/video' },
          { icon: 'people', title: 'People', to: '/people' },
          { icon: 'volume_up', title: 'Auto Attendant', to: '/autoattendant' }
        ],
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'SERIC ADMIN PANEL'
      }
    }
  }
</script>