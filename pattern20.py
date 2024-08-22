#     *
#    * 
#   *
#  *
# *

for i in range(1,6):
    for j in range(5,0,-1):
        if i==j:
            print("*", end='')
            i=i+1
        else:
            print(' ', end='')
    print()

