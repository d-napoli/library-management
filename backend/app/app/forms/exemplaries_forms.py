from typing import Optional

from pydantic import BaseModel


class AddExemplaryForm(BaseModel):
    work_id: int
