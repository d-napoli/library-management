<template v-slot:blingbling>
    <PageHeader title="Usuários" />

    <v-container v-if="$state.isLoading">
        <v-progress-circular indeterminate color="primary"></v-progress-circular>
    </v-container>

    <TableHeader v-else :items="$state.customers">
        <tbody>
            <tr v-for="customer in $state.customers" :key="customer.id">
                <TableRow :customer="customer" />
            </tr>
        </tbody>
    </TableHeader>
</template>

<script setup>
import PageHeader from '@/components/PageHeader.vue';
import { CustomerServices } from '@/services';
import { onMounted, reactive } from 'vue';
import { TableHeader, TableRow } from '@/modules/users/users-tables';

const $state = reactive({
    customers: null,
    isLoading: false,
});

onMounted(() => {
    requestAllUsers();
});

const requestAllUsers = async () => {
    $state.isLoading = true;

    CustomerServices.getAllCustomers()
        .then(({ customers }) => {
            $state.customers = customers;
        })
        .finally(() => {
            $state.isLoading = false;
        });
}

</script>