<template>
    <td>{{ $props.loan.id }}</td>

    <td>{{ $props.loan.exemplary.title }}</td>

    <td>{{ $props.loan.exemplary.author }}</td>

    <td>
        <v-chip :color="getBookTypeColor($props.loan.exemplary.type)">
            {{ getBookType($props.loan.exemplary.type) }}
        </v-chip>
    </td>

    <td>{{ $props.loan.exemplary.id }}</td>

    <td>{{ getDate($props.loan.start_date) }}</td>

    <td>{{ getDate($props.loan.end_date) }}</td>

    <td>{{ getDate($props.loan.return_date) }}</td>

    <td>
        <v-chip :color="getIsLateColor($props.loan.is_devolution_late)">
            {{ getIsLateText($props.loan.is_devolution_late) }}
        </v-chip>
    </td>

    <td>
        <p :class="getFineColor($props.loan.fine)">{{ formatFineCurrency($props.loan.fine) }}</p>
    </td>

    <td>{{ formatUserInfo($props.loan.customer.first_name, $props.loan.customer.last_name) }}</td>

    <td>{{ formatUserEmail($props.loan.customer.email) }}</td>

    <td>
        <slot />
    </td>
</template>

<script setup>
import { getBookType, getBookTypeColor, getStatusColor, getStatusText } from '@/constants'
import { getDate } from '@/utils/date/get-date'
import { formatFineCurrency } from '@/utils/fine/format-fine-currency'

const getIsLateColor = (isLate) => {
    return isLate ? "success" : "red"
}

const getIsLateText = (isLate) => {
    return isLate ? "Sim" : "Não"
}

const formatUserInfo = (firstName, lastName) => {
    return `${firstName} ${lastName}`
}

const formatUserEmail = (userEmail) => {
    return `<${userEmail}>`
}

const getFineColor = (fine) => {
    return fine > 0 ? "text-red-lighten-1" : "black"
}

const $props = defineProps({
    loan: {
        type: Object,
        required: true
    }
})
</script>