def customer_exists_error(email: str) -> str:
    return f"Customer with email '{email}' already exists!"


def customer_not_found_error(id: str) -> str:
    return f"Customer with id '{str(id)}' not found"


def customer_cant_loan_error(customer) -> str:
    return f"Customer {customer.first_name} {customer.last_name} can't loan"
