import { ExemplaryAPI } from "../../http-client";

const reactivateExemplary = async (params) => ExemplaryAPI.reactivateExemplary(params)
    .then(({ data }) => {
        return data
    })
    .catch((error) => Promise.reject(error.response.data.message));

export { reactivateExemplary };
