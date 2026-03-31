import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
Original Array:
print(arr)
[1 2 3 4 5 6]

# Reshaping the array (2 rows, 3 columns)
reshaped_arr = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")

Reshaped Array (2x3):
print(reshaped_arr)
[[1 2 3]
 [4 5 6]]

# Indexing (access element at row 1, column 2)
print("\nElement at position [1][2]:", reshaped_arr[1][2])

Element at position [1][2]: 6
# Sum of elements
print("\nSum of all elements:", np.sum(arr))

Sum of all elements: 21




import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
SyntaxError: multiple statements found while compiling a single statement
import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
... B = np.array([[5, 6], [7, 8]])
SyntaxError: multiple statements found while compiling a single statement
>>> # Create two matrices
... A = np.array([[1, 2], [3, 4]])
>>> B = np.array([[5, 6], [7, 8]])
>>> print("Matrix A:")
Matrix A:
>>> print(A)
[[1 2]
 [3 4]]
>>> print("\nMatrix B:")

Matrix B:
>>> print(B)
[[5 6]
 [7 8]]
>>> # Addition
... print("\nMatrix Addition (A + B):")

Matrix Addition (A + B):
>>> print(A + B)
... 
[[ 6  8]
 [10 12]]
>>> 
... # Multiplication (Matrix multiplication)
... print("\nMatrix Multiplication (A @ B):")

Matrix Multiplication (A @ B):
>>> print(np.dot(A, B)) # or A @ B
[[19 22]
 [43 50]]
>>> # Transpose of matrix A
... print("\nTranspose of Matrix A:")

Transpose of Matrix A:
>>> print(A.T)
[[1 3]
 [2 4]]
