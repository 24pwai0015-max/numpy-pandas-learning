'''What is Broadcasting?
It allows NumPy to perform operations on arrays of different shapes without writing loops.
...
Imagine you have 5 students and you want to give everyone 10 bonus marks:
...
Normal thinking:
Student 1: 45 + 10 = 55
Student 2: 78 + 10 = 88
Student 3: 90 + 10 = 100
Student 4: 55 + 10 = 65
Student 5: 67 + 10 = 77

Broadcasting thinking:
[45, 78, 90, 55, 67] + 10 = [55, 88, 100, 65, 77]
'''

# Step 1 — Scalar Broadcasting
import numpy as np

marks = np.array([45, 78, 90, 55, 67])

# Add 10 to every element
print(marks + 10)
# [55 88 100 65 77]

# Multiply every element by 2
print(marks * 2)
# [90 156 180 110 134]

# Divide every element by 100
print(marks / 100)
# [0.45 0.78 0.90 0.55 0.67]

# No loops needed — NumPy handles it automatically.

'''
Step 2 — Array Broadcasting (Same Shape)'''
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

# Element by element operation
print(arr1 + arr2)
# [11 22 33 44 55]

print(arr1 * arr2)
# [10 40 90 160 250]

'''Step 3 — 2D Array Broadcasting (Same Shape)'''
marks = np.array([
    [45, 78, 90],   # Student 1
    [82, 34, 67],   # Student 2
    [23, 56, 88]    # Student 3
])

# Add 10 bonus to every mark
print(marks + 10)
# [[55 88 100]
#  [92 44  77]
#  [33 66  98]]

'''Step 4 — Row Broadcasting
Add different bonus to each subject:'''
marks = np.array([
    [45, 78, 90],
    [82, 34, 67],
    [23, 56, 88]
])

# Math gets +5, English gets +10, Science gets +15
bonus = np.array([5, 10, 15])

print(marks + bonus)
# [[50  88 105]
#  [87  44  82]
#  [28  66 103]]

'''Step 5 — Column Broadcasting
Add different bonus to each student:'''
marks = np.array([
    [45, 78, 90],
    [82, 34, 67],
    [23, 56, 88]
])

# Student 1 gets +5, Student 2 gets +10, Student 3 gets +15
bonus = np.array([[5],
                  [10],
                  [15]])

print(marks + bonus)
# [[50  83  95]
#  [92  44  77]
#  [38  71 103]]
'''
Rule 1: If arrays have different dimensions
        smaller array is padded on LEFT with 1s

Rule 2: Arrays with size 1 along a dimension
        are stretched to match the other array

Rule 3: If sizes differ and neither is 1
        → ERROR
    real world use of brodcasting:    
        import numpy as np

# Normalize AI model scores to 0-1 range
scores = np.array([
    [85, 92, 78],
    [71, 88, 95],
    [90, 65, 83]
])

# Find min and max per subject
min_scores = scores.min(axis=0)
max_scores = scores.max(axis=0)

# Normalize using broadcasting
normalized = (scores - min_scores) / (max_scores - min_scores)
print("Normalized:\n", normalized)

what is normalization:
Normalization is a data preprocessing technique used to scale 
numerical values to a common range, usually 0 to 1.

'''

marks = np.array([45, 78, 90, 55, 63])

# 1. Add 5 bonus marks to everyone
print("5 bonus marks to everyone:",marks+5)
# 2. Convert marks to percentage (out of 150)
print("percentage:",(marks)/(150)*(100))
# 3. Multiply all marks by 1.1 (10% grade boost)
print("10% grade boost:",marks*1.1)
# 4. Subtract mean from all marks (mean centering)
mean=np.mean(marks)
print(mean)
print("mean centering:",marks-mean)

'''What Mean Centering Does
pythonmarks  = [45,  78,  90,  55,  63]
mean   = 66.2

centered = [-21.2  11.8  23.8  -11.2  -3.2]
Negative = below average

Positive = above average
Used in AI/ML to normalize data before training models.'''


# task 2

sales = np.array([
    [1200, 3400, 2100],    
    [2300, 1800, 4200],
    [3100, 2700, 1900]
])

# 1. Add 500 to all sales
print(sales+500)
# 2. Apply 10% tax
# 10/100=10%
print("with 10 percent tx:",sales*10/100)
# 3. Add different bonus per shop [100, 200, 300]
bonus=np.array([[100], 
                [200], 
                [300]])
print("bonus per shope",sales+bonus)
# 4. Add different bonus per day [50, 100, 150]
bonus=np.array([50, 100, 150])
print("bonus per day:",sales+bonus)
# 5. Normalize between 0 and 1
max=np.max(sales)
min=np.min(sales)

normalized=(sales-min)/(max-min)
print("normalized sales",normalized)

'''import numpy as np

sales = np.array([
    [1200, 3400, 2100],
    [2300, 1800, 4200],
    [3100, 2700, 1900]
])

# 1. Add 500 to all sales
print("Add 500:\n", sales + 500)

# 2. Apply 10% tax
print("10% tax amount:\n", sales * 0.10)

# 3. Add different bonus per shop
bonus = np.array([[100],
                  [200],
                  [300]])
print("Bonus per shop:\n", sales + bonus)

# 4. Add different bonus per day
bonus = np.array([50, 100, 150])
print("Bonus per day:\n", sales + bonus)

# 5. Normalize between 0 and 1
max_sales = np.max(sales)
min_sales = np.min(sales)

normalized = (sales - min_sales) / (max_sales - min_sales)
print("Normalized sales:\n", normalized)'''


# task set 3

# AI agent accuracy scores
# 3 agents tested on 4 different tasks
accuracy = np.array([
    [0.82, 0.85, 0.79, 0.88],
    [0.71, 0.74, 0.69, 0.75],
    [0.90, 0.92, 0.88, 0.94]
])

# 1. Subtract mean accuracy of each agent from their scores
#    Hint: mean(axis=1) then reshape
average_accuracy_score=np.mean(accuracy,axis=1).reshape(3,1)
# print(average_accuracy_score)
print(average_accuracy_score)
print(accuracy-average_accuracy_score)
# 2. Normalize each agent scores between 0 and 1

min_score=np.min(accuracy,axis=1)
max_score=np.max(accuracy,axis=1)

normalized=(accuracy-min_score.reshape(3,1))/(max_score.reshape(3,1)-min_score.reshape(3,1))
print("normalized:",normalized)

improvement = accuracy[:,3] - accuracy[:, 0]
print("Improvement      :", improvement)
print("Most improved    :", np.argmax(improvement) + 1)
# 4. Add weights to tasks [0.1, 0.2, 0.3, 0.4]
#    weighted score = accuracy * weights
#    then sum for each agent

weights = np.array([0.1, 0.2, 0.3, 0.4])

# Step 1 - multiply by weights
weighted_score = accuracy * weights
print("Weighted scores:\n", weighted_score)

# Step 2 - sum per agent (axis=1)
final_score = weighted_score.sum(axis=1)
print("Final weighted score per agent:", final_score)

# Step 3 - best agent
best_agent = np.argmax(final_score) + 1
print("Best agent:", best_agent)