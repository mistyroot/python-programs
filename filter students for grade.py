grade_list=[['naresh','A'], ['ramesh','B'], ['suresh','C'], ['rajesh','A'], ['kishore','B'], ['kiran','C'], ['raman','A']]

print(grade_list)
gradeA_list=[stud for stud in grade_list if stud[1]=='A' ]
gradeB_list=[stud for stud in grade_list if stud[1]=='B' ]
gradeC_list=[stud for stud in grade_list if stud[1]=='C' ]

print(gradeA_list)
print(gradeB_list)
print(gradeC_list)
