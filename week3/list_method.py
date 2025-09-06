grades = [85, 92, 76, 92, 100, 76, 85, 92]

unique = list(set(grades))
print("Unique List:", unique)

print("Lowest grade:", max(unique))
print("Highest grade:", min(unique))

sorted = sorted(unique)
print("Sorted List:", sorted)
