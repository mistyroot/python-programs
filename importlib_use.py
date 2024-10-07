# Write a program to import any library

import importlib

<<<<<<< HEAD

=======
>>>>>>> 50d262ca618a311b5f8104afffd4fffdadd9e21d
module_name=input("Enter Module Name or Library Name to Import")
m=importlib.import_module(module_name)
list1=dir(m)
print(list1)
