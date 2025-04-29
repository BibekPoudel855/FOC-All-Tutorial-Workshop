number_list = []
file = open("lab7.txt", "r")
lines = file.readlines()

for each in lines:
    temp = each.strip().split(",")
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    number_list.append(temp)
print(number_list)
sum=0
for each in number_list:
    for each2 in number_list:
