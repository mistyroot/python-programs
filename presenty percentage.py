#total no of working and absent days, if percentage<75% then not eligible to sit exam
w_days=int(input("Total no of working days"))
a_days=int(input("Total no of absent days"))
p=((w_days-a_days)/(w_days))*100
if p<75:
    print("not eligible to sit exam")
else:
    print("eligible to sit exam")
