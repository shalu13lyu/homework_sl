import numpy as np

# 2x2 matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("2x2 MATRIX CALCULATOR")
print("Addition:")
print(A + B)

print("Subtraction:")
print(A - B)

print("Multiplication:")
print(A @ B)


# 3x3 matrices
C = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

D = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("\n3x3 MATRIX CALCULATOR")
print("Addition:")
print(C + D)

print("Subtraction:")
print(C - D)

print("Multiplication:")
print(C @ D)