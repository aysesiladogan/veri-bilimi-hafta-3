import numpy as np

sequence = np.random.randint(0, 51, 10)
print("Sequence:", sequence)

print("Average:", np.mean(sequence))
print("Standard Deviation:", np.std(sequence))
print("Smallest:", np.min(sequence))
print("Biggest:", np.max(sequence))
