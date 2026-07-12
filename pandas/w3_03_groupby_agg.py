'''focus:
if i want sum,count,mean by group by i will use them separately,now if i want them in
one line.
we will use groupby.agg()'''

import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan', 'Bilal', 'Ayesha'],
    'Class': ['A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Math': [45, 78, 90, 55, 67, 60, 85],
    'English': [67, 88, 55, 70, 60, 72, 90]
}
df = pd.DataFrame(data)

# Multiple aggregations on one column
print(df.groupby('Class')['Math'].agg(['mean', 'max', 'min', 'sum', 'count']))
# print(df.groupby('Name')[['Math','English']].agg(['mean','sum','count']))

'''
 Different Aggregations for Different Columns
What if you want mean for Math but sum for English? Use a dictionary inside agg():'''

print(df.groupby('Class').agg({
    'Math':'sum',
    'English':'mean'
}))

#  Multiple Aggregations Per Column With a Dictionary

print(df.groupby('Class').agg({
    'Math':['sum','mean'],
    'English':['sum','mean']
}))

# Custom Column Names With Named Aggregations
# The multi-level column headers above can be messy. 
# You can give clean names using this syntax:


result=df.groupby('Class').agg(
    math_avg=('Math','mean'),
    math_max=('Math','max')
)
# print(result)
''' agg() on Multiple Groups
Combine everything — group by two columns AND run multiple aggregations:'''

resultt=df.groupby(['Class','Gender']).agg(
    math_avg=('Math','mean'),
    math_max=('Math','max'),
    English_max=('English','max')
)
print(resultt)


import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan', 'Bilal', 'Ayesha'],
    'Class': ['A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Math': [45, 78, 90, 55, 67, 60, 85],
    'English': [67, 88, 55, 70, 60, 72, 90]
}
df = pd.DataFrame(data)

# 1. Group by Class → get mean, max, min for Math all at once using agg()
print("task 1:\n",df.groupby('Class')['Math'].agg(['mean','sum','max','min']))
# 2. Group by Gender → get mean for Math, sum for English (different agg per column)
print("task 2:",df.groupby('Gender').agg({
    'Math':'mean',
    'English':'sum'
}))
# 3. Group by Class → get mean AND max for Math, min AND sum for English
print("task 3:",df.groupby('Class').agg({
    'Math':['mean','max'],
    'English':['min','sum']
}))
# 4. Group by Class → use named aggregations:
print("task 4:",df.groupby('Gender').agg(
    Math_max=('Math','max'),
    English_max=('English','max'),
    Math_avg=('Math','mean'),
    English_min=('English','min'),
    English_sum=('English','sum'),))
#
# 5. Group by BOTH Class AND Gender → named aggregations:
print("task 5:",df.groupby(['Gender','Class']).agg(
    Math_max=('Math','max'),
    English_max=('English','max'),
    Math_avg=('Math','mean'),
    English_min=('English','min'),
    English_sum=('English','sum'),))
# 6. BONUS: Load your cleaned Titanic dataset and run:
#    df.groupby('Passenger class').agg(
#        avg_age    = ('Age', 'mean'),
#        max_fare   = ('Fare', 'max'),
#        survival   = ('Survived', 'mean'),
#        count      = ('Survived', 'count')
#    )