'''Given a list and a value entered via the keyboard,
remove all instances of the value from the list'''

numbers = [1,2,3,4,8,4,6,3,2,7,8,5,6]
a =[]
for i in numbers:
    if i not in a:
        a.append(i)
print(a)
