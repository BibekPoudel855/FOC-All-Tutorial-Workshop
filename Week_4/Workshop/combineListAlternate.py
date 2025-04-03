# Write a program that combines two lists of equal length by alternatingly
# taking elements, e.g.
# [‘a’, ‘b’, ‘c’], [1, 2, 3] -> [‘a’, 1, ‘b’, 2, ‘c’, 3]

# declaring lists 
listOne =['a','b','c']
listTwo = [1,2,3]
newList = []

# to track final lenght h of list
finalLen = 0

# length must be equal to anohter list or we take list length which have smaller index 
if(len(listOne) == len(listTwo)) :
    finalLen = len(listOne)
elif(len(listOne<len(listTwo))):
    finalLen = listOne
elif(len(listOne>len(listTwo))):
    finalLen = listTwo


# to append in new list alternatevely
for i in range(finalLen):
        newList.append(listOne[i])
        newList.append(listTwo[i])
# printing list
print(newList)