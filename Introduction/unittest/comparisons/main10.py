def should_serve_customer(customer_age, on_break, time):
    return customer_age >= 21 and not on_break and 5 <= time <= 10

