#input 2 subject marks and print result
sub1=int(input("Subject1 marks"))
sub2=int(input("Subject2 marks"))
if sub1>=40:
    if sub2>=40:
        print("pass")
    else:
        print("sub2 fail")
else:
    print("sub1 fail")