<template>
    <td>{{ customer.id }}</td>

    <td>{{ customer.first_name }} {{ customer.last_name }}</td>

    <td>{{ customer.email }}</td>

    <td>
        <v-chip :color="customer.type == 'student' ? 'primary' : 'secondary'">
            {{ customer.type == 'student' ? 'Estudante' : 'Professor' }}
        </v-chip>
    </td>

    <td>
        <v-chip :color="customer.is_active ? 'green' : 'red'">
            {{ customer.is_active ? 'Ativo' : 'Inativo' }}
        </v-chip>
    </td>

    <td>
        <slot />
    </td>
</template>

<script setup>
const $props = defineProps({
    customer: {
        type: Object,
        default: null,
    }
})
</script>