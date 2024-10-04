name="NARESH"
marks=[60,70,80]
total=0

for i in range(len(marks)):
    total=total+marks[i]

avg=total/len(marks)

print(f'Name {name}')
print(f'Marks {marks}')
print(f'Total Marks {total}')
print(f'Avg Marks {avg:.2f}')

