<template>
    <v-dialog v-model="$state.isOpen" width="800">
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props">
                <v-icon>mdi-plus</v-icon>&nbsp;
                Novo exemplar
            </v-btn>
        </template>

        <v-container>
            <v-card class="pl-5 pr-5">
                <v-card-title class="pt-10">
                    <span class="text-h4">
                        Novo exemplar
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

                                    <v-combobox v-else v-model="$state.work" label="Obra"
                                        :items="$state.worksNamesList"></v-combobox>
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

                    <v-btn :disabled="$state.isLoading || !isButtonEnabled" color="primary" @click="addNewExemplary">
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
import { WorksServices, ExemplaryServices } from '@/services';
import { WORKS_TYPES } from '@/constants'

onMounted(() => {
    requestAllWorks()
})

const requestAllWorks = async () => {
    $state.isLoading = true;

    WorksServices.getAllWorks()
        .then(({ works }) => {
            works.forEach(work => {
                $state.works[work.title] = work.id
                $state.worksNamesList.push(work.title)
            });
        })
        .finally(() => {
            $state.isLoading = false;
        });
}

const addNewExemplary = () => {
    $state.isLoading = true

    let payload = {
        "work_id": $state.works[$state.work],
    }

    ExemplaryServices.newExemplary(payload)
        .then(() => {
            $emit('snackBar', {
                "title": `Exemplar ${$state.work} cadastrado com sucesso`,
                "type": "success"
            });

            $state.isOpen = false
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

const $state = reactive({
    worksNamesList: [],
    works: {},
    isLoadingWorks: false,
    isLoading: false,
    isOpen: false,
    work: null
})

const isButtonEnabled = computed(() => {
    return $state.work?.length >= 3
})

const $emit = defineEmits(['snackBar']);
</script>