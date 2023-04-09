const getStatusText = (status) => {
    return status ? "Ativo" : "Inativo"
}

const getStatusColor = (status) => {
    return status ? "primary" : "red"
}

export {
    getStatusColor,
    getStatusText
}