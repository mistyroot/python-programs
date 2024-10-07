# Write a program to import any library

import importlib


module_name=input("Enter Module Name or Library Name to Import")
m=importlib.import_module(module_name)
list1=dir(m)
print(list1)
