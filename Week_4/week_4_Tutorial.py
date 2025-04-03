# Simple for sorting but not optimized
List = [1,2,3,4]
temp = 0
for i in range(0, len(List)):
    for j in range(i+1, len(List)):
        if(List[i] > List[j]):
            temp = List[i]
            List[i] = List[j]
            List[j] = temp
            temp = 0


for i in range(0, len(List)):
    print(List[i])



# Bubble Sort Algorithm which is optimized
user_list = [9,5,10,1]
size = len(user_list)

for i in range(size):
    has_swapped = False
    for j in range(size-1-i): # we can remove i in range()
        if user_list[j] > user_list[j+1]:
            user_list[j],user_list[j+1] = user_list[j+1],user_list[j]
            has_swapped = True
    if has_swapped == False:
        break

print(user_list)


# error handling or exception handling
try:
    print(user_list[size+2])
except IndexError:
    print(IndexError)