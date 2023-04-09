import { httpClient } from "./http-client";

const getAllLoans = () => httpClient.get("loans")

const LoanAPI = {
    getAllLoans,
}

export { LoanAPI };