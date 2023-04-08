import { AuthorAPI } from "../../http-client";

const getAllAuthors = async () => AuthorAPI.getAllAuthors()
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { getAllAuthors };
