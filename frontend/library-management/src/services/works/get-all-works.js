import { WorksAPI } from "../../http-client";

const getAllWorks = async () => WorksAPI.getAllWorks()
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { getAllWorks };
