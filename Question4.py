# Q4. Write a function factorial(n) that returns the factorial of a number using a loop.

n = int(input("Enter a number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} is: ")