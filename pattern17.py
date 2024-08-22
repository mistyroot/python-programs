#      A
#     BC 
#    DEF 
#   GHIJ 
#  KLMNO


num=65
for i in range(1,6):
    for j in range(5,0,-1):
        if i>=j:
            print(chr(num), end='')
            num=num+1
        else:
            print(' ', end='')
    print()

