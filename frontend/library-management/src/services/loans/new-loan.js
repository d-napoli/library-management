import { LoanAPI } from "../../http-client";

const newLoan = async (payload) => LoanAPI.newLoan(payload)
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { newLoan };
