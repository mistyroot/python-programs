# Sample Input
# 5
# 2 3 6 6 5

# Sample Output
# 5


n=int(input())
s=input()
list1=list(map(int,s.split()))
list1.sort() 
fmax_value=list1[-1]
c=list1.count(fmax_value)
print(list1[-(c+1)])


