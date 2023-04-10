<template>
    <v-dialog v-model="$state.isOpen" width="800">
        <template v-slot:activator="{ props }">
            <v-list-item-title v-bind="props">
                <v-icon>mdi-pencil</v-icon>
                &nbsp;Editar
            </v-list-item-title>
        </template>

        <v-container>
            <v-card class="pl-5 pr-5">
                <v-card-title class="pt-10">
                    <span class="text-h4">
                        Editar usuário <b>{{ customer.first_name }} {{ customer.last_name
                        }}</b>?
                    </span>
                </v-card-title>

                <v-card-text>
                    <v-form v-model="valid">
                        <v-container>
                            <v-row>
                                <v-col cols="12" md="6">
                                    <v-text-field label="Nome" v-model="$state.newFirstName" :items="[]" />
                                </v-col>

                                <v-col cols="12" md="6">
                                    <v-text-field label="Sobrenome" v-model="$state.newLastName" :items="[]" />
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12" md="12">
                                    <v-text-field label="Email" v-model="$state.newEmail" />
                                </v-col>
                            </v-row>

                            <v-row>
                                <v-col cols="12" md="12">
                                    <v-autocomplete label="Obra" v-model="$state.newUserType"
                                        :items="['Professor', 'Estudante']"></v-autocomplete>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-form>
                </v-card-text>

                <v-card-actions class="pb-5">
                    <v-spacer></v-spacer>

                    <v-btn color="red" flat variant="text" @click="$state.isOpen = !$state.isOpen">
                        Cancelar
                    </v-btn>

                    <v-btn color="primary" @click="handleAction">
                        <template v-if="$state.isLoadingActionButton">
                            <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                        </template>

                        <template v-else>
                            Sim, editar
                        </template>
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-container>
    </v-dialog>
</template>

<script setup>
import { reactive, computed, watch, onMounted } from 'vue';
import { CustomerServices } from '@/services';

const $state = reactive({
    isOpen: false,
    isLoadingActionButton: false,
    newFirstName: null,
    newLastName: null,
    newEmail: null,
    newUserType: null
});

const $props = defineProps({
    customer: {
        type: Object,
        default: null,
    }
})

onMounted(() => {
    $state.newFirstName = $props.customer.first_name
    $state.newLastName = $props.customer.last_name
    $state.newEmail = $props.customer.email
    $state.newUserType = $props.customer.type == "student" ? "Estudante" : "Professor"
})

const constructPayload = () => {
    let payload = {}

    if ($state.newFirstName !== $props.customer.first_name) payload["first_name"] = $state.newFirstName
    if ($state.newLastName !== $props.customer.last_name) payload["last_name"] = $state.newLastName
    if ($state.newEmail !== $props.customer.email) payload["email"] = $state.newEmail

    let userType = $state.newUserType == "Estudante" ? "student" : "teacher"

    if (userType !== $props.customer.type) payload["user_type"] = userType

    return payload
}

const handleAction = () => {
    $state.isLoadingActionButton = true

    let payload = constructPayload()
    let customerId = $props.customer.id

    CustomerServices.updateCustomer(customerId, payload)
        .then(() => {
            $emit('snackBar', {
                "title": "Usuário editado com sucesso!",
                "type": "success"
            });

            $state.isOpen = false
        })
        .catch((error) => {
            $emit('snackBar', {
                "title": error,
                "type": "error"
            });
        })
        .finally(() => {
            console.log("Terminou")
            $state.isLoadingActionButton = false
        })
}

const $emit = defineEmits(['snackBar']);
</script>
