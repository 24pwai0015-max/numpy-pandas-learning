import numpy as np
# aggregation tasks and concepts 

'''def:Aggregation means summarizing many numbers into one single number.'''

'''example: Your monthly expenses:
# Mon: 500
# Tue: 200
# Wed: 800
# Thu: 300
# Fri: 150

# Total = 1950      ← aggregation (sum)
# Average = 390     ← aggregation (mean)
# Highest = 800     ← aggregation (max)
Lowest = 150      ← aggregation (min)
'''

# 1d array

agg=np.array([500,200, 800,300, 150])

print("sum:",agg.sum())
print("mean:",agg.mean())
print("max:",agg.max())
print("min:",agg.min())
print("standard dev:",agg.std())
'''What is std (Standard Deviation)?
   It tells you how spread out numbers are from the average'''
print("range:",agg.max()-agg.min())



'''The Axis Concept 0,1
This is where most people get confused. Let me explain clearly.
A 2D array is like a table:'''

marks=np.array([[25,34,56],
                [34,12,78],
                [67,89,90]])
# # print("data:\n",marks)
print(np.sum(marks,axis=0))
print(marks.sum(axis=0))

'''Visualize it as:
           Math  English  Science
Student 1:  45     78       90
Student 2:  82     34       67
Student 3:  23     56       88

Axis 0 — Goes DOWN
           Math  English  Science
Student 1:  45     78       90
             ↓      ↓        ↓
Student 2:  82     34       67
             ↓      ↓        ↓
Student 3:  23     56       88
             ↓      ↓        ↓
Total:      150    168      245

axis=0 collapses rows → gives one result per column'''
print("col aggregation")
sum_of_math=marks.sum(axis=0)[0]
print(sum_of_math)

sum_of_eng=marks.sum(axis=0)[1]
print(sum_of_eng)

sum_of_sci=marks.sum(axis=0)[2]
print(sum_of_sci)


# rows sum
print("rows summmmmmmmmmmm")

sum_of_math=marks.sum(axis=1)[0]
print(sum_of_math)

print("-"*50)

sum_of_eng=marks.sum(axis=1)[1]
print(sum_of_eng)

print("-"*50)

sum_of_sci=marks.sum(axis=1)[2]
print(sum_of_sci)


print("-"*50)

print("sum ",marks.sum(axis=1))

print("-"*50)


'''marks=np.array([[25,34,56],
                [34,12,78],
                [67,89,90]])'''
                
print("col math max value",marks.max(axis=0)[0])
print("col eng max value",marks.max(axis=0)[1])
print("col sci max value",marks.max(axis=0)[2])

print("-"*50)

'''What is argmax and argmin?
Regular max/min gives you the value.

argmax/argmin gives you the position of that value.
Real life example:

5 students gave exam. You want to know which student
scored highest, not just what the highest score was.'''

# columns
agg=np.array([[23,45,67],
              [45,67,89],
              [1,2,3]])


print(agg)
col_1=np.argmax(agg, axis=0)[0]
print(col_1)

print("-"*50)

col_2=np.argmax(agg, axis=0)[1]
print(col_2)

print("-"*50)

col_3=np.argmax(agg, axis=0)[2]
print(col_3)

print("-"*50)
print("rows argmax and argmin")
print("-"*50)

# rows


row_1=np.argmax(agg, axis=1)[0]
print(row_1)

print("-"*50)


row_2=np.argmax(agg, axis=1)[1]
print(row_2)

print("-"*50)

row_3=np.argmax(agg, axis=1)[2]
print(row_3)

print("-"*50)

'''
import numpy as np

# Response times of your AI agent in milliseconds
response_times = np.array([
    [120, 340, 89, 450, 210],   # Day 1
    [95,  280, 110, 390, 180],  # Day 2
    [150, 310, 95,  420, 200]   # Day 3
])

# Average response time per day
print("Avg per day:", response_times.mean(axis=1))

# Slowest response each day
print("Slowest per day:", response_times.max(axis=1))

# Fastest response each day
print("Fastest per day:", response_times.min(axis=1))

# Which request type is slowest on average
print("Slowest request type:", np.argmax(response_times.mean(axis=0)))

# Days where average response > 250ms (too slow)
avg = response_times.mean(axis=1)
slow_days = np.where(avg > 250)[0] + 1
print("Slow days:", slow_days)

np.where(avg > 250) Find where condition is True
[0]Extract array from tuple
+1Convert from 0-based to 1-based'''


