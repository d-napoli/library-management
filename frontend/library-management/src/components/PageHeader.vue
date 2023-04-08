<template>
    <h1>{{ $props.title }}</h1>
</template>

<script lang="ts" setup>
const $props = defineProps({
    title: {
        type: String,
        required: true
    }
})

</script>