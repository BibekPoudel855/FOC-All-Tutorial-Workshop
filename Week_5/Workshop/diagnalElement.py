A = [
    [2, 3, 4],
    [1, 5, 6],
    [5, 8, 5]
]
print("dianoal")
sumDiagnal = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            sumDiagnal += A[i][j]
print(sumDiagnal)

print("another diagnal")
sumDiagnal = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if i+j == 2:
            sumDiagnal += A[i][j]
print(sumDiagnal)

print("up diagnal")
sumUpDiagnal = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if j>i:
            sumUpDiagnal += A[i][j]
print(sumUpDiagnal)

print("down diagnal")
sumDownDiagnal = 0
for i in range(len(A)):
    for j in range(len(A[i])):
        if i>j:
            sumDownDiagnal += A[i][j]
print(sumDownDiagnal)