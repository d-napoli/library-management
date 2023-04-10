import { CustomerAPI } from "../../http-client";

const updateCustomer = async (customer_id, payload) => CustomerAPI.updateCustomer(customer_id, payload)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { updateCustomer };
