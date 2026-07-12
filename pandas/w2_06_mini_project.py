# '''
# 1. Load data
# 2. Inspect (shape, dtypes, missing values)
# 3. Clean column names
# 4. Handle missing values
# 5. Fix data types
# 6. Clean text columns
# 7. Create useful new columns
# 8. Drop what you don't need
# 9. Verify final result
# 10. Save cleaned CSV + push to GitHub'''
# import pandas as pd
# import numpy as np

# df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# # Always start by looking
# print(df.shape)

# # print("columns list:\n",df.columns)
# # print(df.head())
# # print(df.dtypes)
# # print(df.isnull().sum())
# df.drop(columns=['PassengerId'],inplace=True)
# # print("columns list:\n",df.columns)
# df.rename(columns={'Pclass':'Passenger class'}, inplace=True)
# # print("columns list:\n",df.columns)


# df.rename(columns={'SibSp':'siblings/spouce'}, inplace=True)
# # print("columns list:\n",df.columns)

# df.rename(columns={'Parch':'parents/children'}, inplace=True)
# # print("columns list:\n",df.columns)
# # print(df['Cabin'].head(10))
# df.drop(columns=['Cabin'],inplace=True)
# # print("dropped succesfully,the new df columns are:\n")
# # print(df.columns)
# # print(df['Passenger class'].head(10))
# # print(df['Passenger class'].isnull().sum())
# df['Name']=df['Name'].str.strip()

# # print(df['Name'].head(10))

# # Extract title
# df['title'] = df['Name'].str.extract(r',\s*([^\.]*)\.')

# # Group rare titles
# df['title'] = df['title'].replace(
#     ['Dr', 'Rev', 'Col', 'Major', 'Capt', 'Jonkheer', 'Don', 'Sir', 'Countess', 'Lady'],
#     'Rare'
# )
# df['title'] = df['title'].replace(['Mlle', 'Ms'], 'Miss')
# df['title'] = df['title'].replace('Mme', 'Mrs')

# # print(df['title'].value_counts())
# # print(df['title'].iloc[19:51])

# # print(df['title'].isnull().sum())
# print(df.columns)

# # print(df['Sex'].isnull().sum())
# df['Sex']=df['Sex'].str.strip()
# # print(df['Sex'].head(20))

# # print(df['Age'].isnull().sum())

# # print(df['Age'].iloc[0:100])
# df['Age']=df['Age'].fillna(df['Age'].mean())
# # print(df['Age'].isnull().sum())  
# # print(df['parents/children'].isnull().sum())
# # print(df['Ticket'].isnull().sum())
# # print(df['Fare'].isnull().sum())

# # print(df.isnull().sum())

# # print(df)
# # print(df['Embarked'].iloc[1:10])
# # print(df['Embarked'].value_counts())

# '''Quick Rule for When to Use Which
# MethodUse Whenffill / bfillData has real sequential/time order (stock prices, sensor logs)
# mode()Categorical data with no order (Embarked, Sex, etc.)
# mean() / median()Numeric data (Age, Fare)'''

# '''Think of .mode() as always returning a list of the most common value(s),
# even if there's only one answer. [0] is just "give me the first item from that list."'''

# df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])

# print(df.isnull().sum())

# df['family size']=df['siblings/spouce']+df['parents/children']+1
# print(df.head(10))

'''clean version'''
import pandas as pd
import numpy as np

# 1. Load data
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# print("Shape:", df.shape)

# 2. Drop unneeded columns
df.drop(columns=['PassengerId'], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# 3. Rename columns for clarity
df.rename(columns={
    'Pclass': 'Passenger class',
    'SibSp': 'siblings/spouce',
    'Parch': 'parents/children'
}, inplace=True)

# 4. Clean text columns
df['Name'] = df['Name'].str.strip()
df['Sex'] = df['Sex'].str.strip()

# 5. Feature engineering — extract title from Name
df['title'] = df['Name'].str.extract(r',\s*([^\.]*)\.')

# Group rare titles together
df['title'] = df['title'].replace(
    ['Dr', 'Rev', 'Col', 'Major', 'Capt', 'Jonkheer', 'Don', 'Sir', 'Countess', 'Lady'],
    'Rare'
)
df['title'] = df['title'].replace(['Mlle', 'Ms'], 'Miss')
df['title'] = df['title'].replace('Mme', 'Mrs')

# 6. Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
def age_category(age):
    if age>=30:
        return 'Senior'
    elif age>=20:
        return 'junior'
    else:
        return 'child'
df['Age group']=df['Age'].apply(age_category)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# 7. Verify no missing values remain
# print("\nMissing values:\n", df.isnull().sum())

# 8. Create family size feature
df['family size'] = df['siblings/spouce'] + df['parents/children'] + 1
# survival rate by passenger class
df['survival Pclass']=df.groupby('Passenger class')['Survived'].transform('mean')
df['survival age']=df.groupby('Age group')['Survived'].transform('mean')
df['survival Sex']=df.groupby('Sex')['Survived'].transform('mean')
print("passenger class recap")
print(df.groupby('Passenger class').agg(
       avg_age    = ('Age', 'mean'),
       max_fare   = ('Fare', 'max'),
       survival   = ('Survived', 'mean'),
       count      = ('Survived', 'count')
   ))
print(df)
# 9. Final check
print("\nFinal shape:", df.shape)
print(df.head(10))
print(df.columns)
# 10. Save cleaned dataset
# df.to_csv('titanic_cleaned.csv', index=False)


