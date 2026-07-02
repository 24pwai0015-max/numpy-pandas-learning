# '''groupby :
# Split data by category  →  Calculate something for each category  →  Show results'''

# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
#     'Class': ['A', 'B', 'A', 'B', 'A'],
#     'Math': [45, 78, 90, 55, 67]
# })
# # print(df)

# # print(df.groupby('Class')['Math'].mean())
# df['avg']=df.groupby('Class')['Math'].transform('mean')
# # print(df)
# '''In pandas, transform() is used to perform an operation on 
# each group while keeping the original DataFrame shape. It returns
# one value for each original row, unlike agg() which returns one value per group.'''
# # print("Sum:\n",df.groupby('Class')['Math'].sum())     # total per class
# # print("count:\n",df.groupby('Class')['Math'].count())    # how many students per class
# # print("max:\n",df.groupby('Class')['Math'].max())      # highest score per class
# # print("min:\n",df.groupby('Class')['Math'].min())      # lowest score per class

# #  Groupby on All Numeric Columns at Once

# print("-"*50)

# # print(df.groupby('Class').mean(numeric_only=True))
# # print(df.groupby('Class').mean(numeric_only=True))

# df2 = pd.DataFrame({
#     'Class': ['A', 'A', 'B', 'B'],
#     'Gender': ['M', 'F', 'M', 'F'],
#     'Math': [45, 78, 90, 55]
# })
# df2['math bonus']=df['Math'].apply(lambda x: x+5)
# print(df2)
# # multiple groupby

# # df2['avg']=df2.groupby(['Class','Gender'])['Math'].transform('mean')
# # print(df2)


# # df3 = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# # print(df3.columns)


import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan', 'Bilal', 'Ayesha'],
    'Class': ['A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Math': [45, 78, 90, 55, 67, 60, 85],
    'English': [67, 88, 55, 70, 60, 72, 90]
}
df = pd.DataFrame(data)

# 1. Group by 'Class' → average Math per class
print(df.groupby('Class')['Math'].mean())
# 2. Group by 'Class' → total English per class (sum)
print("Sum:\n",df.groupby('Class')['English'].sum())
# 3. Group by 'Class' → count students per class
print("count:\n",df.groupby('Class').count())
# 4. Group by 'Gender' → average Math AND English (both at once)
print(df.groupby('Gender')[['Math','English']].mean())
# 5. Highest Math score per Class
print("max:\n",df.groupby('Class')['Math'].max()) 
# 6. Lowest English score per Gender
print("min:\n",df.groupby('Gender')['English'].min())  
# 7. Group by BOTH 'Class' AND 'Gender' → average Math
print(df.groupby(['Class','Gender'])['Math'].mean())