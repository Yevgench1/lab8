import random
import numpy as np
a = int(input("Введіть початок діапазону a: "))
b = int(input("Введіть кінець діапазону b: "))
K = np.random.randint(a, b + 1, size=(4, 5))
B = K.reshape(2, 10)
C = B.sum(axis=0)
print("Масив K (4x5):")
print(K)
print("\n Масив B (2x10):")
print(B)
print("\n Масив C (суми стовпців масиву B):")
print(C)
