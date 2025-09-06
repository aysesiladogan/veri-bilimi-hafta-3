def is_armstrong(num):
    total = sum(int(digit)**3 for digit in str(num))
    return total == num

print(is_armstrong(153))
