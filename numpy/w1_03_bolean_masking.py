'''What is a Boolean Mask?
A boolean mask is simply an array of True/False values that acts as a filter.
Think of it like this:
Original:  [5,  12,  3,  18,  7]
Question:  "Which are greater than 10?"
Mask:      [False, True, False, True, False]
Result:    [12, 18]
NumPy keeps only the values where mask is True.

Real Life Analogy
Imagine a security guard with a checklist:

Person 1 — No entry 
Person 2 — Enter 
Person 3 — No entry 
Person 4 — Enter 

That checklist is a boolean mask. It decides who gets through.'''
import numpy as np

arr = np.array([5, 12, 3, 18, 7])

# Step 1 — Create the mask
mask = arr > 10
print(mask)
# Output: [False  True False  True False]

# Step 2 — Apply the mask
result = arr[mask]
print(result)
# Output: [12 18]

# One line shortcut (same thing)
print(arr[arr > 10])
# Output: [12 18]

'''Multiple Conditions'''
arr = np.array([5, 12, 3, 18, 7, 24])

# AND condition — between 10 and 20
print(arr[(arr > 10) & (arr < 20)])
# Output: [12 18]

# OR condition — less than 5 or greater than 20
print(arr[(arr < 5) | (arr > 20)])
# Output: [3 24]

arr = np.array([5, 12, 3, 18, 7])

'''Modifying Values With a Mask'''

# Replace all values greater than 10 with 0
arr[arr > 10] = 0
print(arr)
# Output: [5  0  3  0  7]

'''What is AND / OR Logic?
It's how you combine multiple conditions to make a decision.

AND Logic
Both conditions must be TRUE
Real life example:'''

"I will go out if it's sunny AND I have money"


sunny = True
have_money = False

print(sunny and have_money)
# Output: False

'''OR Logic
At least one condition must be TRUE
Real life example:'''

"I will go out if it's sunny OR I have money"


sunny = False
have_money = True

print(sunny or have_money)
# Output: True

'''NOT Logic
Flips True to False and False to True'''
sunny = True
print(not sunny)
# Output: False

# Now in NumPy
# NumPy uses special symbols because it works on whole arrays:
# Normal Python NumPy Symbol and & or | not ~


arr = np.array([5, 12, 3, 18, 7, 24])

# AND — numbers greater than 5 AND less than 20
print(arr[(arr > 5) & (arr < 20)])
# Output: [12  7  18]

# OR — numbers less than 5 OR greater than 20
print(arr[(arr < 5) | (arr > 20)])
# Output: [3 24]

# NOT — numbers that are NOT greater than 10
print(arr[~(arr > 10)])
# Output: [5 3 7]

