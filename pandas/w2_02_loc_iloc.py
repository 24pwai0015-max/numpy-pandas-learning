'''What is loc?
loc selects data using labels (names).'''
import pandas as pd

df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Ahmed'],
    'Math': [45, 78, 90],
    'English': [67, 88, 55]
})
'''      

Name     Math  English         
Ali      45       67
Sara     78       88
Ahmed    90       55
'''

print(df)
print(df.loc[0,'Name'])

'''in this output,man confuses during the
differentiation of index and lables,index 
are only integers while lables are names,
integers may be numbers,strings etc'''


# custom indexing

df=df.set_index('Name')
print(df)

print(df.loc['Sara','Math'])


'''What is iloc?
iloc selects data using positions (numbers) — always works, regardless of labels.
'''
# iloc uses position numbers (starts from 0)
print(df.iloc[0, 0])    
print(df.iloc[1, 1])   
print("-"*50) 


# by lables
print(df.loc['Sara','English'])
# by positions
print(df.iloc[1,1])
print("-"*50) 

print(df.iloc[0])
print(df.loc['Ali'])
print("-"*50) 

# selecting multiple rows through loc and iloc

print(df.loc[['Ali','Sara']])
print("-"*50)
print(df.iloc[[0,1]])


print("-"*50) 






# iloc slicing — EXCLUDES last position (like Python lists)
print("start")
print(df.iloc[0:0])
print("-"*50)
print(df.iloc[0:1])
print("-"*50)
print(df.iloc[0:2])
print("-"*50)
print(df.iloc[0:3])
print("-"*50)
# print(df.iloc[0:4]) same result as 0:3
print("-"*50)
# Gets row 0 and row 1, NOT row 2'''

'''Slicing With loc and iloc
 loc slicing — INCLUDES last label
print(df.loc['Ali':'Sara'])'''
print("loc start slicing")
print(df.loc['Ali'])
print(df.loc['Ali':'Sara'])
print(df.loc['Ali':'Ahmed'])

print("-"*50)
# select all rows with specific col

print(df.loc[:,'Math'])
print("-"*20)
# print(df.loc[:,'Science'])
print("-"*20)
print(df.loc[:,'English'])
print("-"*30)
print("select all col with specific row")
print("-"*30)
# select all col with specific row

print(df.loc['Ali':'Ahmed',:])
# print(df.loc['Sara',:])

'''Conditional Selection With loc
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Ahmed'],
    'Math': [45, 78, 90]
})

# Get rows where Math > 60
print(df.loc[df['Math'] > 60])
This is actually the most common real-world use of loc.'''


'''Simple Rule
Use iloc → when you don't care about names, just position
Use loc  → when you want to select by name OR by condition

Real World Usage
Use iloc when:
 Getting first 5 rows (position based)
df.iloc[0:5]

# Getting last row
df.iloc[-1]

Looping through rows by position
for i in range(len(df)):
    df.iloc[i]
Use loc when:
You have meaningful names as index
df.loc['Ahmed']

# Filtering with conditions (MOST COMMON USE)
df.loc[df['Math'] > 60]

# Selecting specific columns by name
df.loc[:, 'Math']

Honest Truth — Most Used in Real Work
90% of the time in real data analysis you use:
df[df['column'] > value]     ← shortcut, same as loc condition

loc is used mostly for conditional filtering
iloc is used mostly for position-based slicing

My Recommendation For You
Beginner stage (now)     → Practice both equally to understand them
Real projects (later)    → You'll mostly use:
                            - direct filtering: df[df['col'] > 5]
                            - loc for named index access
                            - iloc rarely, only for position-based needs

Quick Decision Guide
Do you have a column name?           → use loc
Do you have a row/column position?   → use iloc
Are you filtering with a condition?  → use loc (or shortcut)
# '''

# # task set 1
import pandas as pd

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
    'Math': [45, 78, 90, 55, 67],
    'English': [67, 88, 55, 70, 60],
    'Science': [80, 65, 95, 50, 72]
}
df = pd.DataFrame(data)

# 1. Set 'Name' as index
df=df.set_index('Name')
print(df)
# 2. Get Ahmed's Science score using loc
print(df.loc['Ahmed','Science'])
# 3. Get Ahmed's Science score using iloc
print(df.iloc[2,2])
# 4. Get all subjects for Sara using loc ,specific row and all colmns
print(df.loc['Sara',:])

# 5. Get all subjects for row position 1 using iloc
print(df.iloc[1,:])
# 6. Get Math and English columns for Ali and Fatima using loc
print(df.loc[['Ali','Fatima'],['Math','English']])
# 7. Get first 3 rows using iloc
print(df.iloc[0:3])
# 8. Get rows from 'Sara' to 'Hassan' using loc (check what's included)
print(df.loc['Sara':'Hassan'])
# 9. Get all students with Math > 60 using loc
df=df.loc[df['Math']>60]
print(df)
# 10. Get last row using iloc (use -1)
print(df.iloc[-1])