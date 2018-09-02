import Vue from 'vue'
import {
  Vuetify,
  VApp,
  VCard,
  VNavigationDrawer,
  VFooter,
  VList,
  VBtn,
  VIcon,
  VGrid,
  VToolbar,
  VSwitch,
  VTabs,
  VSelect
} from 'vuetify'

Vue.use(Vuetify, {
  theme: {
    primary: '#37474f',
    primaryDark: '#102027',
    primaryLight: '#62727b',
    secondary: '#26A69a',
    secondaryDark: '#00766c',
    secondaryLight: '#64d8cb',
    accent: '#8c9eff',
    error: '#b71c1c'
  },
  components: {
    VApp,
    VCard,
    VNavigationDrawer,
    VFooter,
    VList,
    VBtn,
    VIcon,
    VGrid,
    VToolbar,
    VSwitch,
    VTabs,
    VSelect
  }
})
