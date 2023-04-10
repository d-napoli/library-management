<template>
    <v-row align="center" justify="space-between">
        <v-col cols="12" md="4">
            <PageHeader title="Usuários" />
        </v-col>

        <v-col class="text-right" cols="12" md="2">
            <NewUserModal @snackBar="handleSnackBar($event)" />
        </v-col>
    </v-row>

    <v-row>
        <v-col cols="12">
            <v-checkbox v-model="$state.showInactiveUsers" @click="handleShowInactiveUsers"
                label="Mostrar usuários inativos"></v-checkbox>
        </v-col>
    </v-row>

    <v-row>
        <v-col cols="12" md="12">
            <v-container v-if="$state.isLoading">
                <v-progress-circular indeterminate color="primary"></v-progress-circular>
            </v-container>

            <TableHeader v-else :items="$state.customers">
                <tbody>
                    <tr v-for="customer in $state.customers" :key="customer.id">
                        <TableRow @snackBar="handleSnackBar($event)" :customer="customer">
                            <TableActions :customer="customer" @snackBar="handleSnackBar($event)" />
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
import { CustomerServices } from '@/services';
import { onMounted, reactive } from 'vue';
import { TableHeader, TableRow, TableActions } from '@/modules/users/users-tables';
import NewUserModal from '@/modules/users/new-user-modal.vue'

const handleSnackBar = (event) => {
    $alertState.isActive = true
    $alertState.text = event.title
    $alertState.type = event.type

    if (event.type == "success") {
        requestAllUsers();
    }
}

const $alertState = reactive({
    isActive: false,
    text: null,
    type: "info",
    duration: 1000
})

const $state = reactive({
    customers: null,
    allCustomers: null,
    isLoading: false,
    showInactiveUsers: true
});

onMounted(() => {
    requestAllUsers();
});

const requestAllUsers = async () => {
    $state.isLoading = true;

    CustomerServices.getAllCustomers()
        .then(({ customers }) => {
            $state.customers = customers
            $state.allCustomers = customers
        })
        .finally(() => {
            $state.isLoading = false;
        });
}

const handleShowInactiveUsers = () => {
    $state.showInactiveUsers = !$state.showInactiveUsers;
    $state.customers = !$state.showInactiveUsers ? $state.customers.filter((user) => user.is_active) : $state.allCustomers
}

</script>