# >10 year service  ...........10% bonus
# 10>=servive >6 years     ........8% bonus
# service <6 years    ........5% bonus

salary= float (input("Enter salary"))
service= int(input("Enter service years"))
if service >10:
    bonus=salary*10/100
elif 10 >= service > 6:
    bonus=salary*8/100
elif service <6:
    bonus=salary*5/100

print(f"bonus is{bonus}")
print(f"net bonus is{bonus+salary}")
