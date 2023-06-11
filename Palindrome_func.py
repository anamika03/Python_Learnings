#Define a palindrome function that take a 1 word as a input and return TRUE if it is same from backwork and forward.
# input - madam -----> True
      #   naman -----> True
      #   horse -----> False

def is_palindrome(word):
    if word == word[::-1]:
        return "Pallindrome"
    return "Not Pallindrome"

word = input("Enter any string: ")

print(f"{word} is {is_palindrome(word)}")