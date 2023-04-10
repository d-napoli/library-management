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
                <v-btn variant="text" icon="mdi-menu-down" v-bind="props" />
            </template>

            <v-list>
                <v-list-item>
                    <v-dialog v-model="$state.isOpen" width="800">
                        <template v-slot:activator="{ props }">
                            <v-list-item-title v-bind="props">
                                <v-icon>{{ $props.customer.is_active ? "mdi-delete" : "mdi-check" }}</v-icon>
                                &nbsp;{{ $state.statusText }}
                            </v-list-item-title>
                        </template>

                        <v-container>
                            <v-card class="pl-5 pr-5">
                                <v-card-title class="pt-10">
                                    <span class="text-h4">
                                        {{ $state.statusText }} usuário <b>{{ customer.first_name }} {{ customer.last_name
                                        }}</b>?
                                    </span>
                                </v-card-title>

                                <v-card-actions class="pb-5">
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
    statusText: computed(() => !$props.customer.is_active ? "Ativar" : "Inativar"),
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
    let method = $props.customer.is_active ? CustomerServices.inactivateCustomer : CustomerServices.reactivateCustomer
    let term = $props.customer.is_active ? "inativado" : "ativado"

    $state.isLoadingActionButton = true;
    method($props.customer.id)
        .then(({ }) => {
            $props.customer.is_active = false
            $state.isOpen = false;

            $emit('snackBar', {
                "title": `Usuário ${$props.customer.first_name} ${term} com sucesso`,
                "type": "success"
            });
        })
        .catch(({ error }) => {
            $emit('snackBar', {
                "title": error,
                "type": "danger"
            });
        })
        .finally(() => {
            $state.isLoadingActionButton = false;
        })
}

const $emit = defineEmits(['snackBar']);
</script>