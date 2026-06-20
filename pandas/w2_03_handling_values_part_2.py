import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'name': ['Ali', 'Sara', 'Ahmed'],
#     'math_score': [45, np.nan, 90],
#     'eng_score': [67, 88, 55]
# })
# df=df.set_index('name')
# # Rename specific columns
# df=df.rename(columns={'math_score':'Math'})
# print(df)

# # rename all columns at ones
# df.columns=['Name','Math','English']
# print(df)

# # rename the index

# df=df.rename(index={0:'std1',1:'std2',2:'std3'})
# print(df)
# # drop the row with nan value in column
# dropped=df.dropna(axis=0)
# print(dropped)

# # dropping columns
# df=df.drop('English',axis=1)
# print(df)

# df=df.drop(columns=['English'])
# print(df)

# df['Math']=df['Math'].fillna(df['Math'].mean())
# print(df)

# df=df.drop(columns=['Name','Math','English'])
# print(df)

# print("*"*50)
# # droping rows
# df=df.drop('std1',axis=0)
# print(df)


# # inplace parameter'''using this we donot need to save df again and again

# df.drop(columns=['Math'],inplace=True)



# # checking datatypes

# print(df.dtypes)

# # changing datatypes
# df = pd.DataFrame({
#     'Math': [45, 78, 90],
#     'Passed': [1, 0, 1]
# })

# # Convert int to float
# df['Math'] = df['Math'].astype(float)

# # Convert int to bool
# df['Passed'] = df['Passed'].astype(bool)

# print(df.dtypes)

# # 8 — Common Dtype Conversions
# # String to int (must have valid numbers)
# df['Age'] = df['Age'].astype(int)

# # Int to string
# df['ID'] = df['ID'].astype(str)

# # String to datetime
# df['Date'] = pd.to_datetime(df['Date'])

# # To category (saves memory for repeated values)
# df['Grade'] = df['Grade'].astype('category')

# # 9 — Why Dtypes Matter
# #  This FAILS if column is stored as text
# df['Math'] = df['Math'] + 10
# # TypeError if Math column is "object" type with text

# # Fix by converting first
# df['Math'] = df['Math'].astype(int)
# df['Math'] = df['Math'] + 10   # Now works
# # Real life use:

# # CSV files often load numbers as text — you must convert before doing math.


# # 10 — Real World Example
# df = pd.DataFrame({
#     'Name': ['Ali', 'Sara', 'Ahmed'],
#     'Age': ['20', '22', '21'],        # stored as text!
#     'Salary': ['50000', '60000', '55000']
# })

# print(df.dtypes)
# # Age and Salary are 'object' (text)

# # Convert to proper numeric types
# df['Age'] = df['Age'].astype(int)
# df['Salary'] = df['Salary'].astype(float)

# print(df.dtypes)
# # Now Age is int64, Salary is float64

# # Now math works
# df['Salary'] = df['Salary'] * 1.1   # 10% raise
# print(df)

# Summary Table
# TaskCodeRename columns>>>df.rename (columns={'old':'new'})
# Rename all columns>>>df.columns = [...]
# Drop column>>>df.drop('col', axis=1)
# Drop row>>>df.drop(0, axis=0)
# Check dtypes>>>df.dtypes
# Change dtype>>>df['col'].astype(type)
# Permanent change>>>inplace=True

# Today's Tasks


data = {
    'name': ['Ali', 'Sara', 'Ahmed', 'Fatima'],
    'math_score': ['45', '78', '90', '55'],
    'eng_score': ['67', '88', '55', '70'],
    'passed': [1, 1, 1, 0]
}
df = pd.DataFrame(data)

# 1. Check dtypes of all columns

print("dtypes details:\n",df.dtypes)

# 2. Rename 'name' to 'Name', 'math_score' to 'Math', 'eng_score' to 'English'
df.rename(columns={'name':'Name','math_score' :'Math','eng_score' : 'English'}, inplace=True)
print(df)


# 3. Convert 'Math' and 'English' from text to int
df['Math']=df['Math'].astype(int)
df['English']=df['English'].astype(int)
print(df)
# print("dtype details now:\n",df.dtypes)
# 4. Convert 'passed' column to bool
df['passed']=df['passed'].astype(bool)
print(df)
# 5. Verify all dtypes are now correct
print("dtype details now:\n",df.dtypes)
# 6. Add a 'Total' column (Math + English) - this should work now since they're int
df['Total']=df['Math']+df['English']
print(df)
# 7. Drop the 'passed' column
# print("dropped passed now:\n",df.drop(columns=['passed'],inplace=True))
# print(df)
df.drop(columns=['passed'], inplace=True)  
print(df)  # print separately
# 8. Rename row index 0 to 'Student_A'
df=df.rename(index={0:'Student_A'})
print(df)
# 9. Drop the row 'Student_A' using its new label
df=df.drop('Student_A',axis=0)
print(df)
