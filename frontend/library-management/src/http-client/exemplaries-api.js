import { httpClient } from "./http-client";

const getAllExemplaries = () => httpClient.get("exemplaries/")

// const newExemplary = (params) => httpClient.post("exemplary/add", params)

// const UpdateExemplary = (exemplary_id, params) => httpClient.patch(`exemplary/${exemplary_id}/update`, params)

const ExemplaryAPI = {
    getAllExemplaries,
    // newExemplary,
    // UpdateExemplary
}

export { ExemplaryAPI };