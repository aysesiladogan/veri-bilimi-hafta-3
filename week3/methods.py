def sum_of_digits(text):
    digits = [int(ch) for ch in text if ch.isdigit()]
    return sum(digits)

# Örnek
print(sum_of_digits("abc12def3"))
print(sum_of_digits("ab45c9"))
