import { WorksAPI } from "../../http-client";

const newWork = async (payload) => WorksAPI.newWork(payload)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { newWork };
