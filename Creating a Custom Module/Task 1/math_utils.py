# Create a module file called math_utils.py and implement the following functions:

# add(a, b)

# subtract(a, b)

# multiply(a, b)

# divide(a, b) (handle division by zero)

a = 10
b = 5

# Addition
add = a + b

# Subtraction
subtract = a - b

# Multiplication
multiply = a * b

# Division 
if b == 0:
    divide = "Error: Cannot divide by zero"
else:
    divide = a / b

print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)
