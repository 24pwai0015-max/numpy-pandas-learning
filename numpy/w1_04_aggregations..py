import numpy as np
# # aggregation tasks ans concepts 

# '''def:Aggregation means summarizing many numbers into one single number.'''

# '''example: Your monthly expenses:
# Mon: 500
# Tue: 200
# Wed: 800
# Thu: 300
# Fri: 150

# Total = 1950      ← aggregation (sum)
# Average = 390     ← aggregation (mean)
# Highest = 800     ← aggregation (max)
# Lowest = 150      ← aggregation (min)'''

# # 1d array

# # agg=np.array([500,200, 800,300, 150])

# # print("sum:",agg.sum())
# # print("mean:",agg.mean())
# # print("max:",agg.max())
# # print("min:",agg.min())
# # print("standard dev:",agg.std())
# # '''What is std (Standard Deviation)?
# #    It tells you how spread out numbers are from the average'''
# # print("range:",agg.max()-agg.min())



# '''The Axis Concept 0,1
# This is where most people get confused. Let me explain clearly.
# A 2D array is like a table:'''

marks=np.array([[25,34,56],
                [34,12,78],
                [67,89,90]])
# # print("data:\n",marks)
print(np.sum(marks,axis=0))
print(marks.sum(axis=0))

# '''Visualize it as:
#            Math  English  Science
# Student 1:  45     78       90
# Student 2:  82     34       67
# Student 3:  23     56       88

# Axis 0 — Goes DOWN
#            Math  English  Science
# Student 1:  45     78       90
#              ↓      ↓        ↓
# Student 2:  82     34       67
#              ↓      ↓        ↓
# Student 3:  23     56       88
#              ↓      ↓        ↓
# Total:      150    168      245

# axis=0 collapses rows → gives one result per column'''
# print("col aggregation")
# sum_of_math=marks.sum(axis=0)[0]
# print(sum_of_math)

# sum_of_eng=marks.sum(axis=0)[1]
# print(sum_of_eng)

# sum_of_sci=marks.sum(axis=0)[2]
# print(sum_of_sci)


# # rows sum
# print("rows summmmmmmmmmmm")

# sum_of_math=marks.sum(axis=1)[0]
# print(sum_of_math)

# print("==========================================")

# sum_of_eng=marks.sum(axis=1)[1]
# print(sum_of_eng)

# print("==========================================")

# sum_of_sci=marks.sum(axis=1)[2]
# print(sum_of_sci)




# print("sum ",marks.sum(axis=1))


# '''marks=np.array([[25,34,56],
#                 [34,12,78],
#                 [67,89,90]])'''
                
# print("col math max value",marks.max(axis=0)[0])
# print("col eng max value",marks.max(axis=0)[1])
# print("col sci max value",marks.max(axis=0)[2])




