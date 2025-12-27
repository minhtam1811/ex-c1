''' Given a list and a value entered via the keyboard,
if the value exists in the list, remove the element at its first
occurrence'''

numbers = [1,2,3,4,8,4,6,3,2,7,8,5,6]
value = int(input("Enter a number: "))
count = 0
for num in numbers:
    if num == value:
        count += 1
        break
if count == 0:
    print("The number is zero!")
else:
    numbers.remove(value)
    print('Numbers:',numbers)