# task 1 : Average response time per day
response_times = np.array([
    [120, 340, 89, 450, 210],   # Day 1
    [95,  280, 110, 390, 180],  # Day 2
    [150, 310, 95,  420, 200]   # Day 3
])
# task 1 : Average response time per day
print("Average response time per day",np.mean(response_times,axis=1))
print("-"*50)
# task 2 : slowest response time per day
print("slowest response time per day",np.max(response_times,axis=1))
print("-"*50)
# task 3:Which request type is slowest on average
print("request type is slowest on average ",np.argmax(response_times.mean(axis=0))+1)
print("-"*50)
# Days where average response > 250ms (too slow)
avg_res=np.mean(response_times,axis=1)
slow_days=np.where(avg_res>250)[0]+1

print("slow days:",slow_days)

#  Remaining in Aggregations

#1 — cumsum (Cumulative Sum)

# Running total — each value adds to the previous.


sales = np.array([200, 450, 300, 180, 390])

print(np.cumsum(sales))
# [200  650  950  1130  1520]
# Mon  +Tue  +Wed  +Thu   +Fri

# Real life use:
#  Track total revenue growing day by day.

# 2 — np.percentile

# Finds the value at a certain percentage point.

scores = np.array([45, 67, 78, 89, 92, 55, 71, 83])

print(np.percentile(scores, 25))   # 25th percentile
print(np.percentile(scores, 50))   # 50th = median
print(np.percentile(scores, 75))   # 75th percentile
print(np.percentile(scores, 90))   # Top 10% threshold

# Real life use:
# Find top 10% performing agents in your pipeline.

### 3 — np.median

# Middle value of sorted array.

arr = np.array([5, 12, 3, 18, 7])

print(np.mean(arr))     # 9.0  ← affected by extreme values
print(np.median(arr))   # 7.0  ← not affected

# Real life use:
#  Mean can be misleading if one value is very high. Median is more reliable.


# 4 — np.unique

# Finds all unique values.

responses = np.array([200, 404, 200, 500, 404, 200, 301])

print(np.unique(responses))
# [200 301 404 500]

# Count of each unique value
values, counts = np.unique(responses, return_counts=True)
print(values)   # [200 301 404 500]
print(counts)   # [3   1   2   1]

# Real life use:
# Count how many times each error code appeared in API logs.

# 5 np.clip

# Forces values to stay within a range.

scores = np.array([45, 102, 78, -5, 91, 110])

# Keep all values between 0 and 100
clipped = np.clip(scores, 0, 100)
print(clipped)
# [45 100  78   0  91 100]
# Real life use:
# Keep confidence scores between 0 and 1 in AI models.

# 6 — np.corrcoef

# Measures relationship between two arrays.

# Do more tokens = slower response?
tokens = np.array([100, 300, 500, 700, 900])
response_time = np.array([120, 280, 450, 620, 850])
correlation = np.corrcoef(tokens, response_time)[0][1]
print("Correlation:", correlation)
# 0.99 → very strong relationship
# Result is between -1 and 1:
# 1.0  → perfect positive relationship
# 0.0  → no relationship
# -1.0 → perfect negative relationship
# Real life use:
# > Check if token count affects response time in your AI agent.
## Priority for You Right Now
# Must know now         → cumsum, percentile, median

# Use when needed       → unique, clip
#  Updated Aggregations Checklist
# [x] sum, mean, min, max, std
# [x] axis=0 and axis=1
# [x] argmax and argmin
# [x] np.where
# [ ] cumsum
# [ ] percentile and median
# [ ] unique
# [ ] clip
# [ ] corrcoef'''v    

 













