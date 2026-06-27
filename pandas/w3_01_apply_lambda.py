# '''What is a Lambda Function?
# A lambda is just a mini, throwaway function written in one line. No def, no name needed.

# Regular Function (What You Already Know)
# def add_ten(x):
#     return x + 10

# print(add_ten(5)) 
# # 15
# Same Thing as a Lambda
# add_ten = lambda x: x + 10
# print(add_ten(5)) 
# # 15
# Breaking down the syntax:
# lambda   x: x + 10
#    ^     ^  ^
#    |     |  what to return
#    |     input parameter
#    keyword that means "anonymous function"
   
# Read it as: "a function that takes x and returns x + 10"'''



# # # Why Lambdas Matter With apply()
# # You rarely use lambdas standalone.
# # They shine when you need a quick custom function just for 
# # one line of code, especially inside apply().

# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Ali', 'Sara', 'Ahmed'],
#     'Math': [45, 78, 90],
#     'English':[12,34,56]
# })

# # Add 5 bonus points to every Math score
# df['Math'] = df['Math'].apply(lambda x: x + 5)
# # print(df)

# '''apply() Without Lambda (Using a Real Function)
# If the logic is more complex, use a regular function instead'''

# def grade(score):
#     if score>=90:
#         return 'A'
#     elif score>=78:
#         return 'B'
#     else:
#         return 'failed'
    
# df['Grade']=df['Math'].apply(grade)
# # print(df)

# '''apply() on an Entire Row (axis=1)
# So far we applied to a single column. You can also apply across 
# an entire row using axis=1:'''

# df['Total']=df.apply(lambda row: row['Math']+row['English'], axis=1)
# print(df)

# # df['Math'].apply(lambda x: ...)        x = single value from one column
# # df.apply(lambda row: ...,axis=1)       row = entire row, access any column with row['ColName']

# import pandas as pd

# data = {
#     'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
#     'Math': [45, 78, 90, 55, 67],
#     'English': [67, 88, 55, 70, 60]
# }
# df = pd.DataFrame(data)

# # 1. Use apply + lambda to add 10 bonus points to Math
# df['math bonus']=df['Math'].apply(lambda x: x+10)
# # print(df)
# # 2. Use apply + lambda to convert English scores to percentage (assume out of 100 already, just practice syntax: multiply by 1)
# df['eng percentage']=df['English'].apply(lambda x: (x)/(100)*(100) )
# # print(df)

# # 3. Write a named function 'pass_fail' that returns 'Pass' if score >= 50, else 'Fail'
# df['total']=df['Math']+df['English']
# # print(df)
# def pass_fail(score):
#     if score>=130:
#         return 'pass'
#     else:
#         return 'fail'
# df['result']=df['total'].apply(pass_fail)
# # print(df)
# #    Apply it to the Math column, store in new column 'Math_Result'
# def pass_fail(score):
#     if score>=50:
#         return 'pass'
#     else:
#         return 'fail'
# df['math result']=df['math bonus'].apply(pass_fail)
# # print(df)   
# # 4. Use apply with axis=1 to create a 'Total' column (Math + English)
# # df['total with lambda']=df.apply(lambda row: row['Math'] +row['English'],axis=1)
# # print(df)   
# # 5. Use apply with axis=1 and a lambda to create an 'Average' column ((Math + English) / 2)
# df['avg']=df.apply(lambda row: [row['Math']+row['English']/(2)],axis=1)
# print(df)
# # 6. Write a named function 'performance' that takes the Average and returns:
# #    'Excellent' if >= 80, 'Good' if >= 60, 'Needs Improvement' otherwise
# #    Apply it to the Average column
# # 7. Use apply + lambda on the Name column to get the length of each name
# # 8. BONUS: Apply your 'age_group' style logic (from the lesson) to categorize 
# #    students as 'Top Student' (Average >= 75) or 'Regular Student'

import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
    'Math': [45, 78, 90, 55, 67],
    'English': [67, 88, 55, 70, 60]
}
df = pd.DataFrame(data)

# 1. Add 10 bonus points to Math
df['math bonus'] = df['Math'].apply(lambda x: x + 10)

# 2. Eng percentage (syntax practice)
df['eng percentage'] = df['English'].apply(lambda x: (x) / (100) * (100))

# 3. pass_fail applied to Math (as the task asked)
def pass_fail(score):
    if score >= 50:
        return 'pass'
    else:
        return 'fail'

df['Math_Result'] = df['Math'].apply(pass_fail)

# 4. Total using apply + axis=1
df['Total'] = df.apply(lambda row: row['Math'] + row['English'], axis=1)

# 5. Average using apply + axis=1 (FIXED parentheses + no brackets)
df['Average'] = df.apply(lambda row: (row['Math'] + row['English']) / 2, axis=1)

# print(df)

# 6. Write a named function 'performance' that takes the Average and returns:
#    'Excellent' if >= 80, 'Good' if >= 60, 'Needs Improvement' otherwise
#    Apply it to the Average column
def performance(avg):
    if avg>=80:
        return 'excellent'
    elif avg>=60:
        return 'good'
    else:
        return 'need improvement'
    
df['performance']=df['Average'].apply(performance)
# print(df)

# 7. Use apply + lambda on the Name column to get the length of each name
df['name len']=df['Name'].apply(lambda x: len(x) )
# print(df)
#8: students as 'Top Student' (Average >= 75) or 'Regular Student'
def student_level(avg):
    if avg >= 75:
        return 'top student'
    else:
        return 'regular student'

df['student_level'] = df['Average'].apply(student_level)
print(df)