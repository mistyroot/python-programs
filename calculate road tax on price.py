# Cost:   >100000    15%
#         >50000      10%
#         <=50000     5%    
cost=float(input("Bike cost"))
if cost >100000:
    tax=cost*15/100
elif cost>50000 and cost<=100000:
    tax= cost*10/100
else:
    tax=cost*5/100

print(f"road tax{tax}")