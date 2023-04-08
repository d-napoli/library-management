import { getAllCustomers } from "./get-all-customers";
import { inactivateCustomer } from "./inactivate-customer";
import { reactivateCustomer } from "./reactivate-customer";

const CustomerServices = {
    getAllCustomers,
    inactivateCustomer,
    reactivateCustomer
}

export { CustomerServices };