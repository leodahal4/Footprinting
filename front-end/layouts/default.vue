<template>
  <v-app>
    <NavBar v-if="show" />
    <nuxt />
    <FooterBar />
  </v-app>
</template>

<script>
import NavBar from '../components/NavBar'
import FooterBar from '../components/FooterBar'
export default {
  data () {
    return {
      route: '',
      index: 'index'
    }
  },
  computed: {
    show () {
      this.route = this.$route.name
      if (this.route != this.index)
        return true
      else
        return false
    }
  }
}
</script>
