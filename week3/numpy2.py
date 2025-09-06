import numpy as np

matris = np.random.rand(5, 5)
print("Matris:\n", matris)

column_aver = np.mean(matris, axis=0)
print("\nAverage of columns:", column_aver)

binary = (matris > 0.5).astype(int)
print("\nBinary Matris:\n", binary)
