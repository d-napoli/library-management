<template>
    <v-row align="center" justify="space-between">
        <v-col cols="12" md="4">
            <PageHeader title="Exemplares" />
        </v-col>

        <v-col class="text-right" cols="12" md="2">
            <NewExemplaryModal @snackBar="handleSnackBar($event)" />
        </v-col>
    </v-row>

    <v-row>
        <v-col cols="12" md="12">
            <v-container v-if="$state.isLoading">
                <v-progress-circular indeterminate color="primary"></v-progress-circular>
            </v-container>

            <TableHeader v-else :items="$state.exemplaries">
                <tbody>
                    <tr v-for="exemplary in $state.exemplaries" :key="exemplary.id">
                        <TableRow :exemplary="exemplary" />
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

import { TableHeader, TableRow } from '@/modules/exemplaries/exemplaries-tables';
import { onMounted, reactive } from 'vue';
import { ExemplaryServices } from '@/services';
import NewExemplaryModal from '@/modules/exemplaries/new-exemplary-modal.vue'

const $state = reactive({
    exemplaries: null,
    isLoading: false,
    authors: null,
});

onMounted(() => {
    requestAllExemplaries();
});

const requestAllExemplaries = async () => {
    $state.isLoading = true;

    ExemplaryServices.getAllExemplaries()
        .then(({ exemplaries }) => {
            $state.exemplaries = exemplaries
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
        requestAllExemplaries();
    }
}
</script>