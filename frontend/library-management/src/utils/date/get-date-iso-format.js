const getDateIsoFormat = (date) => {
    if (!date) return undefined;
    return new Date(date).toISOString().split('T')[0];
};

export { getDateIsoFormat }
