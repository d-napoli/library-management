import { CustomerAPI } from "../../http-client";

const newCustomer = async (params) => CustomerAPI.newCustomer(params)
    .then(({ data }) => {
        console.log("The data")
        return data
    })
    .catch((error) => Promise.reject(error.response.data.message));

export { newCustomer };
