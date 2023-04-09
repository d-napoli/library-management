import { httpClient } from "./http-client";

const getAllExemplaries = () => httpClient.get("exemplaries/")

const newExemplary = (params) => httpClient.post("exemplary/add", params)

const inactivateExemplary = (exemplary_id) => httpClient.delete(`exemplary/${exemplary_id}/delete`)

const reactivateExemplary = (exemplary_id) => httpClient.patch(`exemplary/${exemplary_id}/reactivate`)

const ExemplaryAPI = {
    getAllExemplaries,
    newExemplary,
    inactivateExemplary,
    reactivateExemplary,
}

export { ExemplaryAPI };