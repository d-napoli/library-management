import { httpClient } from "./http-client";

const getAllWorks = () => httpClient.get("works/")

const updateWork = (work_id, data) => httpClient.patch(`work/${work_id}/update`, data)

const newWork = (payload) => httpClient.post("work/add", payload)

const WorksAPI = {
    getAllWorks,
    updateWork,
    newWork
}

export { WorksAPI };