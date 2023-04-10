import { LoanAPI } from "../../http-client";

const returnLoan = async (payload) => LoanAPI.returnLoan(payload)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { returnLoan };
