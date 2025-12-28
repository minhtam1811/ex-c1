'''Given two lists, A and B, 
find and output their intersection (common elements).'''

x = [1,2,3,4,8,4,6,3,2,7,8,5,6]
y = [1,5,7,3,7,3,8]
intersection = list (set(x) & set(y))
print(intersection)
