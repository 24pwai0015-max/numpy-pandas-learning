import pandas as pd
import numpy as np
import openpyxl

s=pd.Series(['90',80,70,60])
print(s)
'''# In Pandas, dtype: object means the Series contains 
# Python objects, most commonly strings (text data).'''
s=pd.Series([234,56,78,8])
print(s.size)
print(s.shape)
data={'name':'arsalan','marks':40}
s=pd.Series(data)
print(s)
data={
    'Name':['arsalan','afnan','sufyan'],
    'marks':[12,34,56]
}
df=pd.DataFrame(data)
print(df)
df.to_csv('data.csv',index=True)
df.to_excel('data.xlsx',index=False)

# import pandas as pd

# data = {
#     "Name": ["arsalan", "afnan", "sufyan"],
#     "Marks": [12, 34, 56]
# }

# df = pd.DataFrame(data)

# df.to_excel("students.xlsx", index=False)

# print("Excel file created successfully")
# # Task 1 - Create a DataFrame
data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
    'Math': [45, 78, 90, 55, 67],
    'English': [67, 88, 55, 70, 60],
    'Science': [80, 65, 95, 50, 72]
}

# # 1. Create the DataFrame
df=pd.DataFrame(data)
print("dataframe:\n",df)
# # 2. Print first 3 rows
print("first 3 rows:\n",df.head(3))
# # 3. Print shape and columns
print("shape:\n",df.shape)
print("cols:\n",df.columns)
# # 4. Print describe()
print("desc func:\n",df.describe())
# # 5. Add a 'Total' column (sum of all 3 subjects)
df["total"]=df['Math']+df['English']+df['Science']
print(df)
# # 6. Add an 'Average' column
df['avg']=df['total']/3
print(df)
# 7. Add a 'Result' column (Pass if Average > 60, else Fail)
df['result']=np.where(df['avg']>60, 'pass','fail')
print(df)
# 8. Sort by Total descending
sorted_df = df.sort_values('total', ascending=False)
print(sorted_df)
# 9. Print students who scored above 70 in Math
good=df[df['Math'] > 70]
print(good)


