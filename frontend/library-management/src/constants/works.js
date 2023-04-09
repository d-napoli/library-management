const WORKS_TYPES = {
    "book": {
        "name": "Livro",
        "color": "primary"
    },
    "newspaper": {
        "name": "Jornal",
        "color": "secondary",
    },
    "magazine": {
        "name": "Revista",
        "color": "info"
    }
}

const getBookType = (bookType) => {
    return WORKS_TYPES[bookType]["name"]
}

const getBookTypeColor = (bookType) => {
    return WORKS_TYPES[bookType]["color"]
}

export {
    WORKS_TYPES,
    getBookType,
    getBookTypeColor
}