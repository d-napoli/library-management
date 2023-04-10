<template>
    <v-dialog v-model="$state.isOpen" width="800">
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props">
                <v-icon>mdi-plus</v-icon>&nbsp;
                Novo Empréstimo
            </v-btn>
        </template>

        <v-container>
            <v-card class="pl-5 pr-5">
                <v-card-title class="pt-10">
                    <span class="text-h4">
                        Novo Empréstimo
                    </span>
                </v-card-title>

                <v-card-text>
                    <v-form v-model="valid">
                        <v-container>
                            <v-row>
                                <v-col cols="12" md="12">
                                    <template v-if="$state.isLoadingWorks">
                                        <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                                    </template>

                                    <v-autocomplete v-else label="Obra" v-model="$state.selectedWork"
                                        :items="getWorkTitles()"></v-autocomplete>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12" md="12">
                                    <template v-if="$state.isLoadingUsers">
                                        <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                                    </template>

                                    <v-autocomplete v-else label="Cliente" v-model="$state.selectedClient"
                                        :items="getCustomerNames()"></v-autocomplete>
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12" md="6">
                                    <label>Início</label>
                                    <VueDatePicker :format="format" :teleport="true" v-model="$state.fromDate"
                                        :enable-time-picker="false" />
                                </v-col>

                                <v-col cols="12" md="6">
                                    <label>Fim</label>
                                    <VueDatePicker :format="format" :teleport="true" v-model="$state.toDate"
                                        :enable-time-picker="false" />
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-form>
                </v-card-text>

                <v-card-actions class="pb-5">
                    <v-spacer></v-spacer>

                    <v-btn color="red" flat variant="text" @click="$state.isOpen = false">
                        Cancelar
                    </v-btn>

                    <v-btn :disabled="$state.isLoading || !isButtonEnabled" color="primary" @click="createNewLoan">
                        <template v-if="$state.isLoading">
                            <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                        </template>

                        <template v-else>
                            Cadastrar
                        </template>
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-container>
    </v-dialog>
</template>

<script setup>
import { reactive, computed, onMounted } from "vue";
import { WorksServices, ExemplaryServices, CustomerServices, LoanServices } from '@/services';
import { WORKS_TYPES } from '@/constants'
import { getDateIsoFormat } from '@/utils/date/get-date-iso-format'

onMounted(() => {
    requestAllWorks()
    requestAllUsers()
})

const $state = reactive({
    works: {},
    users: {},
    isLoading: false,
    isLoadingUsers: false,
    isLoadingWorks: false,
    isOpen: false,
    selectedWork: null,
    selectedClient: null,
    fromDate: null,
    toDate: null,
})

const isButtonEnabled = computed(() => {
    return true
})

const format = (date) => {
    let day = String(date.getDate());
    let month = String(date.getMonth() + 1);
    const year = date.getFullYear();

    month = month.length < 2 ? `0${month}` : month // add zero before
    day = day.length < 2 ? `0${day}` : day // add zero before

    return `${day}/${month}/${year}`;
}

const getWorkTitles = () => {
    return $state.works.map((work) => work.title)
}

const getCustomerNames = () => {
    return $state.users.map((customer) => `${customer.first_name} ${customer.last_name} - ${customer.email}`)
}

const requestAllWorks = async () => {
    $state.isLoadingWorks = true;

    WorksServices.getAllWorks()
        .then(({ works }) => {
            $state.works = works;
        })
        .finally(() => {
            $state.isLoadingWorks = false;
        });
}

const requestAllUsers = async () => {
    $state.isLoadingUsers = true;

    CustomerServices.getAllCustomers()
        .then(({ customers }) => {
            $state.users = customers.filter((customer) => customer.is_active === true)
        })
        .finally(() => {
            $state.isLoadingUsers = false;
        });
}


const createNewLoan = () => {
    const fromDate = $state.fromDate
    const toDate = $state.toDate
    const selectedWorkId = $state.works.filter((work) => work.title == $state.selectedWork)[0].id
    const selectedUserEmail = $state.selectedClient.split("-")[1].trim()

    const selectedClientId = $state.users.filter((user) => user.email == selectedUserEmail)[0].id

    const payload = {
        "work_id": selectedWorkId,
        "customer_id": selectedClientId,
        "start_date": getDateIsoFormat(fromDate),
        "end_date": getDateIsoFormat(toDate)
    }

    LoanServices.newLoan(payload)
        .then(() => {
            $emit('snackBar', {
                "title": "Empréstimo realizado com sucesso!",
                "type": "success"
            });

            $state.isOpen = false;
        })
        .catch((error) => {
            $emit('snackBar', {
                "title": error,
                "type": "error"
            });
        })
        .finally(() => {
            console.log("Terminou")
        })
}

const $emit = defineEmits(['snackBar']);
</script>