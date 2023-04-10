import { getAllLoans } from "./get-all-loans";
import { returnLoan } from "./return-loan";
import { newLoan } from "./new-loan";

const LoanServices = {
    getAllLoans,
    returnLoan,
    newLoan
}

export { LoanServices };