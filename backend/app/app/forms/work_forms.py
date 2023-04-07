from typing import Optional

from pydantic import BaseModel


class AddWorkForm(BaseModel):
    title: str
    author_name: str
    type: str


class UpdateWorkForm(BaseModel):
    title: Optional[str]
    author_name: Optional[str]
    type: Optional[str]
