n = input("Enter the number of length of list : ")
n = int(n)
listOfNumbers = []
for i in range(int(n)) :
    listOfNumbers.append(int(input("Enter the number : ")))
    num = int(input("Enter the number : "))
    listOfNumbers.append(num)
    print(listOfNumbers)
print(listOfNumbers)
evenSum = 0
oddSum = 0
for (each) in listOfNumbers:
    if each % 2 == 0:
        print("even")
        evenSum += each
    else :
        print("odd")
        oddSum += each

print(f"sum of even is {evenSum}")
print("sum of odd is ", oddSum)

