import { httpClient } from "./http-client";

const getAllCustomers = () => httpClient.get("customers/")

const inactivateCustomer = (customer_id) => httpClient.delete(`customer/${customer_id}/delete`)

const reactivateCustomer = (customer_id) => httpClient.patch(`customer/${customer_id}/reactivate`)

const newCustomer = (params) => httpClient.post("customer/add", params)

const updateCustomer = (customer_id, payload) => httpClient.patch(`customer/${customer_id}/update`, payload)

const CustomerAPI = {
    getAllCustomers,
    inactivateCustomer,
    reactivateCustomer,
    newCustomer,
    updateCustomer
}

export { CustomerAPI };