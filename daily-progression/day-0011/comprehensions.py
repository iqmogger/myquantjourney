# Old way (Day 8 for loop):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared = []               # start with an empty list
for n in numbers:           # loop through each number
    squared.append(n ** 2)  # square it, add to the list
print(squared)              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# NEW — List comprehension (same result, one line):
squared = [n ** 2 for n in numbers]
print(squared)              # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
