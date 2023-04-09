<template>
    <v-row align="center" justify="space-between">
        <v-col cols="12" md="4">
            <PageHeader title="Empréstimos" />
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

            <TableHeader v-else :items="$state.loans">
                <tbody>
                    <tr v-for="loan in $state.loans" :key="loan.id">
                        <TableRow :loan="loan">
                            <TableActions @snackBar="handleSnackBar($event)" :loan="loan" />
                        </TableRow>
                    </tr>
                </tbody>
            </TableHeader>
        </v-col>
    </v-row>

    <!-- <v-snackbar v-model="$alertState.isActive" :color="$alertState.type" :timeout="2000">
        {{ $alertState.text }}

        <template v-slot:actions>
            <v-btn variant="text" @click="$alertState.isActive = false">
                Fechar
            </v-btn>
        </template>
    </v-snackbar> -->
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue';

import { TableHeader, TableRow, TableActions } from '@/modules/loans/loans-tables';
import { onMounted, reactive } from 'vue';
import { LoanServices } from '@/services';
import NewExemplaryModal from '@/modules/exemplaries/new-exemplary-modal.vue'

const $state = reactive({
    loans: null,
    isLoading: false,
    authors: null,
});

onMounted(() => {
    requestAllLoans();
});

const requestAllLoans = async () => {
    $state.isLoading = true;

    LoanServices.getAllLoans()
        .then(({ loans }) => {
            $state.loans = loans
        })
        .finally(() => {
            $state.isLoading = false;
        });
}

// const $alertState = reactive({
//     isActive: false,
//     text: null,
//     type: "info",
//     duration: 1000
// })

// const handleSnackBar = (event) => {
//     $alertState.isActive = true
//     $alertState.text = event.title
//     $alertState.type = event.type

//     if (event.type == "success") {
//         requestAllExemplaries();
//     }
// }
</script>