lengthList = int(input("Enter the length of list : "))
listOfNumbers = []
for i in range(lengthList) :
    num = int(input("Enter the number : "))
    listOfNumbers.append(num)

max= listOfNumbers[0]
min = listOfNumbers[0]
for each in listOfNumbers :
    if each > max :
        max = each
    if each < min :
        min = each

print(f"the largest number is {max}")
print(f"the smallest number is {min}")