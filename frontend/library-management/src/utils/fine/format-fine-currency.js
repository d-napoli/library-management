const formatFineCurrency = (fine) => {
    let floatFine = parseFloat(fine).toFixed(2)
    return `R$ ${floatFine}`
}

export { formatFineCurrency }