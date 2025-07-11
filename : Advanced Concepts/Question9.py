# Q9. Write a recursive function sum_of_digits(n) that returns the sum of digits of a number.
n = 10
fib = [0, 1]  

if n <= 0:
    fib = []
elif n == 1:
    fib = [0]
else:
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])

print(fib)