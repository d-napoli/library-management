<template>
    <td>{{ author.id }}</td>

    <td>{{ author.name }}</td>

    <td>
        <EditAuthorModal @snackBar="handleSnackBar($event)" :author="$props.author" />
    </td>
</template>

<script setup>
import { reactive } from "vue"
import EditAuthorModal from '@/modules/authors/edit-author-modal.vue'

const $state = reactive({
    isOpen: false
})

const $props = defineProps({
    author: {
        type: Object,
        required: true
    }
})

const handleSnackBar = (event) => {
    $emit('snackBar', event);
}

const $emit = defineEmits(['snackBar']);
</script>