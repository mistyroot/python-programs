
#write a program to calculate elecrticity bill based on units
#first 100 units free
#next 100 units > 100 rs per unit
#after 200 units > 10 rs per unit

# Input the number of units consumed
units = int(input("Enter units:"))

# Calculate the electricity bill
if units <= 100:
    amt = 0
elif 100< units < 200:
    amt = (units - 100) * 5
else:
    # For units greater than 200
    amt = 500 + (units - 200) * 10

# Display the total amount
print(f"Total amount: {amt} ")
