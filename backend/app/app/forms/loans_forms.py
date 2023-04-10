from typing import Optional

from pydantic import BaseModel


class CanUserLoanForm(BaseModel):
    customer_id: int


class ReturnLoanForm(BaseModel):
    loan_id: int
    payment_amount: Optional[int]


class NewLoanForm(BaseModel):
    start_date: str
    end_date: str
    customer_id: int
    work_id: int
    loan_blocked_by_teacher: Optional[bool]
