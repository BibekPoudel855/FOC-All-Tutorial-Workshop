N = int(input("enter number to find fibonachi series : "))
number1=1
number2=1
fibonaciList= [1,1]
for i in range(N-2) :
        temp = number1 + number2
        number1 = number2
        number2 = temp
        fibonaciList.append(temp)

print(fibonaciList)


""" 
in order to find fibonachi series firts we assign 1 value to number1 and number2 variable then we created a list fibonaciList and we use loop to iterate upto N-2 then we added the number1 and number2 and stored it in temp variable then we assigned number2 value to number1 and temp value to number2 then we pushed value of temp to fibonaciList and displayed the fibonaciList
in terminal
"""






