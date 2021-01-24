<template>
  <v-row>
    <v-col>
      <tile loading="isLoading"></tile>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    name: 'Scrapping',
    data () {
      isLoading: true
    }
  }
</script>
