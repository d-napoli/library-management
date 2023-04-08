import { httpClient } from "./http-client";

const getAllAuthors = () => httpClient.get("authors/")

const AuthorAPI = {
    getAllAuthors,
}

export { AuthorAPI };