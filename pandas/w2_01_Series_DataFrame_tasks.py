# import pandas as pd
# import numpy as np
# # Task 1 - Create a DataFrame
# data = {
#     'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
#     'Math': [45, 78, 90, 55, 67],
#     'English': [67, 88, 55, 70, 60],
#     'Science': [80, 65, 95, 50, 72]
# }

# # 1. Create the DataFrame
# df=pd.DataFrame(data)
# print("dataframe:\n",df)
# # 2. Print first 3 rows
# print("first 3 rows:\n",df.head(3))
# # 3. Print shape and columns
# print("shape:\n",df.shape)
# print("cols:\n",df.columns)
# # 4. Print describe()
# print("desc func:\n",df.describe())
# # 5. Add a 'Total' column (sum of all 3 subjects)
# df["total"]=df['Math']+df['English']+df['Science']
# print(df)
# # 6. Add an 'Average' column
# df['avg']=df['total']/3
# print(df)
# # 7. Add a 'Result' column (Pass if Average > 60, else Fail)
# df['result']=np.where(df['avg']>60, 'pass','fail')
# print(df)
# # 8. Sort by Total descending
# sorted_df = df.sort_values('total', ascending=False)
# print(sorted_df)
# # 9. Print students who scored above 70 in Math
# good=df[df['Math'] > 70]
# print(good)

# task set 2

import pandas as pd
import numpy as np

data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
    'Math': [45, 78, 90, 55, 67],
    'English': [67, 88, 55, 70, 60],
    'Science': [80, 65, 95, 50, 72]
}

# Task 1 - Create DataFrame
df = pd.DataFrame(data)

# Task 2 - Set 'Name' as index (so names become row labels)
print(pd.DataFrame(data),index='Name')
print(df)
# Task 3 - Print the DataFrame after setting index

# Task 4 - Access Ahmed's Math score using loc-style label
#          (use df.loc since you now have labels)

# Task 5 - Print transpose of df (df.T)

# Task 6 - Rename 'Math' column to 'Mathematics'

# Task 7 - Add a 'Grade' column using apply():
#          A if average > 75
#          B if average between 60-75
#          C if below 60
#          (calculate average first from Mathematics, English, Science)

# Task 8 - Print value_counts() of Grade column

# Task 9 - Print unique grades

# Task 10 - Reset index back to default (0,1,2...)

# Task 11 - Create a Series of only 'English' scores with Name as labels

# Task 12 - From that Series, get Sara's English score using label