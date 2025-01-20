names=['ramesh','kishore','rajesh','kiran','naresh','suresh']

names_h=[ name  for name in names if name[-1]=='h'] #end with h
print(names)
print(names_h)

names_rh=[name for name in names if name[0]=='r' and name[-1]=='h'] #start with r , end h
print(names_rh)
