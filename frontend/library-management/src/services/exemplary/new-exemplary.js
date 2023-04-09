import { ExemplaryAPI } from "../../http-client";

const newExemplary = async (params) => ExemplaryAPI.newExemplary(params)
    .then(({ data }) => {
        console.log("The data")
        return data
    })
    .catch((error) => Promise.reject(error.response.data.message));

export { newExemplary };
