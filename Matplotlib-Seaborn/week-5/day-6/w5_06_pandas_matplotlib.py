import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
)
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Fare'] = titanic['Fare'].fillna(titanic['Fare'].median())
### ==============================================================================
### DECONSTRUCTING: titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])
### ==============================================================================

# ------------------------------------------------------------------------------
# 1. titanic['Embarked'] (Target Series Selection)
# ------------------------------------------------------------------------------
# • 'titanic' is the primary DataFrame.
# • Bracket notation ['Embarked'] isolates that single column as a Pandas Series.
# • This categorical column contains boarding port codes:
#     - 'S' = Southampton
#     - 'C' = Cherbourg
#     - 'Q' = Queenstown
#     - NaN = Missing values that require imputation before modeling or plotting.

# ------------------------------------------------------------------------------
# 2. .mode() (Categorical Central Tendency)
# ------------------------------------------------------------------------------
# • Calculates the statistical mode: the value that occurs with highest frequency.
# • Why .mode() instead of .mean() or .median()?
#     - .mean() and .median() require numerical continuous data.
#     - 'Embarked' contains text strings; strings cannot be averaged or divided.
#     - The mode is the standard metric for imputing categorical/text nulls.

# ------------------------------------------------------------------------------
# 3. [0] (Extracting the Scalar String from the Series)
# ------------------------------------------------------------------------------
# • Unlike .mean() or .median() which return a single float/int number,
#   Pandas .mode() ALWAYS returns a 1D Pandas Series, not a raw string.
# • Reason: Datasets can have multiple modes (ties for first place).
# • Example Series returned by titanic['Embarked'].mode():
#       Index    Value
#       0        'S'
#       dtype: object
# • Writing .mode()[0] accesses index position 0 to unpack the raw string:
#       titanic['Embarked'].mode()[0]  -->  'S'
# • Passing a raw string into .fillna() avoids shape mismatch errors.

# ------------------------------------------------------------------------------
# 4. .fillna(...) (Missing Value Imputation Engine)
# ------------------------------------------------------------------------------
# • Iterates over every element in the 'Embarked' Series:
#     - Valid strings ('S', 'C', 'Q') are left completely untouched.
#     - Missing slots ('NaN') are replaced with the value passed in ('S').
# • Returns a completely new Pandas Series with zero missing values.

# ------------------------------------------------------------------------------
# 5. titanic['Embarked'] = ... (Reassignment & In-Place Safety)
# ------------------------------------------------------------------------------
# • .fillna() does NOT mutate the original DataFrame in memory by default.
# • Reassigning back to titanic['Embarked'] overwrites the messy column with
#   the newly filled Series inside the original DataFrame.
# • Rule: Use reassignment OR use inplace=True; never mix both[cite: 1].
#   Incorrect: titanic['Embarked'] = titanic['Embarked'].fillna('S', inplace=True)
#   (That evaluates to None and deletes the entire column)[cite: 1]!

titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])
sns.set_style('whitegrid')

print("age null values confirmation:\n",titanic['Age'].isnull().sum())
print("fare null values confirmation:\n",titanic['Fare'].isnull().sum())
print("Embarked null values confirmation:\n",titanic['Embarked'].isnull().sum())

# tasks

# 1. Use groupby to find average Fare per Pclass
#    Chart it using .plot(kind='bar')
# print("average Fare:\n",titanic.groupby('Pclass')['Fare'].mean().plot(kind='bar',x='Pclass',y='Fare'))
# plt.show()

result=titanic.groupby('Pclass')['Fare'].mean()
print(result)
plt.figure(figsize=(10,6))
plt.title("pclass vs fare avg",fontsize=16,fontweight='bold',color="#8A0404")
result.plot(kind='bar',color="#C31616")
plt.xlabel='Pclass'
plt.ylabel='Fare'
plt.show()
# 2. Use groupby to find average Age per Embarked port
#    Chart it using plt.bar() with .index and .values
avg_age=titanic.groupby('Embarked')['Age'].mean()
print(avg_age)
plt.bar(avg_age.index,avg_age.values)
plt.xlabel='Embarked'
plt.ylabel='Age'
plt.title("Average Age per Embarked Port")
plt.show()


# 3. Use groupby(['Pclass','Sex']) to find survival rate
#    Convert to a pivot_table instead, then chart with sns.heatmap()
survival_avg=titanic.groupby(['Pclass','Sex'])['Survived'].mean()
survival_pivote=survival_avg.unstack()
sns.heatmap(data=survival_pivote,annot=True,fmt='0.2f',vmax=1,vmin=0)
plt.title("Survival Rate by Passenger Class and Sex")
plt.xlabel='Sex'
plt.ylabel='Pclass'
plt.show()

# 4. Use value_counts() on 'Embarked'
#    Chart it as a pie chart with percentages

# # # Create pie chart
# # plt.figure(figsize=(8, 6))
# # # 8 wdth
# # # 6 height
# # plt.pie(sizes, 
# #         labels=labels, 
# #         colors=colors,
# #         autopct='%1.1f%%',   # show percentage
# #         startangle=90,       # rotate so first slice starts at top
# #         shadow=True)         # add shadow for 3D effect
colors=["green","red","blue"]
counts=titanic['Embarked'].value_counts()
print(counts)
plt.pie(counts,labels=counts.index,colors=colors,autopct='%1.1f%%',startangle=90,shadow=True)
plt.show()
# 5. Use agg() to get survival_rate, avg_age, avg_fare, count per Pclass
#    Print the full summary table
#    Then chart just the survival_rate column as a bar chart

# 6. Create a pivot_table: average Fare, index=Pclass, columns=Embarked
#    Visualize with sns.heatmap(annot=True, fmt='.1f')

# 7. BONUS: Build a 2x2 dashboard combining 4 different pandas+chart combos:
#    - Top left: groupby.plot() bar chart
#    - Top right: pivot_table heatmap  
#    - Bottom left: value_counts pie chart
#    - Bottom right: agg() summary bar chart
#    Add fig.suptitle('Titanic Analysis Dashboard')