<template>
    <td>{{ $props.work.id }}</td>

    <td>{{ $props.work.title }}</td>

    <td>{{ $props.work.author }}</td>

    <td>
        <v-chip :color="getBookTypeColor($props.work.type)">
            {{ getBookType($props.work.type) }}
        </v-chip>
    </td>

    <td>{{ $props.work.quantity }}</td>

    <td>
        <slot />
    </td>
</template>

<script setup>
import { getBookType, getBookTypeColor } from '@/constants'

const $props = defineProps({
    work: {
        type: Object,
        required: true
    }
})
</script>