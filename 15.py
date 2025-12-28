'''Given a list, count and display the number
of occurrences of each value in the list..'''

x = [1,2,3,4,4,6,3,2,5,6]
counts = {}
for num in x:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
for value in counts:
    print(value, "appears"
