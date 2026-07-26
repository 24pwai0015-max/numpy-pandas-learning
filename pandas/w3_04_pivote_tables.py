'''what are pivote tables:
Think of pivot_table() as groupby's more powerful sibling — instead of a flat list of
results, you get a 2D grid where two categories are cross-compared at once.'''

'''
With groupby() you get this — one dimension:
Passenger class
1    0.630
2    0.473
3    0.242
With pivot_table() you get this — two dimensions at once:
Sex              female      male
Passenger class                  
1                0.968     0.369
2                0.921     0.157
3                0.500     0.135
Same data, but now you can see class AND gender together in one clean grid.

The Basic Syntax
pd.pivot_table(df,
    values  = 'what to calculate',
    index   = 'rows',
    columns = 'columns',
    aggfunc = 'how to calculate'
)
Four parameters — that's all you need to know.'''

import pandas as pd

data = {
    'Name':    ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan', 'Bilal', 'Ayesha'],
    'Class':   ['A', 'B', 'A', 'B', 'A', 'B', 'A'],
    'Gender':  ['M', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Math':    [45, 78, 90, 55, 67, 60, 85],
    'English': [67, 88, 55, 70, 60, 72, 90],
    'result':['pass','fail','pass','pass','fail','pass','fail']
}
df = pd.DataFrame(data)
# print(df)
res=pd.pivot_table(df,
               values='Math',
               index='Class',
               columns=['Gender','result'],
               aggfunc='mean'
               )
print(res)

# # Sum instead of mean
# print(pd.pivot_table(df,
#     values  = 'Math',
#     index   = 'Class',
#     columns = 'Gender',
#     aggfunc = 'sum'
# ))

# # Count
# print(pd.pivot_table(df,
#     values  = 'Math',
#     index   = 'Class',
#     columns = 'Gender',
#     aggfunc = 'count'
# ))

# # Max
# print(pd.pivot_table(df,
#     values  = 'Math',
#     index   = 'Class',
#     columns = 'Gender',
#     aggfunc = 'max'
# ))

# res=pd.pivot_table(df,
#                values=['Math','English'],
#                index='Class',
#                columns='Gender',
#                aggfunc='mean',
#                margins='True'
#                )
# print(res)


# print(pd.pivot_table(df,
#     values    = 'Math',
#     index     = 'Class',
#     columns   = ['Gender','result'],
#     aggfunc   = 'mean',
#     fill_value = 10# ← replace NaN with 0
# ))


# # tasks
# import pandas as pd

# data = {
#     'Name':    ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan', 'Bilal', 'Ayesha'],
#     'Class':   ['A', 'B', 'A', 'B', 'A', 'B', 'A'],
#     'Gender':  ['M', 'F', 'M', 'F', 'M', 'M', 'F'],
#     'Math':    [45, 78, 90, 55, 67, 60, 85],
#     'English': [67, 88, 55, 70, 60, 72, 90]
# }
# df = pd.DataFrame(data)

# # 1. Pivot table: average Math score, rows=Class, columns=Gender
# res=pd.pivot_table(df,
#                values='Math',
#                index='Class',
#                columns='Gender',
#                aggfunc='mean'
#                )
# print(res)
# # 2. Pivot table: total (sum) English score, rows=Class, columns=Gender
# print("task 2:\n",pd.pivot_table(df,
#                values='English',
#                index='Class',
#                columns='Gender',
#                aggfunc='sum'
#                ))
# # 3. Pivot table: count of students, rows=Class, columns=Gender
# print("task 3:\n",pd.pivot_table(df,
#                values='Name',
#                index='Class',
#                columns='Gender',
#                aggfunc='count'
#                ))
# # 4. Pivot table: average Math AND English, rows=Class, columns=Gender
# res=pd.pivot_table(df,
#                values=['Math','English'],
#                index='Class',
#                columns='Gender',
#                aggfunc='mean',
               
#                )
# print(res)
# # 5. Pivot table: max Math score, rows=Class, columns=Gender, add margins=True
# # Max
# print(pd.pivot_table(df,
#     values  = 'Math',
#     index   = 'Class',
#     columns = 'Gender',
#     aggfunc = 'max',
#     margins='True'
# ))

# # 6. Pivot table: average Math, rows=Class, columns=Gender, fill_value=0
# print(pd.pivot_table(df,
#     values    = 'Math',
#     index     = 'Class',
#     columns   ='Gender',
#     aggfunc   = 'mean',
#     fill_value = 0
# ))
# # 7. BONUS: Load Titanic and create:
# #    - Survival rate by Passenger class (index) and Sex (columns)
# #    - Average Fare by Passenger class (index) and Embarked (columns)
# # resp=pd.pivot_table(df,
# #                    values='Age',
# #                    index='Passenger class',
# #                    columns='Sex',
# #                    aggfunc='mean',
# #                    fill_value=0,
# #                    )
# # print(resp)
# # rese=pd.pivot_table(df,
# #                    values='Fare',
# #                    index='Passenger class',
# #                    columns='Embarked',
# #                    aggfunc='mean',
# #                    fill_value=0,
# #                    )
# # print(rese)