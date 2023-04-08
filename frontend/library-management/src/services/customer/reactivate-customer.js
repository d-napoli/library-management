import { CustomerAPI } from "../../http-client";

const reactivateCustomer = async (customer_id) => CustomerAPI.reactivateCustomer(customer_id)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response));

export { reactivateCustomer };
