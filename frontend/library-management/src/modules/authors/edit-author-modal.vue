<template>
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
                            <v-icon>mdi-pencil</v-icon>
                            &nbsp;Editar
                        </v-list-item-title>
                    </template>

                    <v-container>
                        <v-card class="pl-5 pr-5">
                            <v-card-title class="pt-10">
                                <span class="text-h4">
                                    Editar autor <b>{{ author.name }}</b>?
                                </span>
                            </v-card-title>

                            <v-card-text>
                                <v-card-text>
                                    <v-form v-model="valid">
                                        <v-container>
                                            <v-row>
                                                <v-col cols="12" md="12">
                                                    <v-text-field v-model="$state.newName" label="Nome"
                                                        required></v-text-field>
                                                </v-col>
                                            </v-row>
                                        </v-container>
                                    </v-form>
                                </v-card-text>
                            </v-card-text>

                            <v-card-actions class="pb-5">
                                <v-spacer></v-spacer>

                                <v-btn color="red" flat variant="text" @click="$state.isOpen = !$state.isOpen">
                                    Cancelar
                                </v-btn>

                                <v-btn :disabled="$state.isLoading || !isButtonEnabled" color="primary" @click="editAuthor">
                                    <template v-if="$state.isLoading">
                                        <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                                    </template>

                                    <template v-else>
                                        Editar
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
import { reactive, computed } from "vue"
import { AuthorServices } from '@/services';

const $state = reactive({
    isOpen: false,
    isLoading: false,
    newName: null
})

const isButtonEnabled = computed(() => {
    return $state.newName?.length >= 3
})

const $props = defineProps({
    author: {
        type: Object,
        required: true
    }
})

const editAuthor = () => {
    $state.isLoading = true;

    let payload = {
        "name": $state.newName,
    }

    AuthorServices.updateAuthor($props.author.id, payload)
        .then(() => {
            $state.isOpen = false;

            $emit('snackBar', {
                "title": `Usuario ${$state.newName} editado com sucesso!`,
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