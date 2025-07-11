# Q12. Write a function analyze_list(lst) that returns:

# Total number of elements
# Maximum and minimum value
# Average

list = [12, 5, 8, 19, 3]
result = {
    'count': len(list),
    'max': max(list) if list else None,
    'min': min(list) if list else None,
    'average': sum(list)/len(list) if list else None
}
print(result)