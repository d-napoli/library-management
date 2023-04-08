<template>
    <v-row align="center" justify="space-between">
        <v-col cols="12" md="4">
            <PageHeader title="Obras" />
        </v-col>

        <v-col class="text-right" cols="12" md="2">
            <v-btn v-bind="props">
                <v-icon>mdi-plus</v-icon>&nbsp;
                Nova obra
            </v-btn>
        </v-col>
    </v-row>

    <v-row>
        <v-col cols="12" md="12">
            <v-container v-if="$state.isLoading">
                <v-progress-circular indeterminate color="primary"></v-progress-circular>
            </v-container>

            <TableHeader v-else :items="$state.works">
                <tbody>
                    <tr v-for="work in $state.works" :key="work.id">
                        <TableRow :work="work">
                            <TableActions @snackBar="handleSnackBar($event)" :work="work" />
                        </TableRow>
                    </tr>
                </tbody>
            </TableHeader>
        </v-col>
    </v-row>

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

import { TableHeader, TableRow, TableActions } from '@/modules/works/works-tables';
import { onMounted, reactive } from 'vue';
import { WorksServices } from '@/services';

const $state = reactive({
    works: null,
    isLoading: false,
    authors: null,
});

onMounted(() => {
    requestAllWorks();
});

const requestAllWorks = async () => {
    $state.isLoading = true;

    WorksServices.getAllWorks()
        .then(({ works }) => {
            $state.works = works
        })
        .finally(() => {
            $state.isLoading = false;
        });
}

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
        requestAllWorks();
    }
}
</script>