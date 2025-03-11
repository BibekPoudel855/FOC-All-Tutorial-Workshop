# find hcf of 2 number the program should exit on user request only

'''
algorithm of hcf of given two inputs


step 1 : Start
step 2 : display 1 for continue and 2 for exit
step 3 : take input from user
step 4 : if input == 1 then
            go to step 5 
        otherwise if input == 2 then
            go to step 6
        otherwise
            go to step 8

step 5 : 
        step 5.1 : Input 2 number num1 and num2
        step 5.2 : if num1 > num2 then
                    M = num1 and N = num2
                otherwise
                    M = num2 and N = num1
        step 5.3 : calculare R = M % N
        step 5.4 : if R == 0 then
                    display "HCF of num1 and num2 is N"
                    go to step 2
                otherwise
                    M = N and N = R
                    go to step 5.3
step 6 : display "thank for using the program". do visit again. i am waiting for you come back!"
step 7 : Stop
step 8 : display"invalid number try option 1 and 2 only"
step 9 : return to step 2
'''

# main function used in program 
# type : returns the datatype of arg/paramter and the class association with it
# input : takes the input from user which returns in string format
# print : prints the output on console or teminal

DEBUG = True # global variable Debug true mean development and false mean production

while(True) :
# display option to the user
    print("enter 1 to run and 2 for exit")

    # take input from user and convert string to integer
    choice = int(input("Enter your choice : "))


    if(DEBUG) : 
        # display the datatype of choice variable
        print("the datatyoe of choice is : ", type(choice))

        if(choice == 1) :
            pass # add noting to the workflow but eliminates the need of statement or indent . remove when code is added
            num1 = int(input("Enter the first number : "))
            num2 = int(input("Enter the second number : "))
            if(num1 > num2) :
                M,N = num1,num2
            else :
                M,N = num2,num1
                done = False

                while(done==False) :
                    R = M % N
                    if(R == 0) :
                        print("HCF of ",num1," and ",num2," is ",N)
                        done = True
                    else :
                        M,N = N,R

        elif(choice == 2) :
            print("thank for using the program. do visit again. i am waiting for you come back!")
            break
        else :
            print("invalid number try option 1 and 2 only")