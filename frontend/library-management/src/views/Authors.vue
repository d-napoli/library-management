<template>
    <PageHeader title="Autores" />

    <template v-if="$state.isLoading">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </template>

    <TableHeader v-else>
        <tbody>
            <tr v-for="author in $state.authors" :key="author.id">
                <TableRow :author="author" />
            </tr>
        </tbody>
    </TableHeader>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue';
import { TableHeader, TableRow } from '@/modules/authors/authors-table';
import { onMounted, reactive } from 'vue';
import { AuthorServices } from '@/services';

onMounted(() => {
    requestAllAuthors()
})

const $state = reactive({
    isLoading: false,
    authors: []
})

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