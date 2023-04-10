<template>
  <v-app>
    <default-bar>
      <v-container>
        <default-view class="default-view" />
      </v-container>
    </default-bar>

    <v-snackbar v-model="$alertState.isActive" :color="$alertState.type" :timeout="2000">
      {{ $alertState.text }}

      <template v-slot:actions>
        <v-btn variant="text" @click="$alertState.isActive = false">
          Fechar
        </v-btn>
      </template>
    </v-snackbar>

    <Footer />
  </v-app>
</template>

<script setup>
import DefaultBar from './AppBar.vue'
import DefaultView from './View.vue'
import Footer from './Footer.vue'
import { reactive } from 'vue';

const handleSnackBar = (event) => {
  $alertState.isActive = true
  $alertState.text = event.title
  $alertState.type = event.type

  if (event.type == "success") {
    requestAllUsers();
  }
}

const $alertState = reactive({
  isActive: false,
  text: null,
  type: "info",
  duration: 1000
})
</script>
