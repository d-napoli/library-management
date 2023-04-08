import { httpClient } from "./http-client";

const getAllAuthors = () => httpClient.get("authors/")

const newAuthor = (params) => httpClient.post("author/add", params)

const updateAuthor = (author_id, params) => httpClient.patch(`author/${author_id}/update`, params)

const AuthorAPI = {
    getAllAuthors,
    newAuthor,
    updateAuthor
}

export { AuthorAPI };