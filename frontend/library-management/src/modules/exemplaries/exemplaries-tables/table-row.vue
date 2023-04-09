<template>
    <td>{{ $props.exemplary.id }}</td>

    <td>{{ $props.exemplary.title }}</td>

    <td>{{ $props.exemplary.author }}</td>

    <td>
        <v-chip :color="getBookTypeColor($props.exemplary.type)">
            {{ getBookType($props.exemplary.type) }}
        </v-chip>
    </td>

    <td>{{ $props.exemplary.quantity }}</td>

    <td>
        <slot />
    </td>
</template>

<script setup>
import { WORKS_TYPES } from '@/constants'

const getBookType = (bookType) => {
    return WORKS_TYPES[bookType]["name"]
}

const getBookTypeColor = (bookType) => {
    return WORKS_TYPES[bookType]["color"]
}

const $props = defineProps({
    exemplary: {
        type: Object,
        required: true
    }
})
</script>