import { CustomerAPI } from "../../http-client";

const inactivateCustomer = async (customer_id) => CustomerAPI.inactivateCustomer(customer_id)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { inactivateCustomer };
