
def countVowelConstant(word) :
    count = 0
    word = word.lower()
    for char in word:
        if char in 'aeiou':
            count += 1

    return count
print(countVowelConstant(input("Enter a number: ")))


