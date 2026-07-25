'''After joins (combining by matching keys), concat() is simpler — 
it just stacks DataFrames together without needing a key column.

What is concat()?
Joins:   combine by matching a KEY column
concat:  just STACK tables together — no key needed

Two modes:

axis=0 → stack vertically (add more rows)
axis=1 → stack horizontally (add more columns)'''
import pandas as pd

df1 = pd.DataFrame({
    'Name':  ['Ali', 'Sara'],
    'Math':  [45, 78],
    'f_name':['ahmed','aqrar']
})

df2 = pd.DataFrame({
    'Name':  ['Ahmed', 'Fatima'],
    'Math':  [90, 55],
})

df3 = pd.DataFrame({
    'Name':  ['Hassan', 'Bilal'],
    'Math':  [67, 60],
})
# add rows
result=pd.concat([df1,df2],axis=0,)
print(result)
# ignore index
result=pd.concat([df1,df2],axis=0,ignore_index=True)
print(result)
print("+"*50)
# add columns
result1=pd.concat([df1,df2],axis=1)
print(result1)
print("+"*50)
# multile files cncat
result2=pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(result2)

# What Happens With Different Columns
df_a = pd.DataFrame({
    'Name': ['Ali', 'Sara'],
    'Math': [45, 78]
})

df_b = pd.DataFrame({
    'Name':    ['Ahmed', 'Fatima'],
    'English': [90, 55]   # different column!
})

result = pd.concat([df_a, df_b], axis=0, ignore_index=True)
print(result)
print(result.fillna(result.median(numeric_only=True)))

batches=pd.concat([df1,df2,df3],
                  axis=0,
                  keys=['batch 1','batch 2','batch 3'])
print(batches)


# ////////////////////////////////////////////////////////////////
'''just real example'''
# jan = pd.read_csv('january.csv')
# feb = pd.read_csv('february.csv')
# mar = pd.read_csv('march.csv')

# # Combine all months into one DataFrame
# all_data = pd.concat([jan, feb, mar], axis=0, ignore_index=True)


# tasks

import pandas as pd
import numpy as np

batch1 = pd.DataFrame({
    'Name':  ['Ali', 'Sara'],
    'Math':  [45, 78],
    'English': [67, 88]
})

batch2 = pd.DataFrame({
    'Name':  ['Ahmed', 'Fatima'],
    'Math':  [90, 55],
    'English': [55, 70]
})

batch3 = pd.DataFrame({
    'Name':  ['Hassan', 'Bilal'],
    'Math':  [67, 60],
    'English': [60, 72]
})

scores = pd.DataFrame({
    'Math':    [45, 78, 90],
    'English': [67, 88, 55]
})

names = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Ahmed']
})

extra_col = pd.DataFrame({
    'Science': [80, 75, 95]
})
print("task 1")
# axis=0 tasks
# 1. Concat batch1 + batch2 vertically (axis=0)
#    → How many rows in result?
print(pd.concat([batch1,batch2],axis=0,ignore_index=True))

# total 4 rows now
print("++"*40)
print("task 2")
# 2. Concat batch1 + batch2 + batch3 (all three)
#    → use ignore_index=True — check the index
print(pd.concat([batch1,batch2,batch3],axis=0,ignore_index=True))
# 3. Concat batch1 + batch2 WITHOUT ignore_index
#    → What happens to the index? Why is this a problem?
print("++"*40)
print("task 3")
print(pd.concat([batch1,batch2],axis=0))
# without this the couning order is not correct
# 4. Concat batch1 + batch2 with keys=['Batch1','Batch2']
#    → What does the multi-level index look like?
print("++"*40)
print("task 4")
batches=pd.concat([batch1,batch2],
                  axis=0,
                  keys=['batch 1','batch 2'])
print(batches)
# 5. Create df_a with Math column, df_b with English column (same Names)
#    Concat vertically — observe the NaN pattern
print("++"*40)
print("task 5")
df_a = pd.DataFrame({
    'Name': ['Ali', 'Sara'],
    'Math': [45, 78]
})

df_b = pd.DataFrame({
    'Name':    ['Ahmed', 'Fatima'],
    'English': [90, 55]   # different column!
})

result = pd.concat([df_a, df_b], axis=0, ignore_index=True)
print(result)
print(result.fillna(result.median(numeric_only=True)))

# axis=1 tasks
# 6. Concat names + scores horizontally (axis=1)
#    → Result should have Name, Math, English columns
print("++"*40)
print("task 6")
print(pd.concat([names,scores],axis=1))
# 7. Concat names + scores + extra_col horizontally
#    → Result should have 4 columns
print("++"*40)
print("task 7")
print(pd.concat([names,scores,extra_col],axis=1))
# 8. BONUS: Split the Titanic dataset into two halves
#    (first 445 rows and last 446 rows)
#    then concat them back together and verify shape matches original
print("++"*40)
print("task 8")

import pandas as pd

titanic = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Check original shape
print("Original shape:", titanic.shape)

# Split into two halves
first_half  = titanic.iloc[:445]
second_half = titanic.iloc[445:]

print("First half:", first_half.shape)
print("Second half:", second_half.shape)

# Concat back together
rejoined = pd.concat([first_half, second_half], axis=0, ignore_index=True)

# Verify shape matches original
print("Rejoined shape:", rejoined.shape)
print("Match:", rejoined.shape == titanic.shape)