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
                            &nbsp;Atualizar
                        </v-list-item-title>
                    </template>

                    <v-container>
                        <v-card class="pl-5 pr-5">
                            <v-card-title class="pt-10">
                                <span class="text-h4" :title="$props.work.title">
                                    Atualizar obra {{ $props.work.title }}
                                </span>
                            </v-card-title>

                            <v-card-text>
                                <v-form v-model="valid">
                                    <v-container>
                                        <v-row>
                                            <v-col cols="12" md="6">
                                                <v-text-field v-model="$state.newTitle" label="Novo título"
                                                    required></v-text-field>
                                            </v-col>

                                            <v-col cols="12" md="6">
                                                <template v-if="$state.isLoadingAuthors">
                                                    <v-progress-circular size="25" indeterminate
                                                        color="primary"></v-progress-circular>
                                                </template>

                                                <v-combobox v-else v-model="$state.newAuthor" label="Novo Autor"
                                                    :items="$state.authorsList"></v-combobox>
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

                                <v-btn :disabled="$state.isLoading || !isButtonEnabled" color="primary"
                                    @click="updateAuthor">
                                    <template v-if="$state.isLoading">
                                        <v-progress-circular size="25" indeterminate color="primary"></v-progress-circular>
                                    </template>

                                    <template v-else>
                                        Sim, atualizar
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
import { onMounted, reactive, computed } from 'vue'
import { AuthorServices, WorksServices } from '@/services';

const $props = defineProps({
    work: {
        type: Object,
        required: true
    },
})

const isButtonEnabled = computed(() => {
    return $state.newAuthor?.length >= 3 && $state.newTitle?.length >= 3
})

onMounted(() => {
    requestAllAuthors()
})

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

const updateAuthor = () => {
    let payload = {
        "title": $state.newTitle,
        "author_name": $state.newAuthor
    }

    $state.isLoading = true

    WorksServices.updateWork($props.work.id, payload)
        .then(() => {
            console.log("Atualizado")

            $emit('snackBar', {
                "title": `Obra ${$state.newTitle} editada com sucesso!`,
                "type": "success"
            });
        })
        .catch(({ error }) => {
            console.log("Deu erro")
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

const $state = reactive({
    isLoading: false,
    isLoadingAuthors: false,
    isOpen: false,
    newTitle: $props.work.title,
    newAuthor: $props.work.author,
    authorsList: []
})

const $emit = defineEmits(['snackBar']);
</script>