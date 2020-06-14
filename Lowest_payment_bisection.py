balance = 320000
annualInterestRate = 0.2
first_balance = balance
lower_bound = balance/12
upper_bound = (balance * ((1 + (annualInterestRate/12))**12))/12
while True:
    balance = first_balance
    monthlyPayment = (upper_bound + lower_bound)/2
    for i in range (12):
        balance = balance - monthlyPayment
        monthinterest = balance * (annualInterestRate/12.0)
        balance = balance + monthinterest
    if balance <= 0 and balance >= -0.1:
        break
    elif balance > 0:
        lower_bound = monthlyPayment
    else:
        upper_bound = monthlyPayment
print("Lowest Payment: ", round(monthlyPayment, 2))
