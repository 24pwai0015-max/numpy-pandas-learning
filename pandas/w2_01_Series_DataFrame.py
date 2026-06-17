# '''What is Pandas?
# Built on top of NumPy, designed for working with tables (like Excel but in code).'''

# # Series  One Column of Data
import pandas as pd

#Series is like a single column
marks = pd.Series([45, 78, 90, 55, 67])
print("series:one column>>\n",marks)
# Output:
# 0    45
# 1    78
# 2    90
# 3    55
# 4    67
# dtype: int64
# Notice — it has index (0,1,2,3,4) automatically.
s=pd.Series([12,34,56,76])
print(s)
print(s.values)
print(s.index)
# indexing concept>>>>=start,stop,step
'''series from dict'''
data = {'Math': 45, 'English': 67, 'Science': 80}
s = pd.Series(data)
print(s)

# np operations
s = pd.Series([10, 20, 30, 40])

print(s + 5)        # adds 5 to all
print(s * 2)         # multiply all
print(s[s > 20])     # boolean masking works here too!
print(s.mean())      # 25.0
print(s.sum())       # 100
'''What are Labels?
Labels are the names given to rows and columns instead of just numbers.

Without Labels (Just Numbers)
import numpy as np

arr = np.array([45, 78, 90])
print(arr[0])   # 45 ← only number position works
NumPy arrays only have positions (0,1,2...) — no names.

With Labels (Pandas)
import pandas as pd

marks = pd.Series([45, 78, 90], index=['Math', 'English', 'Science'])
print(marks)
Output:
Math       45
English    78
Science    90
Now 'Math', 'English', 'Science' are labels — you can use names instead of just numbers.
print(marks['Math'])    # 45 ← using label
print(marks[0])         # 45 ← position still works too

Real Life Analogy
Without labels = phone contacts saved as numbers only
                  0123456789, 0123456788...

With labels = phone contacts saved with names
              "Mom", "Boss", "Friend"
Much easier to understand with labels.

In DataFrame — Two Types of Labels
df = pd.DataFrame({
    'Math': [45, 78, 90],
    'English': [67, 88, 55]
}, index=['Ali', 'Sara', 'Ahmed'])

print(df)
Output:
       Math  English
Ali      45       67
Sara     78       88
Ahmed    90       55
Column labels → 'Math', 'English'    (top)
Row labels    → 'Ali', 'Sara', 'Ahmed' (side)'''

# Custom Index
marks = pd.Series([45, 78, 90], index=['Math', 'English', 'Science'])
print("custom indexing  :\n",marks)
# Output:
'''Math       45
English    78
Science    90
dtype: int64
'''
# DataFrame — Multiple Columns (Like Excel Table)
data = {
    'Name': ['Ali', 'Sara', 'Ahmed'],
    'Math': [45, 78, 90],
    'English': [67, 88, 55]
}

df = pd.DataFrame(data)
print("col to dataframe :\n",df)
'''Output:
    Name  Math  English
0    Ali    45       67
1   Sara    78       88
2  Ahmed    90       55

Series vs DataFrame
Series    → ONE column        (like a list with labels)
DataFrame → MULTIPLE columns  (like a full table)'''

# Creating DataFrame — Different Ways

# Way 1 - From dictionary
data = {
    'Name': ['Ali', 'Sara', 'Ahmed'],
    'Math': [45, 78, 90],
    'English': [67, 88, 55]
}
df = pd.DataFrame(data)
print("way 1 throgh dict:\n",df)

# Way 2 - From list of lists
data2 = [
    ['Ali', 45, 67],
    ['Sara', 78, 88],
    ['Ahmed', 90, 55]
]
df2 = pd.DataFrame(data2, columns=['Name', 'Math', 'English'])
print("way 2 through list of lists:\n",df2)

'''What is CSV?
CSV = Comma Separated Values
It is a simple text file format for storing tabular data (rows and columns).

How It Looks
A normal Excel table:
Name      Math    English
Ali       45      67
Sara      78      88
Ahmed     90      55

Same data as CSV file (.csv):
Name,Math,English
Ali,45,67
Sara,78,88
Ahmed,90,55
Just commas separating values, one row per line.

Why CSV is Used:

Very small file size
Opens in Excel, Notepad, any text editor
Easy for programs to read
Universal format — works everywhere
Most datasets online are in CSV format

Real Example
Open Notepad and type this:
Name,Age,City
Ali,20,Lahore
Sara,22,Karachi
Ahmed,21,Islamabad
Save as data.csv — that's it. A real CSV file.'''

# Reading CSV in Pandas
import pandas as pd

df = pd.read_csv('data.csv')
print(df)
'''Output:
    Name  Age      City
0    Ali   20    Lahore
1   Sara   22  Karachi
2  Ahmed   21  Islamabad
Pandas automatically converts CSV into a clean table.

Saving DataFrame to CSV
df.to_csv('output.csv', index=False)
index=False means don't save the row numbers (0,1,2) into the file.

Where You Will Use CSV
- Kaggle datasets are mostly CSV
- Exporting your analysis results
- Sharing data between programs
- Database exports
- API responses sometimes give CSV


Simple rule:

CSV = plain table data, no styling, universal format.


What is Excel?
Excel is spreadsheet software made by Microsoft for 
creating and managing tables, calculations, and charts.

How It Looks
┌─────────┬──────┬──────────┐
│  Name   │ Age  │   City   │
├─────────┼──────┼──────────┤
│  Ali    │  20  │  Lahore  │
│  Sara   │  22  │ Karachi  │
│  Ahmed  │  21  │Islamabad │
└─────────┴──────┴──────────┘
File extension: .xlsx or .xls

What Makes Excel Special
✅ Colors and formatting
✅ Built-in formulas (SUM, AVERAGE, IF)
✅ Multiple sheets in one file
✅ Charts and graphs
✅ Can have merged cells
✅ Conditional formatting


Reading Excel in Pandas
import pandas as pd

# Read excel file
df = pd.read_excel('students.xlsx')
print(df)

# If multiple sheets, specify which one
df = pd.read_excel('students.xlsx', sheet_name='Sheet1')

You Need Extra Library for Excel
# pip install openpyxl
CSV needs no extra library. Excel does.

Saving DataFrame to Excel
df.to_excel('output.xlsx', index=False)


Simple Rule

Excel = software with formatting and formulas

CSV = plain data file that Excel can also open'''


