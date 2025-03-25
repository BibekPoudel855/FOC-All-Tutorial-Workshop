List = [1,2,3,4,5,6]
print("List is ",List)
reversedList = []
for i in range(len(List)-1, -1, -1):
    reversedList.append(List[i])

print("Reversed List is ",reversedList)


""" 
in order to reverse a list we have created a resersedList variable and we used loop in List variable in reverse order
and appended the elements of List variable to the reversedList
"""