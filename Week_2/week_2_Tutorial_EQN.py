''' 
wap to ask user to input the cofficient  a,b,c of the quadratic equation ax^2 + bx + c = 0.
The program should find value of x which are solution to quadratic equation using formula
'''
# Quadratic equation: ar^2 + br + c = 0
# input 3 value of a,b and c from user and converting to float
a = float(input("enter first number"))
b = float(input("enter second number"))
c = float(input("enter third number"))

# calculating the algebric expression and storing to x1 amd x2
x1 = ((b*-1) + ((b**2 - 4*a*c)**0.5))/(2*a)
x2 = ((b*-1) - ((b**2 - 4*a*c)**0.5))/(2*a)

# printing the result in terminal
print("result of x1 is ", x1,"result of x2 is", x2)
print("thank you")
# end of the
