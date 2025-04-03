details = {}
print(details)
while True :
    try :
        N = int(input("Enter a number: "))
        break
    except :
        print("Invalid input")

for i in range(int(N)):
    name = input("Enter a name: ")
    while True :
        try :
            marks = int(input("Enter a marks: "))
            break
        except :
            print("Invalid input")
    details[name] = marks
print(details)