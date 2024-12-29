word = input("Enter the word: ")
if word == word[::-1]:  # Slicing to reverse the string
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")