import { getAllExemplaries } from "./get-all-exemplaries";
import { newExemplary } from "./new-exemplary";
import { reactivateExemplary } from "./reactivate-exemplary";
import { inactivateExemplary } from "./inactivate-exemplary";


const ExemplaryServices = {
    getAllExemplaries,
    newExemplary,
    inactivateExemplary,
    reactivateExemplary
}

export { ExemplaryServices };