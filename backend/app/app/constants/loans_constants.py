def get_fine_per_day():
    return 1


def wrong_payment_error(paid_value, expected_value):
    return f"Invalid amount paid. Expected {expected_value} - Received: {paid_value}"


def wrong_start_end_dates_error():
    return "Start or end dates incorrect"


def loan_blocked_by_teacher_error(teacher_name):
    return f"Loan blocked by teacher '{teacher_name}'"
