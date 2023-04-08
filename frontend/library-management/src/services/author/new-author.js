import { AuthorAPI } from "../../http-client";

const newAuthor = async (params) => AuthorAPI.newAuthor(params)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { newAuthor };
