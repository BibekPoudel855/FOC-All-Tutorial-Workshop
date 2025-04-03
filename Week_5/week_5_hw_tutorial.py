# Given below is a 3x3 matrix A, use 2D lists to
# represent the matrix in a python script. Then find out
# the elements of the matrix which are divisible by 2
# and 3. Also find out the maximum and minimum
# element of the matrix.


A = [[24,3,6],
     [8,12,18],
     [2,66,7]]
print("Finding Divisible by 2 and 3............")
for i in range(len(A)):
    for j in range(len(A[i])):
        if(A[i][j]%2 == 0 and A[i][j]%3==0) :
            print(A[i][j], "is divisible by 2 and 3")


print("Finding Maximum and Minimum..........")

maximum = A[0][0]# 24
minimum = A[0][0]#24
for i in range(len(A)):
    for j in range(len(A[i])):
        if(A[i][j] > maximum):
            maximum = A[i][j]
        if(A[i][j] < minimum):
            minimum = A[i][j]
print("Maximum: ", maximum)
print("Minimum: ", minimum)

