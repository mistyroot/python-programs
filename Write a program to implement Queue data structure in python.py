#Write a program to implement Queue data structure in python

queue=[]
while True:
    print("1. Adding ")
    print("2. Removing ")
    print("3. View ")
    print("4. Exit")
    opt=int(input("Enter Your Option :"))
    match(opt):
        case 1:
            value=int(input("Enter Value "))
            queue.append(value)
            print(f'{value} is added with queue')
        case 2:
            if len(queue)==0:
                print("queue is empty")
            else:
                value=queue[0]
                del queue[0]
                print(f'{value} is removed from queue')
        case 3:
            print(f'Queue is {queue}')
        case 4:
            break
        case _:
            print("invalid option")
