<template>
    <v-row align="center" justify="space-between">
        <v-col cols="12" md="4">
            <PageHeader title="Autores" />
        </v-col>

        <v-col class="text-right" cols="12" md="2">
            <NewAuthorModal @snackBar="handleSnackBar($event)" />
        </v-col>
    </v-row>

    <template v-if="$state.isLoading">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </template>

    <TableHeader v-else>
        <tbody>
            <tr v-for="author in $state.authors" :key="author.id">
                <TableRow @snackBar="handleSnackBar($event)" :author="author" />
            </tr>
        </tbody>
    </TableHeader>

    <v-snackbar v-model="$alertState.isActive" :color="$alertState.type" :timeout="2000">
        {{ $alertState.text }}

        <template v-slot:actions>
            <v-btn variant="text" @click="$alertState.isActive = false">
                Fechar
            </v-btn>
        </template>
    </v-snackbar>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue';
import { TableHeader, TableRow } from '@/modules/authors/authors-table';
import { onMounted, reactive } from 'vue';
import { AuthorServices } from '@/services';
import NewAuthorModal from '@/modules/authors/new-author-modal.vue'

onMounted(() => {
    requestAllAuthors()
})

const $state = reactive({
    isLoading: false,
    authors: []
})

const $alertState = reactive({
    isActive: false,
    text: null,
    type: "info",
    duration: 1000
})

const handleSnackBar = (event) => {
    $alertState.isActive = true
    $alertState.text = event.title
    $alertState.type = event.type

    if (event.type == "success") {
        requestAllAuthors();
    }
}

const requestAllAuthors = async () => {
    $state.isLoading = true;

    AuthorServices.getAllAuthors()
        .then(({ authors }) => {
            console.log(authors)
            $state.authors = authors;
        })
        .catch(({ error }) => {
            console.log(error)
        })
        .finally(() => {
            $state.isLoading = false;
        })
}

</script>