'''Given a list and a value entered via the keyboard,
remove all instances of the value from the list'''

numbers = [1,2,3,4,8,4,6,3,2,7,8,5,6]
value = int(input("Enter a number: "))
for i in range(len(numbers)-1,-1,-1):
    if numbers[i] == value:
        numbers.pop(i)
print (numbers)
