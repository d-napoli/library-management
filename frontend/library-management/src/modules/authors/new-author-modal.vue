<template>
    <v-dialog v-model="$state.isOpen" width="800">
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props">
                <v-icon>mdi-plus</v-icon>&nbsp;
                Novo autor
            </v-btn>
        </template>

        <v-container>
            <v-card class="pl-5 pr-5">
                <v-card-title class="pt-10">
                    <span class="text-h4">
                        Novo autor
                    </span>
                </v-card-title>

                <v-card-text>
                    <v-form v-model="valid">
                        <v-container>
                            <v-row>
                                <v-col cols="12" md="12">
                                    <v-text-field v-model="$state.name" label="Nome" required></v-text-field>
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

                    <v-btn :disabled="$state.isLoading || !isButtonEnabled" color="primary" @click="addNewCustomer">
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
import { reactive, computed } from "vue";
import { AuthorServices } from '@/services';

const $state = reactive({
    isLoading: false,
    isOpen: false,
    name: null,
})

const isButtonEnabled = computed(() => {
    return $state.name?.length >= 3
})

const addNewCustomer = async () => {
    $state.isLoading = true;

    let payload = {
        "name": $state.name,
    }

    AuthorServices.newAuthor(payload)
        .then(() => {
            $state.isOpen = false;

            $emit('snackBar', {
                "title": `Usuario ${$state.name} cadastrado com sucesso!`,
                "type": "success"
            });
        })
        .catch((error) => {
            $emit('snackBar', {
                "title": error,
                "type": "error"
            });
        })
        .finally(() => {
            $state.isLoading = false;
        })
}

const $emit = defineEmits(['snackBar']);
</script>