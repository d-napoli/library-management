<template>
    <v-table fixed-header hover>
        <thead>
            <tr>
                <template v-for="item in menuItems" :key="item">
                    <th class="text-left">{{ item }}</th>
                </template>
            </tr>
        </thead>

        <slot />
    </v-table>
</template>

<script setup>
const menuItems = [
    "ID",
    "Título",
    "Autor",
    "Tipo",
    "Dt. Início",
    "Dt. Fim",
    "Dt. Retorno",
    "Atrasado",
    "Multa",
    "Usuário",
    "E-mail Usuário",
    "Ações"
]
</script>