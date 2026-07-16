import pandas as pd
'''What is Merging?
So far you've worked with one DataFrame. In real world, data lives in multiple tables that need to be combined.
Students Table          Grades Table
--------------          ------------
ID | Name               ID | Math | English
1  | Ali                1  | 45   | 67
2  | Sara               2  | 78   | 88
3  | Ahmed              4  | 90   | 55  ← ID 4, not 3!
Notice: Student 3 (Ahmed) has no grades. Student 4 has grades but no name. How you handle these mismatches
is what the 4 join types control.'''

students = pd.DataFrame({
    "Student_ID":[101,102,103,104],
    "Name":["Ali","Ahmed","Sara","Ayesha"]
})

marks = pd.DataFrame({
    "Student_ID":[101,103,104,105],
    "Marks":[85,91,76,88]
})

# this is inner join merge return only common rows between dataframes
result=pd.merge(students,marks, on="Student_ID")
print(result
      )
# left join
result_1=pd.merge(students,marks, on="Student_ID",how="left")
print("students at left",result_1
      )


result_2=pd.merge(marks,students, on="Student_ID",how="left")
print("students at right",result_2
      )
# tasks 15 min
students = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Ali","Sara","Ahmed"]
})

marks = pd.DataFrame({
    "ID":[1,3],
    "Marks":[80,95]
})
'''Do the following:

Perform an Inner Join.
Perform a Left Join.
Which student gets NaN?
Why?'''
print("*"*50)
# inner join
inner=pd.merge(students,marks, on="ID")
print(inner)
print("*"*50)
left=pd.merge(students,marks, on="ID",how="left")
print(left)

# i got nan at id 2,with sara using left join,because no matched data,and left join retrive
# left table whone and retrieve matching rows from right table or list

# tasks 25 min?intermediate

employees = pd.DataFrame({
    "Emp_ID":[101,102,103,104],
    "Name":["Ali","Sara","John","Ayesha"]
})

departments = pd.DataFrame({
    "Emp_ID":[101,102,104],
    "Department":["HR","IT","Finance"]
})

'''Inner Join
Left Join
Which employee has no department?
Explain why.'''
print("+"*50)
print("task 1:\n")
inner2=pd.merge(employees,departments, on="Emp_ID")
print(inner2)
print("+"*50)
print("task 3:\n")
left2=pd.merge(employees,departments, on="Emp_ID",how="left")
print(left2)

# John (Emp_ID = 103) has no department because there is no matching Emp_ID 
# (103) in the departments DataFrame. A Left Join keeps all rows from the left
# DataFrame (employees) and adds matching values from the right DataFrame (departments).
# Since no match exists for John, Pandas fills the missing value with NaN.

# tasks complex lil bit
'''
Create your own two DataFrames.
Then:

Perform an Inner Join.
Perform a Left Join.
Explain the difference in your own words.'''
products = pd.DataFrame({
    "Product_ID":[1,2,3,4],
    "Product":["Mouse","Keyboard","Monitor","Laptop"]
})

prices = pd.DataFrame({
    "Product_ID":[1,2,4],
    "Price":[1200,3500,95000]
})
print("+"*50)
print(pd.merge(products,prices, on="Product_ID"))

print("+"*50)
last=pd.merge(products,prices, on="Product_ID",how="left")
print(last)

# nan=moniter has no price nan val


# new concepts loading

import pandas as pd

students = pd.DataFrame({
    'ID':   [1, 2, 3, 4],
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima']
})

grades = pd.DataFrame({
    'ID':      [1, 2, 4, 5],
    'Math':    [45, 78, 90, 55],
    'English': [67, 88, 55, 70]
})

print("Students:\n", students)
print("\nGrades:\n", grades)
inner = pd.merge(students, grades, on='ID', how='inner')
print(inner)
# Think of it as: A ∩ B
left = pd.merge(students, grades, on='ID', how='left')
print(left)
# Think of it as: Keep everything from A, add B where possible
right = pd.merge(students, grades, on='ID', how='right')
print(right)
# Think of it as: Keep everything from B, add A where possible

'''Join 4 — OUTER JOIN (Full Join)
"Keep ALL rows from BOTH tables, fill NaN where no match"'''
outer = pd.merge(students, grades, on='ID', how='outer')
print(outer)
'''Output:
   ID    Name  Math  English
0   1     Ali  45.0     67.0
1   2    Sara  78.0     88.0
2   3   Ahmed   NaN      NaN  ← from students only
3   4  Fatima  90.0     55.0
4   5     NaN  55.0     70.0  ← from grades only

Nobody gets dropped
Missing values filled with NaN
The union of both tables

Think of it as: A ∪ B'''

# with diff key columns

