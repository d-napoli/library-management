<template>
    <td>{{ $props.exemplary.id }}</td>

    <td>{{ $props.exemplary.title }}</td>

    <td>{{ $props.exemplary.author }}</td>

    <td>
        <v-chip :color="getBookTypeColor($props.exemplary.type)">
            {{ getBookType($props.exemplary.type) }}
        </v-chip>
    </td>

    <td>
        <v-chip :color="getStatusColor($props.exemplary.active)">
            {{ getStatusText($props.exemplary.active) }}
        </v-chip>
    </td>

    <td>
        <v-chip :color="$props.exemplary.is_borrowed ? 'success' : 'error'">
            {{ $props.exemplary.is_borrowed ? "Sim" : "Não" }}
        </v-chip>
    </td>

    <td>
        <slot />
    </td>
</template>

<script setup>
import { getBookType, getBookTypeColor, getStatusText, getStatusColor } from '@/constants'

const $props = defineProps({
    exemplary: {
        type: Object,
        required: true
    }
})
</script>