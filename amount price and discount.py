#calculate amount price and discount
# price>10000 20%
# 10000 >= price > 7000   15%
# price <=7000        10%

price=float(input("Enter price"))
if price>10000:
    discount=price*20/100
elif 10000>=price>7000:
    discount=price*15/100
else:
    discount=price*10/100
    
print(f"discount is {discount}")
print(f"Net amount is {price-discount}")
