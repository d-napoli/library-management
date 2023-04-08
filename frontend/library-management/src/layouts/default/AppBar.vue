<template v-slot:mainContent>
  <v-app>
    <v-app-bar :elevation="2">
      <v-app-bar-title>Biblioteca</v-app-bar-title>
  
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer>
      <v-list>
        <v-list-item
          v-for="[icon, text] in $data.links"
          :key="icon"
          link
        >
          <template v-slot:prepend>
            <v-icon>{{ icon }}</v-icon>
          </template>

          <v-list-item-title>{{ text }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <slot />
  </v-app>
</template>

<script lang="ts" setup>
  const $data = {
    drawer: null,
    links: [
      ['mdi-account', 'Usuários'],
      ['mdi-account-edit', 'Autores'],
      ['mdi-send', 'Obras'],
      ['mdi-book', 'Exemplares'],
      ['mdi-ray-start-end', 'Empréstimos'],
    ],
  }
</script>
