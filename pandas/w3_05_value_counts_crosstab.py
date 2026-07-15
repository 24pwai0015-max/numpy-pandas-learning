'''
value_counts() counts how many times each unique value appears in a column.
It's the fastest way to understand the distribution of any categorical column.

### Summary

**Count** → Number of occurrences.

  python
  df['Class'].value_counts()
  

**Proportion** → Fraction of the total (between 0 and 1).

  
  df['Class'].value_counts(normalize=True)


**Percentage** → Proportion × 100.


  df['Class'].value_counts(normalize=True) * 100


**Formula:**

* **Proportion = Count ÷ Total**
* **Percentage = (Count ÷ Total) × 100**

**Example:**
If there are **10 students** and **4 are in Class A**:

* Count = **4**
* Proportion = **4/10 = 0.4**
* Percentage = **40%**
'''

import pandas as pd

df = pd.DataFrame({
    'Name':      ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan', 'Bilal', 'Ayesha'],
    'Class':     [1, 2, 1, 2, 1, 2, 1],
    'Gender':    ['M', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Grade':     ['B', 'A', 'A', 'B', 'C', 'B', 'A'],
    'Math':      [45, 78, 90, 55, 67, 60, 85],
    'English':   [67, 88, 55, 70, 60, 72, 90]
})

print(df['Class'].value_counts())
# normalize,proportion
print(df['Class'].value_counts(normalize=True))
# in percentage
print(df['Class'].value_counts(normalize=True)*100)
# value_counts() With sort=False (Keep Original Order)
print(df['Grade'].value_counts(sort=False))
print(df['Class'].value_counts(sort=True))

import numpy as np

df2 = pd.DataFrame({'City': ['Lahore', 'Karachi', None, 'Lahore', None]})

# By default NaN is excluded
print(df2['City'].value_counts())

# Include NaN in the count
print(df2['City'].value_counts(dropna=False))

# Count combinations of Class + Gender
print(df[['Class', 'Gender']].value_counts())


print("*" * 50)

'''crosstab() is like value_counts() for two columns at once — it shows a frequency grid of how two categories overlap. 
Similar to pivot_table() but specifically for counting.'''

relation=pd.crosstab(df['Class'],df['Grade'])
print("relation 1: \n",relation)
print("*" * 50)
print(pd.crosstab(df['Class'],df['Grade'],margins=True))
print(pd.crosstab(df['Class'],df['Grade'],normalize=True)*100)
print(pd.crosstab(df['Class'],df['Grade'],normalize='index'))
print(pd.crosstab(df['Class'],df['Grade'],normalize='columns'))
# print(pd.crosstab(df['Class'],df['Grade']))



# Average Math score for each Class/Gender combination
print(pd.crosstab(
    df['Class'],
    df['Gender'],
    values  = df['Math'],
    aggfunc = 'mean'
))


import pandas as pd
import numpy as np

data = {
    'Name':    ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan', 'Bilal', 'Ayesha', 'Zara'],
    'Class':   ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Gender':  ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F'],
    'Grade':   ['B', 'A', 'A', 'B', 'C', 'B', 'A', 'C'],
    'Math':    [45, 78, 90, 55, 67, 60, 85, 72],
    'English': [67, 88, 55, 70, 60, 72, 90, 65],
    'City':    ['Lahore', 'Karachi', 'Lahore', None, 'Islamabad', 'Lahore', None, 'Karachi']
}
df = pd.DataFrame(data)
print("tasks")
print("*" * 50)

# value_counts() tasks
# 1. Count how many students are in each Class
print("task 1:\n",df['Class'].value_counts())
# 2. Count how many students got each Grade — show as percentage
print("task 2:\n",df['Grade'].value_counts(normalize=True)*100)
# 3. Count Gender distribution — sort=False
print("task 3:\n",df['Gender'].value_counts(sort=False))
# 4. Count City values — include NaN (dropna=False)
print("task 4:\n",df['City'].value_counts(dropna=False))
# 5. Count combinations of Class + Gender together
print("task 5:\n",df[['Class','Gender']].value_counts())

# crosstab() tasks
# 6. crosstab of Class vs Gender (raw counts)
print(pd.crosstab(df['Class'],df['Gender']))
# 7. crosstab of Class vs Grade — normalize by row (% within each class)
print(pd.crosstab(df['Class'],df['Grade'],normalize='index')*100)
# 8. crosstab of Class vs Gender — add margins=True
print(pd.crosstab(df['Class'],df['Gender'],margins=True))

# 9. crosstab of Class vs Gender — show average Math score (values + aggfunc)
print(pd.crosstab(df['Class'],df['Gender'],
                  values='Math',
                  aggfunc='mean'))
# BONUS: Load Titanic and:
# 10. value_counts() on Pclass, Sex, Embarked columns
# 11. crosstab of Pclass vs Sex (raw counts)
# 12. crosstab of Pclass vs Sex showing survival RATE (values=Survived, aggfunc='mean')   