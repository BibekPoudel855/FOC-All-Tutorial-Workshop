# Bubble Sort Algorithm which is optimized
user_list = [9,5,10,1]
# size of list 
size = len(user_list)


for i in range(size):
    # to track is list sorted or not 
    # it help to run loop lower
    has_swapped = False
    for j in range(size-1-i): # we can remove i in range()
        if user_list[j] > user_list[j+1]:
            # swapping if first list is greater 
            user_list[j],user_list[j+1] = user_list[j+1],user_list[j]
            has_swapped = True

    # if list is swapped then break so code optimzed
    if has_swapped == False:
        break

print(user_list)
