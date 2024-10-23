def first_palindrome(words):
    return next((word for word in words if word == word[::-1]), "")
