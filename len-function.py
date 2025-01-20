student_names=["Naresh","Suresh","Ramesh","Kishore","Rajesh","Kiran","Raman"]
index= int(input("Enter student position to read:"))

if index>= 0 and index< len(student_names) or (index >= -len(student_names)) and index <= -1 :
    name= student_names[index]
    print(f'Student_name {name}')
else:
    print("invalid index")
