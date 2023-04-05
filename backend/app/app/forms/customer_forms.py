from typing import Optional

from pydantic import BaseModel


class UpdateCustomerForm(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
