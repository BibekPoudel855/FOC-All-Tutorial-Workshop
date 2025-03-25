# default list given in question
List = [1, 1, 2, 3, 3, 4, 4, 5, 6, 5, 6]
# list where unique elements will be stored
uniqueList = []
# loop through the list
for i in List:
    if(i not in uniqueList):
        uniqueList.append(i)

print(uniqueList)


"""
in this question we have to display the unique elements from the given list
we have created a uniqueList variable and We use loop to iterate the list then we check if the element is not in the uniqueList then append it to the uniqueList and display the uniqueList
"""