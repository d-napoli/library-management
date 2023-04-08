<template>
  <v-app>
    <default-bar>
      <v-container>
        <default-view class="default-view" />
      </v-container>
    </default-bar>

    <Footer />
  </v-app>
</template>

<script lang="ts" setup>
import DefaultBar from './AppBar.vue'
import DefaultView from './View.vue'
import Footer from './Footer.vue'
</script>
