def is_palindrome(words):
    return word == word[::-1]

# Input from user
word = input("Enter a word: ")

# Check if the word is a palindrome
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

