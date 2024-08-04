sales_amount = float(input("Enter the sales amount: "))

if sales_amount >= 60000:
    commission = sales_amount * 0.10
elif sales_amount >= 40000:
    commission = sales_amount * 0.05
else:
    commission = 0

print(f"The commission based on sales of {sales_amount} is {commission}")
