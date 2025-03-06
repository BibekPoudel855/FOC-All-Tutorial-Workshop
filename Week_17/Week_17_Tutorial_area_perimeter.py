# wap to find area and perimeter of the rectangle by input from user

'''
function to solve problem
1. input : method which take string msg as parameter and
        returns value provided by user as string when enter pressed
2. print : method which take values as parameters and print it on screen
3. type : returns the data type of input provided by user
'''



# get value of length and breadth of rectangle  from user
length = input("Enter the length of rectangle in meters : ")
breadth = input("Enter the breadth of rectangle in meters : ")


# convert the string data into float data
length = float(length)
breadth = float(breadth)

# check the data type of length and breadth
print("data type of length", type(length))
print("data type of breadth", type(breadth))

# calculate the area and perimeter of rectangle
area = length * breadth
perimeter = 2 * (length + breadth)

# print data types
print("data type of perimeter", type(perimeter))
print("data type of area", type(area))


# display values
print("value of perimeter is ",perimeter)
print("valeu of area is ", area)