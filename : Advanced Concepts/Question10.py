# Q10. Write a function is_palindrome(s) that checks whether a string is a palindrome or not.

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])