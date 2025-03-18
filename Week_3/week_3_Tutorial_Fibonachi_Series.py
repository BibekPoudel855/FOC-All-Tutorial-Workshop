a=2,3
print(type(a))

n = int(input("enter number to find fibonachi series : "))
a=1

b=1
for i in range(n) :
        c = a + b
        a = b
        b = c

        print(c)







