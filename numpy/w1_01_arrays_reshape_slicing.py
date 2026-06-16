
## Step 1 — Creating Arrays
import numpy as np

# From list
arr1 = np.array([1, 2, 3, 4, 5])
print("1D array:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D array:\n", arr2)

# Zeros
print("Zeros:", np.zeros(5))
print("Zeros 2D:\n", np.zeros((3, 4)))

# Ones
print("Ones:", np.ones(5))
print("Ones 2D:\n", np.ones((3, 4)))

# arange — like Python range
print("arange:", np.arange(0, 10, 2))
# [0 2 4 6 8]

# linspace — evenly spaced between two numbers
print("linspace:", np.linspace(0, 2, 5))
# [0.0  0.25  0.5  0.75  1.0]

## Step 2 — Array Properties

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Shape :", arr.shape)   # (2, 3)
print("Ndim  :", arr.ndim)    # 2
print("Size  :", arr.size)    # 6
print("Dtype :", arr.dtype)   # int64

## arange vs linspace

'''arange   → you control the STEP
linspace → you control the COUNT

arange(0, 10, 2)  → [0, 2, 4, 6, 8]     step=2
linspace(0, 1, 5) → [0, 0.25, 0.5, 0.75, 1.0]  5 evenly spaced

Real life use:
arange  → loop counters, indices
linspace → AI learning rates, graph axes'''


## Step 3 — Reshape

arr = np.arange(1, 13)
print("Original:", arr)
# [ 1  2  3  4  5  6  7  8  9  10  11  12]

# Reshape to 3x4
print("3x4:\n", arr.reshape(3, 4))

# Reshape to 2x6
print("2x6:\n", arr.reshape(2, 6))

# Reshape to 4x3
print("4x3:\n", arr.reshape(4, 3))

# Flatten back to 1D
print("Flatten:", arr.reshape(3, 4).flatten())



## Step 4 — Indexing


# 1D indexing
arr = np.array([10, 20, 30, 40, 50])
#index:          0   1   2   3   4

print(arr[0])    # 10 ← first
print(arr[4])    # 50 ← last
print(arr[-1])   # 50 ← last (negative index)
print(arr[-2])   # 40 ← second from last

# 2D indexing
marks = np.array([
    [45, 78, 90],
    [82, 34, 67],
    [23, 56, 88]
])

print(marks[0, 0])   # 45 ← row0, col0
print(marks[1, 2])   # 67 ← row1, col2
print(marks[2, 1])   # 56 ← row2, col1
print(marks[-1, -1]) # 88 ← last row, last col

## Step 5 — Slicing

arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Basic slice [start:stop:step]
print(arr[1:4])     # [20 30 40]
print(arr[:3])      # [10 20 30] first 3
print(arr[3:])      # [40 50 60 70] from index 3
print(arr[::2])     # [10 30 50 70] every 2nd
print(arr[::-1])    # [70 60 50 40 30 20 10] reversed

## Step 6 — 2D Slicing

marks = np.array([
    [45, 78, 90],
    [82, 34, 67],
    [23, 56, 88]
])

# All rows, first column
print(marks[:, 0])
# [45 82 23]

# First row, all columns
print(marks[0, :])
# [45 78 90]

# First two rows
print(marks[:2, :])
# [[45 78 90]
#  [82 34 67]]

# Last two columns
print(marks[:, 1:])
# [[78 90]
#  [34 67]
#  [56 88]]

# Submatrix — first 2 rows, last 2 cols
print(marks[:2, 1:])
# [[78 90]
#  [34 67]]

## Step 7 — dtype

# Integer array
arr_int = np.array([1, 2, 3])
print(arr_int.dtype)   # int64

# Float array
arr_float = np.array([1.0, 2.0, 3.0])
print(arr_float.dtype)  # float64

# Change dtype
arr_int = arr_int.astype(float)
print(arr_int.dtype)   # float64

# Why it matters
# AI models need float not int
# Saves memory with right dtype

# Now Your Tasks

# import numpy as np

# Task 1 - Create these arrays:
# 1. 1D array of numbers 1-20
arr=np.arange(0,21,1)
print(arr)
# 2. 2D array of zeros (4x5)
print(np.zeros((4,5)))
# 3. Array of 10 evenly spaced numbers between 0 and 100
print(np.linspace(0,100,10).astype(int))
# 4. arange from 0 to 50 step 5
print(np.arange(0,51,5))

# Task 2 - Reshape:
# 1. Create array 1-24
arr=np.arange(1,25)
print(arr)
# 2. Reshape to 4x6
print(np.reshape(arr,[4,6]))
# 3. Reshape to 2x12
print(np.reshape(arr,[2,12]))
# 4. Flatten back to 1D
print(np.reshape(arr,[4,6]).flatten())

# Task 3 - Slicing:
marks = np.array([
    [45, 78, 90, 55],
    [82, 34, 67, 91],
    [23, 56, 88, 74],
    [95, 61, 43, 38]
])


# 1. Get first row
# 2. Get last column
# 3. Get first 2 rows and first 2 columns
# 4. Get marks of student 3 (row 2)
# 5. Reverse the entire array
# 6. Get every other row

