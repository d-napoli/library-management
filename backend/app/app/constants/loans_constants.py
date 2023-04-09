def get_fine_per_day():
    return 1


def wrong_payment_error(paid_value, expected_value):
    return f"Invalid amount paid. Expected {expected_value} - Received: {paid_value}"
