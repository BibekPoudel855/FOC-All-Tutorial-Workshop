N = int(input("enter number to find fibonachi series : "))
number1=1
number2=1
print("1, 1, ")
for i in range(N) :
        temp = number1 + number2
        number1 = number2
        number2 = temp
        print(temp, )


"""

"""







