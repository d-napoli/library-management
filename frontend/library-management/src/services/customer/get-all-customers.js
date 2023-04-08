import { CustomerAPI } from "../../http-client";

const getAllCustomers = async () => CustomerAPI.getAllCustomers()
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response));

export { getAllCustomers };
