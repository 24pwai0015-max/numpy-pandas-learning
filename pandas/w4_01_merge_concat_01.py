import pandas as pd

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