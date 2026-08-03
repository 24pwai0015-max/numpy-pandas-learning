import pandas as pd

# Create DataFrames
employees = pd.DataFrame({
    'ID': [12, 13, 14, 15],
    'Name': ['ali', 'raza', 'ahmad', 'sara'],
    'department': ['Ai', 'cs', 'ds', 'arts']
})

salary = pd.DataFrame({
    'ID': [13, 14, 15, 16],
    'salary': [1200, 1300, 1400, 1500],
    'bonus': [5, 10, 15, 20]
})

projects = pd.DataFrame({
    'ID': [12, 15, 16, 13],
    'project_name': ['robo', 'nexusai', 'dtp', 'fit flow ai']
})

# Q1. Which employees have BOTH salary info AND project assignments?
result = pd.merge(employees, salary, on='ID', how='inner')
result = pd.merge(result, projects, on='ID', how='inner')
print("Q1:")
print(result)

# Q2. Show ALL employees — even those with no salary on record
result = pd.merge(employees, salary, on='ID', how='left')
print("\nQ2:")
print(result)

# Q3. Show ALL salary records — even if the employee name is missing
result = pd.merge(salary, employees, on='ID', how='left')
print("\nQ3:")
print(result)

# Q4. Show EVERYTHING from both employees and salaries
result = pd.merge(employees, salary, on='ID', how='outer')
print("\nQ4:")
print(result)

# Q5. Three-way merge:
# Get employees who have BOTH salary AND project data
result = pd.merge(employees, salary, on='ID', how='inner')
three_way = pd.merge(result, projects, on='ID', how='inner')
print("\nQ5:")
print(three_way)

# Q6. Summary using groupby + agg
summary = three_way.groupby('department').agg(
    average_salary=('salary', 'mean'),
    employee_count=('ID', 'count'),
    max_bonus=('bonus', 'max')
)

print("\nQ6:")
print(summary)