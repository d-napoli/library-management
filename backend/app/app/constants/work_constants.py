def work_already_exists_error(title: str) -> str:
    return f"Work '{title}' already exists!"


def work_not_found_error(title) -> str:
    return f"Work '{title}' not found"


def work_not_found_by_id_error(id: int) -> str:
    return f"Work not found with the id '{id}'"
