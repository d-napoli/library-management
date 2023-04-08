<template>
  <v-card
    width="400"
    :title="$props.title"
    :subtitle=$props.subtitle
  >
    <v-card-actions>
      <v-btn variant="outlined">
        {{$props.buttonText}}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script lang="ts" setup>
  const $props = defineProps({
    title: {
      type: String,
      required: true
    },
    subtitle: {
      type: String,
      required: true
    },
    buttonText: {
      type: String,
      required: true
    }
  })
</script>
