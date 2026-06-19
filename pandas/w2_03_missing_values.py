import pandas as pd
import numpy as np
'''Real world data is never clean. Missing values are everywhere — empty cells, NaN, null. 
Before any analysis, you must handle them.'''
#   missing values looks like,
# nan is not a number


data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', None],
    'Math': [45, np.nan, 90, 55, 67],
    'English': [67, 88, np.nan, 70, 60],
    'Science': [80, 65, 95, np.nan, 72]
}
df = pd.DataFrame(data)
print(df)
# ......>>>>this is called crashed data


# step 1,, detect missing values
# result output will be true,false

print(df.isnull())
# false means have some value,true means there are no value

# count ,issing value per col
print(df.isnull().sum())


# Total missing values in whole dataset
print(df.isnull().sum().sum())


# step 2...notnull()it is opposite to isnull;;
missed_values=df.notnull()
print(missed_values)

# count ,total value per col
missed_values=df.notnull().sum()
print(missed_values)

# count ,total value per data
missed_values=df.notnull().sum().sum()
print(missed_values)

# Step 3 — Drop Missing Values
dropped=df.dropna()
print(dropped)

'''Output:
   Name  Math  English  Science
0   Ali  45.0     67.0     80.0
Only row 0 survives — everyone else had at least one missing value.'''


# Drop Only If All Values Missing

dropped=df.dropna(how='all')
print(dropped)

# Drop row Based on Specific Column

dropped=df.dropna(subset=['Math'])
print(dropped)


dropped=df.dropna(subset=['Name'])
print(dropped)


dropped=df.dropna(subset=['Science'])
print(dropped)

# Drop Columns Instead of Rows

dropped=df.dropna(axis=0)
print(dropped)

# Step 4 — Fill Missing Values (Better Than Dropping)

df['Math']=df['Math'].fillna(55)
df['English']=df['English'].fillna(df['English'].mean())
# Fill with median (better if there are outliers)
df['Science']=df['Science'].fillna(df['Science'].median())
# Fill text column with a placeholder
df['Name']=df['Name'].fillna('Tara')
print(df)
'''Why Mean vs Median?
scores = [45, 50, 48, 52, 1000]  # one outlier

mean   = 239   # heavily affected by outlier
median = 50    # not affected
Real life:

If data has extreme outliers, use median. Otherwise mean is fine'''


# Step 5 — Fill Entire DataFrame At Once
#  Fill all numeric columns with their own mean


filled=df.fillna(df.mean(numeric_only=True))
print(filled)


# Step 6 — Forward Fill and Backward Fill

# ffill — fill missing value with PREVIOUS value
df['Math']=df['Math'].fillna(Method='ffill')
print(df)

# ffill — fill missing value with PREVIOUS value
df['Math'] = df['Math'].ffill()

# bfill — fill missing value with NEXT value
df['Math'] = df['Math'].bfill()
print(df)


df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', None],
    'Math': [45, np.nan, 90, 55, 67],
    'English': [67, 88, np.nan, 70, 60],
    'Science': [80, 65, 95, np.nan, 72]
    
})
print(df.isnull().sum())
df['Name'] = df['Name'].fillna('Tara')
# print(df)
final_df = df.fillna(df.mean(numeric_only=True))
print(final_df)

print(final_df.isnull().sum())


data = {
    'Name': ['Ali', 'Sara', 'Ahmed', None, 'Hassan'],
    'Math': [45, np.nan, 90, 55, np.nan],
    'English': [67, 88, np.nan, 70, 60],
    'Science': [80, np.nan, 95, 50, 72]
}
df = pd.DataFrame(data)

# 1. Print isnull() for entire DataFrame
print(df.isnull())
# 2. Count missing values per column
print(df.isnull().sum())
# 3. Count total missing values in dataset
print(df.isnull().sum().sum())
# 4. Fill 'Name' missing values with 'Unknown'
df['Name'] = df['Name'].fillna('tara')
# 5. Fill 'Math' missing values with mean
df['Math'] = df['Math'].fillna(df['Math'].mean())
# 6. Fill 'English' missing values with median
df['English'] = df['English'].fillna(df['English'].median())
# 7. Fill 'Science' missing values with 0
df['Science'] = df['Science'].fillna(0)
# 8. Verify no missing values remain (isnull().sum() should be all 0)
print(df.isnull().sum())
# 9. Create a NEW dataframe (copy) and drop any row with missing values instead
# dropped_df = df.dropna()
# print(dropped_df)
#    Compare how many rows remain vs original
# import pandas as pd
# import numpy as np

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', None, 'Hassan'],
    'Math': [45, np.nan, 90, 55, np.nan],
    'English': [67, 88, np.nan, 70, 60],
    'Science': [80, np.nan, 95, 50, 72]
}
df = pd.DataFrame(data)

# Save original BEFORE any fillna
df_copy_for_drop = df.copy()

# ... your fillna tasks (4,5,6,7) happen on df ...

# Task 9 - use the saved copy
dropped_df = df_copy_for_drop.dropna()

print("Original rows :", df_copy_for_drop.shape[0])
print("After dropna  :", dropped_df.shape[0])
print(dropped_df)


print(df_copy_for_drop )

