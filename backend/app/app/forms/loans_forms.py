from typing import Optional

from pydantic import BaseModel


class CanUserLoanForm(BaseModel):
    customer_id: int


class ReturnLoanForm(BaseModel):
    loan_id: int
    payment_amount: Optional[int]
