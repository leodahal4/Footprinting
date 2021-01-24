<template>
  <v-footer
    dark
    padless
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="teal">
        <strong class="text-h6">Get connected with us !</strong>
        <v-spacer></v-spacer>
        <v-btn
          class="mx-4"
          dark
          icon
          @click="goToGitHub"
        >
          <v-icon size="24px">
            mdi-github
          </v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text class="py-2 white--text text-center">
        {{ new Date().getFullYear() }} — <strong>Pro-X</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>
<script>
  export default {
    methods: {
      goToGitHub () {
        window.open('https://github.com/leodahal4/Footprinting','_blank');
      }
    }
  }
</script>
