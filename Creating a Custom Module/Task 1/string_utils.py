def count_vowels(s):
    
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):

    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def reverse_words(sentence):
    
    words = sentence.split()
    return ' '.join(reversed(words))