from pydantic import BaseModel


class BaseAuthorForm(BaseModel):
    name: str
