import { httpClient } from "./http-client";

const getAllLoans = () => httpClient.get("loans")

const returnLoan = (payload) => httpClient.post("loans/return", payload)

const newLoan = (payload) => httpClient.post("loans/new", payload)

const LoanAPI = {
    getAllLoans,
    returnLoan,
    newLoan
}

export { LoanAPI };