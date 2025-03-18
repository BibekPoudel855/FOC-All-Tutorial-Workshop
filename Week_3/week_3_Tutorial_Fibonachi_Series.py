n = int(input("enter number to find fibonachi series : "))

for i in range(n) :
    if i == 0 :
        a = 0
        print(a)
    elif i == 1 :
        b = 1
        print(b)
    else :
        c = a + b
        a = b
        b = c
        print(c)







