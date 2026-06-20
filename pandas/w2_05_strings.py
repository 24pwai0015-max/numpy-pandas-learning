'''
        Summary Table
str.lower() Convert to lowercase.
str.upper() Convert to uppercase.
str.title() First letter capital.
str.strip() Remove leading/trailing spaces.
str.contains() Check if substring exists. 
str.replace() Find and replace text.
str.split() Split into multiple columns.
str.len() Get string length'''


# Real data has inconsistent text: extra spaces, mixed case, typos. Before analysis,
# you need .str methods to clean it.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Ali Khan', 'SARA AHMED', 'ahmed hussain', '  Fatima  '],
    'City': ['Lahore', 'Karachi', 'ISLAMABAD', 'Peshawar']
})
# df=messy data noe the goal is to to clean the data
print(df)
print("/"*40)
print("start the string operations:")
print("/"*40)

# Step 1 — Convert to Lowercase

df['Name']=df['Name'].str.lower()
df['City']=df['City'].str.lower()
print("df with lower case:\n",df)
print("/"*40)

# Step 2 — Convert to Uppercase
df['Name']=df['Name'].str.upper()
print("df with upper case:\n",df)
print("/"*40)
# Step 3 — Title Case (First Letter Capital)
df['City']=df['City'].str.title()
print(df)
print("/"*40)

# Step 4 — Remove Extra Spaces
df['Name']=df['Name'].str.strip()
print("df with strip case:\n",df)
print("/"*40)

df = pd.DataFrame({
    'Name': ['ali khan', 'sara ahmed', 'Ahmed hussain', 'fatima ali','None'],
    'Email': ['ali@gmail.com', 'sara@yahoo.com', 'ahmed@gmail.com', 'fatima@yahoo.com','none']
})
# print(df['Name'].str.upper())
# Check if Name contains 'ahmed'
print(df['Name'].str.contains('ahmed',case=False,na=False))
# filter rows

print(df[df['Name'].str.contains('ali')])

# Step 6 — Check if Column Contains a Substring (Case-Insensitive)
# 'Ahmed' with capital A
print(df['Name'].str.contains('Ahmed', case=False))

print("/"*40)
# step 7:replace the text

df['Email']=df['Email'].str.replace('@','&&')
print(df)
df['Name']=df['Name'].replace('None',np.nan)
print(df)
df['Name']=df['Name'].fillna('tara ahmad')
print(df)

print("/"*40)
# Step 8 — Split Text Into Separate Columns

df[['first','last']]=df['Name'].str.split(' ',expand=True)
print(df)

# expand ,break the lists into dataframe
# extraction of specific sub string

print("/"*40)

df['username']=df['Email'].str.split('&&').str[0]
print(df)

print("/"*100)
# str length

df['Name_Length'] = df['Name'].str.len()
print(df)
print("/"*100)
print("                                               \ttasks")
print("/"*100)
# import numpy as np
# import pandas as pd

df = pd.DataFrame({
    'Name': ['ali khan', 'SARA AHMED', '  ahmed hussain  ', 'Fatima Ali'],
    'Email': ['ali@GMAIL.COM', 'sara@yahoo.com', 'AHMED@GMAIL.COM', 'fatima@yahoo.com'],
    'Phone': ['123-456-7890', '098-765-4321', '555-1234-5678', '111-222-3333']
})

# 1. Convert Name to title case
df['Name']=df['Name'].str.title()
print(df)
print("+"*100)
# 2. Convert Email to lowercase
df['Email']=df['Email'].str.lower()
print(df)
print("+"*100)
# 3. Strip extra spaces from Name
df['Name']=df['Name'].str.strip()
print(df)
print("+"*100)
# 4. Check if Email contains 'gmail' (case-insensitive)
print(df['Email'].str.contains('gmail',case=False))
print("+"*100)
# 5. Replace 'gmail.com' with 'google.com' in Email
print(df['Email'].str.replace('gmail.com','google.com',case=False))
print("+"*100)
# 6. Extract username (before @) from Email into new column
df['username']=df['Email'].str.split('@').str[0]
print(df)
print("+"*100)
# 7. Check length of Name column
df['length']=df['Name'].str.len()
print(df)
# 8. Split Phone into area code and rest (split by first '-')
df[['area code','rest']]=df['Phone'].str.split('-',n=1,expand=True)
print(df)
print("+"*100)
# 9. Filter rows where Name contains 'ahmed' (case-insensitive)
print(df[df['Name'].str.contains('ahmed',case=False)])
# 10. Create a full cleaned version - title case Name, lowercase Email, stripped spaces

print("cleaned:\n",df)

'''
1. .str[0] — Indexing Into Split Results
When you split a string, you get a list of pieces. .str[0] grabs the first piece from each list.
In pandas, you do the same thing across a whole column using .str[0]:

2. case= Parameter — Only Works on Some .str Methods
This is the important distinction you hit yesterday.
case= IS supported on:
df['Name'].str.contains('ahmed', case=False)   # ✅ works
df['Name'].str.match('ahmed', case=False)        # ✅ works
case= is NOT supported on .str.replace() in the way you'd expect:
df['Email'].str.replace('gmail', 'google', case=False)  # ❌ TypeError
Why the difference? 
.contains() and .match() are search/check functions — case-insensitivity is a simple flag. 
.replace() is more complex because pandas treats your search text as a regex pattern by default, 
and case-insensitivity for regex needs a different approach (regex flags), not a simple case= argument.

3. How to Actually Do Case-Insensitive Replace
Option A — If your column is already lowercase (easiest):
df['Email'] = df['Email'].str.lower()  # normalize first
df['Email'] = df['Email'].str.replace('gmail.com', 'google.com')  # now safe
Option B — Use regex with the IGNORECASE flag:
pythonimport re
df['Email'] = df['Email'].str.replace('gmail.com', 'google.com', case=False, regex=True)
Wait — actually in newer pandas (1.x+), case=False does work, but only when regex=True:
pythondf['Email'] = df['Email'].str.replace('gmail', 'google', case=False, regex=True)
This is likely why your code errored — depending on your pandas version, you may have 
been missing regex=True, or your version doesn't support case on .replace() at all.

'''