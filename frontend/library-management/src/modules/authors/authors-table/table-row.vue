<template>
    <td>{{ author.id }}</td>
    <td>{{ author.name }}</td>
</template>

<script setup>
const $props = defineProps({
    author: {
        type: Object,
        required: true
    }
})
</script>