<template v-slot:mainContent>
  <v-app>
    <v-app-bar :elevation="2">
      <v-app-bar-title>Biblioteca</v-app-bar-title>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer>
      <v-list>
        <v-list-item v-for="item in $data.menuItens" :key="item.name" link>
          <template v-slot:prepend>
            <v-icon>{{ item.icon }}</v-icon>
          </template>

          <v-list-item-title @click="handleClick(item.route)" :to="{ name: 'item.route' }">{{ item.name
          }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <slot />
  </v-app>
</template>

<script setup>
import router from '@/router'

const handleClick = (theRouteName) => {
  router.push(theRouteName)
}

const $data = {
  drawer: null,
  menuItens: [
    {
      "icon": 'mdi-account',
      "name": 'Usuários',
      "route": "/users"
    },
    {
      "icon": 'mdi-account-edit',
      "name": 'Autores',
      "route": "/authors"
    },
    {
      "icon": 'mdi-send',
      "name": 'Obras',
      "route": "/users"
    },
    {
      "icon": 'mdi-book',
      "name": 'Exemplares',
      "route": "/users"
    },
    {
      "icon": 'mdi-ray-start-end',
      "name": 'Empréstimos',
      "route": "/users"
    },
  ]
}
</script>
