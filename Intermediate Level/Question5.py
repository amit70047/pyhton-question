# Q5. Write a function find_max(lst) that takes a list and returns the maximum number
k = [3, 1, 5, 10]

if not k:
    max_num = None
else:
    max_num = k[0]
    for num in k:
        if num > max_num:
            max_num = num

print(max_num)