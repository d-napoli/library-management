import { LoanAPI } from "../../http-client";

const getAllLoans = async () => LoanAPI.getAllLoans()
    .then(({ data }) => data)
    .catch((error) => Promise.reject(error.response.data.message));

export { getAllLoans };
