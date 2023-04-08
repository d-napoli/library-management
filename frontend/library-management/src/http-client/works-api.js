import { httpClient } from "./http-client";

const getAllWorks = () => httpClient.get("works/")

const updateWork = (work_id, data) => httpClient.patch(`work/${work_id}/update`, data)

const WorksAPI = {
    getAllWorks,
    updateWork
}

export { WorksAPI };