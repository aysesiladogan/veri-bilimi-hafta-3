A = {"Python", "R", "SQL", "Java"}
B = {"C++", "Python", "JavaScript", "SQL"}

print("Common language:", A & B)

print("Only in A:", A - B)

print("Combination (alphabetical):", sorted(A | B))
