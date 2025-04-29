def palindromeCheck(word):
    word = word.lower()
    reversed_word_list = []
    for i in range(len(word) - 1, -1, -1):
        reversed_word_list.append(word[i])
    reversed_word = ''.join(reversed_word_list)  # Convert list to string
    return reversed_word == word

# checking if this is palindrome or not based on return value
if palindromeCheck(input("Enter word: ")):
    print("Palindrome")
else:
    print("Not Palindrome")
