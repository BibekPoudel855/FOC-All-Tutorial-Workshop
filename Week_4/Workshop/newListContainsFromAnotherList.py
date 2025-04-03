#Write a program that creates a new list containing all the elements placed
#on even positions of the original list.
#[43, 23, 21, 44, 56, 75] -> [23, 44, 75]
oldList = [43, 23, 21, 44, 56, 75]
newList = []
for i in range(len(oldList)):
    # appending odd index or appednig event position 
    if(i % 2 != 0 ):
        newList.append(oldList[i])
# printing list 
print(newList)