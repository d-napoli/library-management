import { ExemplaryAPI } from "../../http-client";

const getAllExemplaries = async () => ExemplaryAPI.getAllExemplaries()
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { getAllExemplaries };
