import { getAllCustomers } from "./get-all-customers";
import { inactivateCustomer } from "./inactivate-customer";
import { reactivateCustomer } from "./reactivate-customer";
import { newCustomer } from "./new-customer";
import { updateCustomer } from "./update-customer";

const CustomerServices = {
    getAllCustomers,
    inactivateCustomer,
    reactivateCustomer,
    newCustomer,
    updateCustomer
}

export { CustomerServices };