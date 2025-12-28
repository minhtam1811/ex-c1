'''Given a list and a value entered via the keyboard,
remove all instances of the value from the list'''

x = [1,2,3,4,8,4,6,3,2,7,8,5,6]
y = [1,5,7,3,7,3,8]
intersection = list (set(x) & set(y))
print(intersection)
