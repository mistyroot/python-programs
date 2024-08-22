# A
# BC 
# DEF 
# GHIJ
# KLMNO 

num=65
for i in range(1,6):
    for j in range(1, i+1):
        print(chr(num), end='')
        num=num+1
    print()
