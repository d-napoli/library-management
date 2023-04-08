<template>
    <td>{{ customer.id }}</td>

    <td>{{ customer.first_name }} {{ customer.last_name }}</td>

    <td>{{ customer.email }}</td>

    <td>
        <v-chip :color="customer.type == 'student' ? 'primary' : 'secondary'">
            {{ customer.type == 'student' ? 'Estudante' : 'Professor' }}
        </v-chip>
    </td>

    <td>
        <v-chip :color="customer.is_active ? 'green' : 'red'">
            {{ customer.is_active ? 'Ativo' : 'Inativo' }}
        </v-chip>
    </td>

    <td>
        <v-menu>
            <template v-slot:activator="{ props }">
                <v-btn v-bind="props">
                    <v-icon>mdi-menu-down</v-icon>
                </v-btn>
            </template>

            <v-list>
                <v-list-item>
                    <v-dialog v-model="$state.isOpen" width="800">
                        <template v-slot:activator="{ props }">
                            <v-list-item-title v-bind="props">
                                <v-icon>mdi-delete</v-icon>
                                &nbsp;{{ $state.statusText }}
                            </v-list-item-title>
                        </template>

                        <v-container>
                            <v-card>
                                <v-card-title>
                                    <span class="text-h4">
                                        {{ $state.statusText }} usuário <b>{{ customer.first_name }} {{ customer.last_name
                                        }}</b>?
                                    </span>
                                </v-card-title>

                                <v-card-actions>
                                    <v-spacer></v-spacer>

                                    <v-btn color="red" flat variant="text" @click="$state.isOpen = !$state.isOpen">
                                        Cancelar
                                    </v-btn>

                                    <v-btn color="primary" @click="handleAction">
                                        Sim, {{ $state.statusText }}
                                    </v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-container>
                    </v-dialog>
                </v-list-item>
            </v-list>
        </v-menu>
    </td>


    <v-snackbar v-model="$alertState.isActive" :color="$alertState.type" variant="tonal" :timeout="2000">
        {{ $alertState.text }}

        <template v-slot:actions>
            <v-btn :color="$alertState.type" variant="text" @click="handleAlertClick">
                Fechar
            </v-btn>
        </template>
    </v-snackbar>
</template>

<script setup>
import { CustomerServices } from '@/services';
import { reactive, computed, watch } from 'vue';

const $props = defineProps({
    customer: {
        type: Object,
        default: null,
    }
})

const $state = reactive({
    isOpen: false,
    isLoadingActionButton: false,
    statusText: computed(() => !$props.customer.is_active ? "ativar" : "inativar"),
});

const $alertState = reactive({
    isActive: false,
    text: null,
    type: "info",
    duration: 1000
})

const handleAlertClick = () => {
    $alertState.isActive = !$alertState.isActive
}

const handleAction = () => {
    $props.customer.is_active ? handleConfirmInactive() : handleConfirmReactivate();
}

const handleConfirmInactive = async () => {
    $state.isLoadingActionButton = true;
    CustomerServices.inactivateCustomer($props.customer.id)
        .then(({ }) => {
            $props.customer.is_active = false
            $state.isOpen = false;

            $alertState.text = `Usuário ${$props.customer.first_name} inativado com sucesso`
            $alertState.type = "success"
            $alertState.isActive = true
        })
        .catch(({ error }) => {
            $alertState.text = `Erro: ${error}`
            $alertState.type = "danger"
            $alertState.isActive = true
        })
        .finally(() => {
            $state.isLoadingActionButton = false;
        })
}

const handleConfirmReactivate = async () => {
    $state.isLoadingActionButton = true;

    CustomerServices.reactivateCustomer($props.customer.id)
        .then(({ }) => {
            $props.customer.is_active = true
            $state.isOpen = false;

            $alertState.text = `Usuário ${$props.customer.first_name} reativado com sucesso`
            $alertState.type = "success"
            $alertState.isActive = true
        })
        .catch(({ error }) => {
            $alertState.text = `Erro: ${error}`
            $alertState.type = "danger"
            $alertState.isActive = true
        })
        .finally(() => {
            $state.isLoadingActionButton = false;
        })
}
</script>