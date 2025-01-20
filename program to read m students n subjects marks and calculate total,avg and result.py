m= int(input("Enter how many student:"))
n= int(input("Enter how many subjects"))
marks= []

for i in range(m):
    row=[]
    for j in range(n):
        s= int(input(f"Student {i+1} marks {j+1} "))
        row.append(s)
    marks.append(row)

for row in marks:
    total= sum(row)
    avg= total/n
    result= "pass"
    for s in row:
        if s<40:
            result="fail"
            break

    print(f"{row}\t{total}\t{avg}\t{result}")