students2 = pd.DataFrame({
    'StudentID': [1, 2, 3],
    'Name':      ['Ali', 'Sara', 'Ahmed']
})

grades2 = pd.DataFrame({
    'GradeID': [1, 2, 4],
    'Math':    [45, 78, 90]
})

# left_on and right_on instead of on=
result = pd.merge(students2, grades2,
                  left_on  = 'StudentID',
                  right_on = 'GradeID',
                  how      = 'inner')
print(result)

# ?on multiple key columns

df1 = pd.DataFrame({
    'Name':  ['Ali', 'Ali', 'Sara'],
    'Class': ['A', 'B', 'A'],
    'Math':  [45, 78, 90]
})

df2 = pd.DataFrame({
    'Name':    ['Ali', 'Sara'],
    'Class':   ['A', 'A'],
    'English': [67, 88]
})

# Match on BOTH Name AND Class
result = pd.merge(df1, df2, on=['Name', 'Class'], how='inner')
print(result)

# In real projects: inner and left are used 90% of the time. right is rare 
# (just flip the tables and use left). outer is used when you can't afford to lose any data.

# final tasks

import pandas as pd
import numpy as np

students = pd.DataFrame({
    'ID':     [1, 2, 3, 4, 5],
    'Name':   ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
    'Class':  ['A', 'B', 'A', 'B', 'A']
})

grades = pd.DataFrame({
    'ID':      [1, 2, 4, 6, 7],
    'Math':    [45, 78, 90, 55, 67],
    'English': [67, 88, 55, 70, 60]
})

attendance = pd.DataFrame({
    'ID':         [1, 2, 3, 5, 6],
    'Attendance': [90, 85, 78, 92, 88]
})
print("*"*50)
print("claud tasks")
print("*"*50)
# INNER JOIN tasks
# 1. Inner join students + grades on ID
print("task 1:\n",pd.merge(students,grades,on="ID"))
#    → How many rows? Who got dropped and why?
# as you told me it acts like A INTERSECRION B drops are:id 3,5,6,7
# 2. Inner join students + attendance on ID
#    → Who is missing from the result?
print("*"*50)
print("task 2:\n",pd.merge(students,attendance,on="ID"))
# 4 and 6 are dropped
print("*"*50)
# LEFT JOIN tasks
# 3. Left join students + grades on ID
#    → Which students have NaN grades? Why?
print("task 3:\n",pd.merge(students,grades,on="ID",how="left"))
# the nan grades students are [ahmed and hassan]
# 4. Left join students + attendance on ID
#    → Who has NaN attendance?
print("task 4:\n",pd.merge(students,attendance,on="ID",how="left"))
print("*"*50)
# fatima has nan
# RIGHT JOIN tasks
# 5. Right join students + grades on ID
#    → Which grade records have no student name?
print("task 5:\n",pd.merge(students,grades,on="ID",how="right"))
# no ahmad and hassan 
print("*"*50)

# OUTER JOIN tasks
# 6. Outer join students + grades on ID
#    → How many total rows? What does each NaN mean?
print("task 6:\n",pd.merge(students,grades,on="ID",how="outer"))
# total 7 rows,it means there are no recods
print("*"*50)
# ADVANCED tasks
# 7. Three-way merge: inner join (students + grades),
#    then left join the result with attendance
#    → Build one complete table
result=pd.merge(students,grades, on="ID",how="inner")
# print("result:\n",result)
print("final result:\n",pd.merge(result,attendance, on="ID",how="left"))
print("*"*50)
# 8. Create two DataFrames with DIFFERENT key column names
#    and merge using left_on and right_on
students2 = pd.DataFrame({
    'StudentID': [1, 2, 3],
    'Name':      ['Ali', 'Sara', 'Ahmed']
})

grades2 = pd.DataFrame({
    'GradeID': [1, 2, 4],
    'Math':    [45, 78, 90]
})

# left_on and right_on instead of on=
result = pd.merge(students2, grades2,
                  left_on  = 'StudentID',
                  right_on = 'GradeID',
                  how      = 'inner')
print(result)
print("*"*50)
# 9. BONUS: Merge on TWO columns at once
#    Create DataFrames where you need both Name AND Class to uniquely identify a row
df1 = pd.DataFrame({
    'Name':  ['Ali', 'Ali', 'Sara'],
    'Class': ['A', 'B', 'A'],
    'Math':  [45, 78, 90]
})

df2 = pd.DataFrame({
    'Name':    ['Ali', 'Sara'],
    'Class':   ['A', 'A'],
    'English': [67, 88]
})

# Match on BOTH Name AND Class
result = pd.merge(df1, df2, on=['Name', 'Class'], how='inner')
print(result)
print("*"*50)