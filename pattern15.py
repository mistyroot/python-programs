# ABCDE
# ABCD
# ABC
# AB 
# A 

for i in range(5, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end='')
    print()
