import numpy as np

m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
m = np.ravel(m1 + m2)
print(m)
