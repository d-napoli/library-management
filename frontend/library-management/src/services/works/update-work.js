import { WorksAPI } from "../../http-client";

const updateWork = async (work_id, data) => WorksAPI.updateWork(work_id, data)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { updateWork };
