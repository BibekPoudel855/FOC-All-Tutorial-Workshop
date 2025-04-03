# guessing game
import random
# random number
randomNumber = random.randint(1,100)
print(randomNumber)
# attempt number 
number = int(input("your attempts"))

for i in range(number):
    userNumber = int(input("enter number to guess"))
    while(userNumber != randomNumber) : 
        if(randomNumber > userNumber):
            print("usernumb is small")
        else:
            print("usernumb is greater")
        userNumber = int(input("enter number to guess"))
    print("you guess the number", userNumber, randomNumber)