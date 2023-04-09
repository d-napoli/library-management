<template>
    <v-dialog v-model="$state.isOpen" width="800">
        <template v-slot:activator="{ props }">
            <v-btn v-bind="props">
                <v-icon>mdi-plus</v-icon>&nbsp;
                Nova obra
            </v-btn>
        </template>

        <v-container>
            <v-card class="pl-5 pr-5">
                <v-card-title class="pt-10">
                    <span class="text-h4">
                        Nova obra
                    </span>
                </v-card-title>

                <v-card-text>
                    <v-form v-model="valid">
                        <v-container>
                            <v-row>
                                <v-col cols="12" md="6">
                                    <v-text-field v-model="$state.title" label="Novo título" required></v-text-field>
                                </v-col>

                                <v-col cols="12" md="6">
                                    <template v-if="$state.isLoadingAuthors">
                                        <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                                    </template>

                                    <v-combobox v-else v-model="$state.authorName" label="Autor"
                                        :items="$state.authorsList"></v-combobox>
                                </v-col>

                                <v-col cols="12" md="6">
                                    <v-combobox v-model="$state.type" label="Tipo da Obra"
                                        :items="getWorkTypes()"></v-combobox>
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

                    <v-btn :disabled="$state.isLoading || !isButtonEnabled" color="primary" @click="addNewWork">
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
import { AuthorServices, WorksServices } from '@/services';
import { WORKS_TYPES } from '@/constants'

onMounted(() => {
    requestAllAuthors()
})

const getWorkTypes = () => {
    let returnArray = []

    for (let type in WORKS_TYPES) {
        let typeKey = WORKS_TYPES[type].name
        let typeValue = type

        $state.invertedWorkTypes[typeKey] = typeValue

        returnArray.push(typeKey)
    }

    return returnArray
}

const requestAllAuthors = async () => {
    $state.isLoadingAuthors = true;

    AuthorServices.getAllAuthors()
        .then(({ authors }) => {
            authors.forEach(author => {
                $state.authorsList.push(author.name)
            });
        })
        .catch(({ error }) => {
            console.log(error)
        })
        .finally(() => {
            $state.isLoadingAuthors = false;
        })
}

const addNewWork = () => {
    $state.isLoading = true

    let payload = {
        "title": $state.title,
        "type": $state.invertedWorkTypes[$state.type],
        "author_name": $state.authorName
    }

    WorksServices.newWork(payload)
        .then(() => {
            $emit('snackBar', {
                "title": `Livro ${$state.title} cadastrado com sucesso`,
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
    authorsList: [],
    invertedWorkTypes: {},
    isLoadingAuthors: false,
    isLoading: false,
    isOpen: false,
    authorName: null,
    title: null,
    type: null
})

const isButtonEnabled = computed(() => {
    return $state.authorName?.length >= 3 && $state.title?.length >= 3 && $state.type?.length >= 3
})

const $emit = defineEmits(['snackBar']);
</script>