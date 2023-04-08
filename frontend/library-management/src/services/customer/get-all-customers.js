import { CustomerAPI } from "../../http-client";

const getAllCustomers = async () => CustomerAPI.getAllCustomers()
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { getAllCustomers };
