import random
import statistics

numbers = [random.randint(1, 100) for _ in range(10)]
print("Random Numbers:", numbers)

print("Average:", statistics.mean(numbers))
print("Standard Deviation:", statistics.stdev(numbers))
