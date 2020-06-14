balance = 3926
annualInterestRate = 0.2
monthlyPayment = 0
first_balance = balance
while True:
    balance = first_balance
    monthlyPayment += 1
    for i in range (12):
        balance = balance - monthlyPayment
        monthinterest = balance * (annualInterestRate/12.0)
        balance = balance + monthinterest
    if balance <= 0:
        break
print("Lowest Payment: ", monthlyPayment)
