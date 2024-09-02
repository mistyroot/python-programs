# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

list1=[]
n=int(input())
for i in range(n):
    cmd=input().split()
    if cmd[0]=="insert":
       list1.insert(int(cmd[1]),int(cmd[2]))
    elif cmd[0]=="print":
        print(list1)
    elif cmd[0]=="sort":
        list1.sort() 
    elif cmd[0]=="reverse":
        list1.reverse() 
    elif cmd[0]=="pop":
        list1.pop()
    elif cmd[0]=="append":
        list1.append(int(cmd[1]))
    elif cmd[0]=="remove":
        list1.remove(int(cmd[1]))



