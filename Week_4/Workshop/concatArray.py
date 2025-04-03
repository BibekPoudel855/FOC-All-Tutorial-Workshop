# Write a program that performs element-wise addition on 2 lists of numbers

# having the same length and outputs another list containing the sums, e.g.

#  + [1, 2, 3, 4, 5, 6]

# -> [2, 4, 6, 8, 10, 12]

num  = [1, 2, 3, 4, 5, 6]
addition =[]

for i in range(len(num)) :
    # appending number by adding them
    addition.append((num[i]+num[i]))

print(addition)

""" 

we have find sq of that number by adding that number twice
"""