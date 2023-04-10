<template>
    <v-menu>
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props" icon="mdi-menu-down" variant="text" />
        </template>

        <v-list>
            <v-list-item v-if="$props.loan.return_date == null">
                <v-dialog v-model="$state.isOpen" width="800">
                    <template v-slot:activator="{ props }">
                        <v-list-item-title v-bind="props">
                            <v-icon>mdi-keyboard-return</v-icon>
                            &nbsp;Cadastrar retorno
                        </v-list-item-title>
                    </template>

                    <v-container>
                        <v-card class="pl-5 pr-5">
                            <v-card-title class="pt-10">
                                <span class="text-h4" :title="$props.loan.title">
                                    Retornar empréstimo?
                                </span>
                            </v-card-title>

                            <template v-if="$props.loan.is_devolution_late">
                                <v-card-text>
                                    <span class="text-h6">O empréstimo estava atrasado
                                        <v-icon>
                                            {{ $state.paidFine ? 'mdi-emoticon-happy' : 'mdi-emoticon-sad' }}
                                        </v-icon>
                                    </span>
                                    <v-checkbox v-model="$state.paidFine" :label="getCheckboxLabel()"></v-checkbox>
                                </v-card-text>
                            </template>

                            <v-card-actions class="pb-5">
                                <v-spacer></v-spacer>

                                <v-btn color="red" flat variant="text" @click="$state.isOpen = false">
                                    Cancelar
                                </v-btn>

                                <v-btn :disabled="!isButtonEnabled()" color="primary" @click="handleAction()">
                                    <template v-if="$state.isLoading">
                                        <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                                    </template>

                                    <template v-else>
                                        Sim, retornar
                                    </template>
                                </v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-container>
                </v-dialog>
            </v-list-item>
        </v-list>
    </v-menu>
</template>

<script setup>
import { reactive } from 'vue'
import { LoanServices } from '@/services';
import { formatFineCurrency } from '@/utils/fine/format-fine-currency'

const handleAction = (status) => {
    $state.isLoading = true

    let loanId = $props.loan.id
    let paymentAmount = $props.loan.fine

    let payload = {
        "loan_id": loanId,
        "payment_amount": paymentAmount
    }

    LoanServices.returnLoan(payload)
        .then(() => {
            $emit('snackBar', {
                "title": "Exemplar retornado com sucesso",
                "type": "success"
            });
        })
        .catch((error) => {
            console.log(error)
            $emit('snackBar', {
                "title": error,
                "type": "error"
            });
        })
        .finally(() => {
            $state.isLoading = false
        })
}

const isButtonEnabled = () => {
    let wasLate = $props.loan.is_devolution_late

    return wasLate ? $state.paidFine && !$state.isLoading : !$state.isLoading
}

const getCheckboxLabel = () => {
    return `Usuário pagou a multa (${formatFineCurrency($props.loan.fine)})`
}

const $props = defineProps({
    loan: {
        type: Object,
        required: true
    },
})

const $state = reactive({
    isLoading: false,
    isOpen: false,
    paidFine: false
})

const $emit = defineEmits(['snackBar']);
</script>
