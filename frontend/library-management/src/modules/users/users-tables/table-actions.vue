<template>
    <v-menu>
        <template v-slot:activator="{ props }">
            <v-btn variant="text" icon="mdi-menu-down" v-bind="props" />
        </template>

        <v-list>
            <v-list-item>
                <EditUserModal @snackBar="handleSnackBar($event)" :customer="$props.customer" />
            </v-list-item>

            <v-list-item>
                <ActivateUserModal @snackBar="handleSnackBar($event)" :customer="$props.customer" />
            </v-list-item>
        </v-list>
    </v-menu>
</template>

<script setup>
import ActivateUserModal from '@/modules/users/activate-user-modal.vue'
import EditUserModal from '@/modules/users/edit-user-modal.vue'

const $props = defineProps({
    customer: {
        type: Object,
        default: null,
    }
})

const handleSnackBar = (event) => {
    $emit('snackBar', event);
}

const $emit = defineEmits(['snackBar']);
</script>