<template>
  <v-row justify="center" align="center">
    <v-col cols="6">
      <v-stepper v-model="e1">
        <v-stepper-header>
          <v-stepper-step :complete="e1 > 1" step="1">
            Name
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step :complete="e1 > 2" step="2">
            Email address
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="3">
            Personal Address
          </v-stepper-step>
        </v-stepper-header>
        <v-stepper-items>
          <v-stepper-content step="1">
            <v-card
              class="ma-5 pa-5 mb-12"
              height="200px"
            >
              <v-text-field
                v-model="firstname"
                label="First name"
                required
              ></v-text-field>
              <v-text-field
                v-model="firstname"
                label="Last name"
                required
              ></v-text-field>
            </v-card>
            <v-btn color="primary" @click="e1 = 2">
              Continue
            </v-btn>
            <v-btn text>
              Cancel
            </v-btn>
          </v-stepper-content>
          <v-stepper-content step="2">
            <v-card
              class="ma-5 pa-5 mb-12"
              height="200px"
            >
              <v-text-field
                v-model="firstname"
                label="Gmail address"
                required
              ></v-text-field>
              <v-text-field
                v-model="firstname"
                label="Yahoo address"
                required
              ></v-text-field>
            </v-card>
            <v-btn color="primary" @click="e1 = 3">
              Continue
            </v-btn>
            <v-btn text>
              Cancel
            </v-btn>
          </v-stepper-content>
          <v-stepper-content step="3">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>
            <v-btn color="primary" @click="startCrawling">
              Continue
            </v-btn>

            <v-btn text>
              Cancel
            </v-btn>
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-col>
  </v-row>
</template>
<script>
  export default {
    data () {
      return {
        e1: 1,
      }
    },
    methods: {
      startCrawling () {
        window.href('/scrapping')
      }
    }
  }
</script>
