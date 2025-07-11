# Q11. Write a function calculate_grade(score) that returns a grade based on score:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

score = 85

if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)