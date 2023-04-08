import { AuthorAPI } from "../../http-client";

const updateAuthor = async (author_id, params) => AuthorAPI.updateAuthor(author_id, params)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { updateAuthor };
