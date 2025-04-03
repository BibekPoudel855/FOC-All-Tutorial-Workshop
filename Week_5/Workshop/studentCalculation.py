# Given below is a table containing data of 5 students obtained in 5 subjects.
# Store the data in python using 2D lists and write code that calculates the
# average marks of all the students and print them out

studentDetails = [
    ['john', 88, 86, 76, 66, 76],
    ['sam', 77, 67, 87, 67, 56],
    ['anna', 67, 65, 67, 76, 65],
    ['ben', 87, 78, 67, 77, 57],
    ['jeff', 90, 80, 79, 88, 70]
]
for student in studentDetails:
    print(student)
    totalMarks = 0
    for i in range(1, len(student)):
        totalMarks+= student[i]

    name = student[0]
    averageMarks = totalMarks / (len(student)-1)
    print(f"average marks of {name} is ",averageMarks)