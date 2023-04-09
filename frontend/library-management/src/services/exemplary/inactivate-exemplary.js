import { ExemplaryAPI } from "../../http-client";

const inactivateExemplary = async (params) => ExemplaryAPI.inactivateExemplary(params)
    .then(({ data }) => {
        return data
    })
    .catch((error) => Promise.reject(error.response.data.message));

export { inactivateExemplary };
