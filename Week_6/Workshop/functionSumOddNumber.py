# method which take parameter N and returns the sum of all odd numbers from 1 to N.
def sum(N):
    sum = 0
    for i in range(1, N+1):
        if i % 2 != 0:
            sum += i
    return sum
# Testing the function
print(sum(int(input("Enter number"))))