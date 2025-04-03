# orignal list
original_list = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
print("Original list:", original_list)
# Removing redundant data
# converting it to set and then back to list
uniqueList = set(original_list)
uniqueList = list(uniqueList)
# printing unique list
print("Unique list:", uniqueList)
#sorting the list in descending order
size = len(uniqueList)
for i in range(size):
    has_swapped = False
    for j in range(size - 1 - i):
        if uniqueList[j] < uniqueList[j + 1]:
            uniqueList[j
            ], uniqueList[j + 1] = uniqueList[j + 1], uniqueList[j]
            has_swapped = True
    if not has_swapped: 
        break

# print sorted list
print(uniqueList)
