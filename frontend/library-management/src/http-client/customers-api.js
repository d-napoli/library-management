import { httpClient } from "./http-client";

const getAllCustomers = () => httpClient.get("customers/")

const inactivateCustomer = (customer_id) => httpClient.delete(`customer/${customer_id}/delete`)

const reactivateCustomer = (customer_id) => httpClient.patch(`customer/${customer_id}/reactivate`)

const CustomerAPI = {
    getAllCustomers,
    inactivateCustomer,
    reactivateCustomer
}

export { CustomerAPI };