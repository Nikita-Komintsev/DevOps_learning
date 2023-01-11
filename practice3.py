import re

some_string = input("Введите строку ")
n = 1
while n:
    some_string, n = re.subn(r'\[[^\[\]]*\]', '', some_string)
print(some_string)