#Write a program to read m students n subjects marks and calculate total,avg and result
m= int(input("Enter how many students:"))
marks=[]

for i in range(m):
    n=int(input(f'Enter how many subject for student {i+1}'))
    row=[]
    for j in range(n):
        s=int(input(f'student {i+1} subject {j+1} marks'))
        row.append(s)
    marks.append(row)

for row in marks:
    total=sum(row)
    avg=total/n
    result="pass"
    for s in row:
        if s<40:
            result="fail"
            break
    print(f'{row}\t{total}\t{avg:.2}\t{result}')

