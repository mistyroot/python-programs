name=input("Enter Name ")
n=int(input("Enter how many subjects ?"))

marks=[]
for i in range(n):
    s=int(input("Enter Marks "))
    marks.append(s)

total=0
for s in marks:
    total+=s

avg=total/n
result="pass"
for s in marks:
    if s<40:
        result="fail"
        break

print(f"{name}\t{marks}\t{total}\t{avg:.2f}\t{result}")
