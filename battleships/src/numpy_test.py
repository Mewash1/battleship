import numpy as np


x = np.zeros((3, 3))

for y in range(0, 3):
    try:
        x[2][0 + y] = 1
    except IndexError:
        continue

print(x)