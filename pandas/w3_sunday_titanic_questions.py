'''Q1. What was the overall survival rate on the Titanic?

Q2. Did passenger class affect survival?
    (Which class had the highest/lowest survival rate?)

Q3. Did gender affect survival?
    (Did women really survive more than men?)

Q4. Did family size affect survival?
    (Were solo travelers more/less likely to survive?)

Q5. Which combination of class + gender had the
    highest and lowest survival rates?'''
    
'''clean version'''

import pandas as pd
import numpy as np

# =====================================================
# 1. Load data
# =====================================================

df = pd.read_csv(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
)

# =====================================================
# 2. Drop unneeded columns
# =====================================================

df.drop(columns=['PassengerId'], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# =====================================================
# 3. Rename columns for clarity
# =====================================================

df.rename(columns={
    'Pclass': 'Passenger class',
    'SibSp': 'siblings/spouce',
    'Parch': 'parents/children'
}, inplace=True)

# =====================================================
# 4. Clean text columns
# =====================================================

df['Name'] = df['Name'].str.strip()
df['Sex'] = df['Sex'].str.strip()

# =====================================================
# 5. Feature engineering — Extract title
# =====================================================

df['title'] = df['Name'].str.extract(r',\s*([^\.]*)\.')

# Group rare titles together
df['title'] = df['title'].replace(
    ['Dr', 'Rev', 'Col', 'Major', 'Capt',
     'Jonkheer', 'Don', 'Sir', 'Countess', 'Lady'],
    'Rare'
)

df['title'] = df['title'].replace(['Mlle', 'Ms'], 'Miss')
df['title'] = df['title'].replace('Mme', 'Mrs')

# =====================================================
# 6. Handle missing values
# =====================================================

df['Age'] = df['Age'].fillna(df['Age'].mean())

def age_category(age):
    if age >= 30:
        return 'Senior'
    elif age >= 20:
        return 'junior'
    else:
        return 'child'

df['Age group'] = df['Age'].apply(age_category)

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# =====================================================
# 7. Create family size feature
# =====================================================

df['family size'] = (
    df['siblings/spouce'] +
    df['parents/children'] +
    1
)

# =====================================================
# 8. Pivot tables
# =====================================================

resp = pd.pivot_table(
    df,
    values='Age',
    index='Passenger class',
    columns='Sex',
    aggfunc='mean',
    fill_value=0,
)

print(resp)

rese = pd.pivot_table(
    df,
    values='Fare',
    index='Passenger class',
    columns='Embarked',
    aggfunc='mean',
    fill_value=0,
)

print(rese)
# =====================================================
# 9. value counts and cross tab:
# =====================================================
# BONUS: Load Titanic and:
# 10. value_counts() on Pclass, Sex, Embarked columns
print(df['Passenger class'].value_counts())
print(df['Sex'].value_counts())
print(df['Embarked'].value_counts())
# 11. crosstab of Pclass vs Sex (raw counts)
print(pd.crosstab(df['Passenger class'],df['Sex']))
# 12. crosstab of Pclass vs Sex showing survival RATE (values=Survived, aggfunc='mean')
print(pd.crosstab(df['Passenger class'],df['Sex'],
                  values=df['Survived'],
                  aggfunc='mean'))
# =====================================================
# 9. Final check
# =====================================================

# print("\nFinal shape:", df.shape)
# print(df.head(10))
print(df.columns)
# =====================================================
# 10. Save cleaned dataset
# =====================================================
# df.to_csv('titanic_cleaned.csv', index=False)

# =====================================================
# Q1: Overall survival rate
# =====================================================
survival_rate=df['Survived'].mean()*100
print(f"overall survival rate:{survival_rate:.1f}%")
# ... the output is 38.4 %,2 out of 3 are dead...

# =====================================================
# Q2. Did passenger class affect survival?
#     (Which class had the highest/lowest survival rate?)
# =====================================================
relation_2=pd.pivot_table(df,
                          values='Survived',
                          index='Passenger class',
                          aggfunc='mean',
                          margins=True
                          )*100
print("survival affected by p class:\n ",relation_2)

# =====================================================
# Q3. Did gender affect survival?
#     (Did women really survive more than men?)
# =====================================================
relation_3=pd.pivot_table(df,
                          values='Survived',
                          index='Sex',
                          aggfunc='mean',
                          margins=True
                          )*100
print("survival affected by sex:\n ",relation_3)

# =====================================================
# Q4. Did family size affect survival?
    # (Were solo travelers more/less likely to survive?)
# =====================================================

# print(df.groupby('Survived')['family size'].mean()*100)
relation_4=pd.pivot_table(df,
                          values='Survived',
                          index='family size',
                          aggfunc='mean',
                          margins=True
                          )*100
print("survival affected by fsize:\n ",relation_4)

'''Q5. Which combination of class + gender had the
    highest and lowest survival rates?'''
print(pd.pivot_table(df,
    values  = 'Survived',
    index   = 'Passenger class',
    columns = 'Sex',
    aggfunc = 'mean'
) * 100)
                  