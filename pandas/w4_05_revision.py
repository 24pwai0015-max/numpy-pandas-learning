# Create these three DataFrames yourself:

# employees — ID, Name, Department
# salaries  — ID, Salary, Bonus
# projects  — ID, Project_Name

# Then answer these questions using the RIGHT join each time:

# Q1. Which employees have BOTH salary info AND project assignments?
#     (only complete records)

# Q2. Show ALL employees — even those with no salary on record
#     (keep everyone, NaN is okay)

# Q3. Show ALL salary records — even if the employee name is missing
#     (salary data is the priority)

# Q4. Show EVERYTHING from both employees and salaries
#     (nobody gets dropped)

# Q5. Three-way merge:
#     Get employees who have BOTH salary AND project data
#     (chain two merges together)

# Q6. Create a summary using groupby + agg on your merged result:
#     - Average salary per department
#     - Count of employees per department
#     - Max bonus per department


import pandas as pd

employees=pd.DataFrame({'ID':[12,13,14,15],
                        'Name':['ali','raza','ahmad','sara'],
                        'department':['Ai','cs','ds','arts']})
salary=pd.DataFrame({'ID':[13,14,15,16],
                       'salary':[1200,1300,1400,1500],
                       'bonus':[5,10,15,20]})
projects=pd.DataFrame({'ID':[12,15,16,13],
                       'project_name':['robo','nexusai','dtp','fit flow ai']})
# Then answer these questions using the RIGHT join each time:
# Q1. Which employees have BOTH salary info AND project assignments?
#     (only complete records)

result=pd.merge(employees,salary, on='ID',how='inner')
print(result)

# Q2. Show ALL employees — even those with no salary on record
#     (keep everyone, NaN is okay)

result=pd.merge(employees,salary, on='ID',how='left')
print(result)

# Q3. Show ALL salary records — even if the employee name is missing
#     (salary data is the priority)


result=pd.merge(salary,employees, on='ID',how='left')
print(result)

# Q4. Show EVERYTHING from both employees and salaries
#     (nobody gets dropped)

result=pd.merge(salary,employees, on='ID',how='outer')
print(result)

# Q5. Three-way merge:
#     Get employees who have BOTH salary AND project data
#     (chain two merges together)


result=pd.merge(employees,salary, on='ID',how='inner')
print(result)

three_way=pd.merge(result,projects, on='ID',how='inner')
print(three_way)

employees=pd.DataFrame({'ID':[12,13,14,15],
                        'Name':['ali','raza','ahmad','sara'],
                        'department':['Ai','cs','ds','arts']})
salary=pd.DataFrame({'ID':[13,14,15,16],
                       'salary':[1200,1300,1400,1500],
                       'bonus':[5,10,15,20]})
projects=pd.DataFrame({'ID':[12,15,16,13],
                       'project_name':['robo','nexusai','dtp','fit flow ai']})
# Q6. Create a summary using groupby + agg on your merged result:
#     - Average salary per department
#     - Count of employees per department
#     - Max bonus per department