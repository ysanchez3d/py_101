# monthly_payment = 250
loan_amount = 10000
loan_duration_in_months = 24
interest_rate_monthly = 0.10 / 12

def calculate_monthly_payment(loan_amount, interest_rate_monthly, loan_duration_in_months):
    return round(loan_amount * (interest_rate_monthly / (1 - (1 + interest_rate_monthly) ** (-loan_duration_in_months))), 2)

print(calculate_monthly_payment(loan_amount, interest_rate_monthly, loan_duration_in_months))