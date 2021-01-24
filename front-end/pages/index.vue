<template>
  <v-row justify="center" align="center">
    <v-col cols="3">
      <v-hover
        v-slot="{ hover }"
      >
      <v-card height="50vh" :elevation="hover? 12 : 2" to="/organization">
        <v-card-title>
            <v-img
              height="30vh"
              width="100%"
              src="/company.png"
              contain
              style="background: white!important;"
            />
        </v-card-title>
        <v-card-text class="text-h2">
          Organization
        </v-card-text>
      </v-card>
      </v-hover>
    </v-col>
    <v-col cols="3">
      <v-hover
        v-slot="{ hover }"
      >
      <v-card height="50vh" :elevation="hover? 12:2" to="/person">
        <v-card-title>
            <v-img
              height="30vh"
              width="100%"
              src="/person.png"
              contain
              style="background: white!important;"
            />
        </v-card-title>
        <v-card-text class="text-h2">
          Person
        </v-card-text>
      </v-card>
      </v-hover>
    </v-col>
  </v-row>
</template>

<script>

export default {
}
</script>

<style scoped>
  .v-card{
    cursor: pointer!important;
  }
</style>
