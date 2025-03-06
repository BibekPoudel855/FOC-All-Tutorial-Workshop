'''
wap to enter 2  a and b and swap it and print
'''
# input 2 value of a and b from user
a = input("Enter a : ")
b = input("Enter b : ")

# swapping the value of a and b without 3rd variable
# this type of assingnment is called multiple assignment which help us to assign multiple value to multiple variable in single line
a, b= b, a

print("a is ", a, "b is ", b)   # printing the result in terminal