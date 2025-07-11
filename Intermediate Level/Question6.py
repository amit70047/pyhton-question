# Q6. Write a function count_vowels(s) that counts the number of vowels in a string.

s = "Hello World"
vowels = "asdfghjkl"
count = 0

for char in s:
    if char in vowels:
        count += 1

print(count)