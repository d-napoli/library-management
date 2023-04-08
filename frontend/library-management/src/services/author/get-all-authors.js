import { AuthorAPI } from "../../http-client";

const getAllAuthors = async () => AuthorAPI.getAllAuthors()
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response));

export { getAllAuthors };
