# simple program to input 2 number from user and find sum and difference of them
'''
function to solve problem
1. input : method which take string msg as parameter and
        returns value provided by user as string when enter pressed
2. print : method which take values as parameters and print it on screen
3. type : returns the data type of input provided by user
'''


# input first number from user 
firstNum = input("Enter the first number : ")
# input second number from user
secondNum = input("Enter the second number : ")

# check the data type of first number and second number
print("data type of first number", type(firstNum))
print("data type of second number", type(secondNum))

# convert the string data into float data
firstNum = int(firstNum)
secondNum = int(secondNum)

# print data type of number
print("data type of first number", type(firstNum))
print("data type of second number", type(secondNum))

# calculate the sum and difference of two numbers
sum = firstNum + secondNum
difference = firstNum - secondNum

# check the data type of sum and difference
print("data type of sum", type(sum))
print("data type of difference", type(difference))

# display the sum and difference of two numbers
print("sum of two numbers is ", sum)
print("difference of two numbers is ", difference)



# wap to input name from user and print it on screen
name = input("Enter your name : ")
print("Hello Your Name is",name)
print("Welcome to python programming")