<template>
    <v-menu>
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props" icon="mdi-menu-down" variant="text" />
        </template>

        <v-list>
            <v-list-item>
                <v-dialog v-model="$state.isOpen" width="800">
                    <template v-slot:activator="{ props }">
                        <v-list-item-title v-bind="props">
                            <v-icon>mdi-pencil</v-icon>
                            &nbsp;{{ getActionText($props.exemplary.active) }}
                        </v-list-item-title>
                    </template>

                    <v-container>
                        <v-card class="pl-5 pr-5">
                            <v-card-title class="pt-10">
                                <span class="text-h4" :title="$props.exemplary.title">
                                    {{ getActionText($props.exemplary.active) }} exemplar?
                                </span>

                                <p class="text">
                                    {{ $props.exemplary.title }}
                                </p>
                            </v-card-title>

                            <v-card-actions class="pb-5">
                                <v-spacer></v-spacer>

                                <v-btn color="red" flat variant="text" @click="$state.isOpen = false">
                                    Cancelar
                                </v-btn>

                                <v-btn :disabled="$state.isLoading" color="primary"
                                    @click="handleAction($props.exemplary.active)">
                                    <template v-if="$state.isLoading">
                                        <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                                    </template>

                                    <template v-else>
                                        Sim, {{ getActionText($props.exemplary.active) }}
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
import { ExemplaryServices } from '@/services';

const handleAction = (status) => {
    let method = status ? ExemplaryServices.inactivateExemplary : ExemplaryServices.reactivateExemplary
    let term = status ? "Inativado" : "Ativado"

    method($props.exemplary.id)
        .then(() => {
            $emit('snackBar', {
                "title": `Obra ${$props.exemplary.title} foi ${term.toLowerCase()} com sucesso!`,
                "type": "success"
            });
        })
        .catch(({ error }) => {
            $emit('snackBar', {
                "title": error,
                "type": "error"
            });
        })
        .finally(() => {
            $state.isLoading = false
        })
}


const getActionText = (status) => {
    return status ? "Inativar" : "Ativar"
}

const $props = defineProps({
    exemplary: {
        type: Object,
        required: true
    },
})

const $state = reactive({
    isLoading: false,
    isOpen: false,
})

const $emit = defineEmits(['snackBar']);
</script>
