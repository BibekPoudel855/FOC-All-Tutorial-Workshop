'''Write a program that computes the value of the algebraic expression given below.
The program should ask the user to input the values of x and y. Write comments to describe your code '''

# x^3 + 3x^2y + 3xy^2 + y^3
# input 2 value of x and y from user
x = input("enter first number")
y = input("enter second number")

# converting string to integer and storing to x and y respectively
x= int(x)
y= int(y)

# calculating the algebric expression and storing to res
res = x**3 + 3 * x**2 * y + 3 * x * y**2 + y**3

# printing the result with proper formatting
print("Your Result of Algebric Expression is ", res)
print("thank you")
# thank you
