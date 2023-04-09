const getDate = (date) => {
    let parsedDate = date;
    if (!parsedDate) return undefined;
  
    return new Date(parsedDate).toLocaleDateString('pt-br');
  };
  
  export { getDate };
