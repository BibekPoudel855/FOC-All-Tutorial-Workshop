# to find if list a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112] has any number divisible by 2 and 3

a = [2, 3, 6, 8, 9, 12, 15, 18, 24, 22, 33, 112]
for i in range(len(a)):
    # if numb divisivle by both number then it is divisible
    if a[i] % 2 == 0 and a[i] % 3 == 0:
        # printing number 
        print(a[i])