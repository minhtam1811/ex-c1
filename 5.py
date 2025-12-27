'''Given a list and a value entered via the keyboard, determine whether the value exists in the list. If it does,
return the index of its last occurrence.'''

numbers = [1,2,3,4,8,4,6,3,2,7,8,5,6]
value = int(input("Enter a number: "))
check = True
for i in range(len(numbers)-1,0,-1):
    if numbers[i] == value:
        print(i)
        check=False
        break
if check :
    print('Not found')
