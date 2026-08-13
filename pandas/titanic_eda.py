# =====================================================
# MONTH 1 FINAL PROJECT — Titanic EDA
# Arsalan | Week 4 Sunday
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# SECTION 1: Load & Inspect
# =====================================================

df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)

print("=" * 50)
print("Dataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nSummary Statistics")
print(df.describe(include="all"))

# =====================================================
# SECTION 2: Data Cleaning
# =====================================================

df.drop(columns=["PassengerId", "Cabin"], inplace=True)

df.rename(columns={
    "Pclass"  : "Passenger Class",
    "SibSp"   : "Siblings/Spouse",
    "Parch"   : "Parents/Children"
}, inplace=True)

df["Name"]      = df["Name"].str.strip()
df["Sex"]       = df["Sex"].str.strip()

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df.drop_duplicates(inplace=True)

print("\nRemaining Missing Values")
print(df.isnull().sum())

# =====================================================
# SECTION 3: Feature Engineering
# =====================================================

# Title
df["Title"] = df["Name"].str.extract(r",\s*([^.]*)\.")
df["Title"] = df["Title"].str.strip()

df["Title"] = df["Title"].replace(
    ["Capt", "Col", "Don", "Dr", "Jonkheer",
     "Lady", "Major", "Rev", "Sir", "Countess", "the Countess"],
    "Rare"
)

df["Title"] = df["Title"].replace(["Mlle", "Ms"], "Miss")
df["Title"] = df["Title"].replace("Mme", "Mrs")

# Age Category
df["Age Category"] = pd.cut(
    df["Age"],
    bins=[0, 12, 19, 59, 100],
    labels=["Child", "Teen", "Adult", "Senior"],
    include_lowest=True
)

# Family Size
df["Family Size"] = (
    df["Siblings/Spouse"]
    + df["Parents/Children"]
    + 1
)

# Is Alone
df["Is Alone"] = np.where(df["Family Size"] == 1, "Yes", "No")

# Family Group
def family_group(size):
    if size == 1:
        return "Solo"
    elif size <= 4:
        return "Small Family"
    else:
        return "Large Family"

df["Family Group"] = df["Family Size"].apply(family_group)

# Fare Category
df["Fare Category"] = pd.qcut(
    df["Fare"],
    q=4,
    labels=["Low", "Medium", "High", "Very High"]
)

# =====================================================
# SECTION 4: Business Questions
# =====================================================

print("\n" + "=" * 60)
print("Q1. Overall Survival Rate")
print("=" * 60)
print(f"{df['Survived'].mean()*100:.2f}%")

print("\n" + "=" * 60)
print("Q2. Survival Rate by Passenger Class")
print("=" * 60)
print(
    df.groupby("Passenger Class")["Survived"]
      .mean()
      .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("Q3. Gender Effect on Survival")
print("=" * 60)
print("\nCounts")
print(pd.crosstab(df["Sex"], df["Survived"]))
print("\nRates")
print(
    pd.crosstab(
        df["Sex"],
        df["Survived"],
        normalize="index"
    ) * 100
)

print("\n" + "=" * 60)
print("Q4. Age Category vs Survival")
print("=" * 60)
print(
    df.groupby("Age Category", observed=True)["Survived"]
      .mean()
      .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("Q5. Family Group vs Survival")
print("=" * 60)
print(
    df.groupby("Family Group")["Survived"]
      .mean()
)

print("\n" + "=" * 60)
print("Q6. Title with Highest Survival")
print("=" * 60)
print(
    df.groupby("Title")["Survived"]
      .mean()
      .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("Q7. Passenger Class + Gender Survival")
print("=" * 60)
pivot = pd.pivot_table(
    df,
    values="Survived",
    index="Passenger Class",
    columns="Sex",
    aggfunc="mean"
)
print(pivot)

print("\n" + "=" * 60)
print("Q8. Fare Distribution by Passenger Class")
print("=" * 60)
print(
    df.groupby("Passenger Class")["Fare"]
      .agg(
          Mean="mean",
          Min="min",
          Max="max",
          Count="count"
      )
)

# =====================================================
# Extra Analysis
# =====================================================

print("\nPassenger Class Counts")
print(df["Passenger Class"].value_counts())

print("\nGender Counts")
print(df["Sex"].value_counts())

print("\nEmbarked Counts")
print(df["Embarked"].value_counts())

print("\nPassenger Class vs Gender")
print(pd.crosstab(df["Passenger Class"], df["Sex"]))

print("\nPassenger Class vs Gender Survival Rate")
print(
    pd.crosstab(
        df["Passenger Class"],
        df["Sex"],
        values=df["Survived"],
        aggfunc="mean"
    )
)

# =====================================================
# SECTION 5: Key Findings
# =====================================================

print("\n" + "=" * 60)
print("KEY FINDINGS")
print("=" * 60)
print("""
1. Female passengers had much higher survival rate than males
2. First class passengers had the highest survival rate
3. Children generally survived more often than seniors
4. Small families survived more often than large families
5. Higher ticket fares = better survival chances
6. Mrs and Miss titles showed higher survival rates
7. First class females had the highest survival probability
8. Third class males had the lowest survival probability
""")

# =====================================================
# SECTION 6: Data Visualization
# =====================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Titanic EDA — Arsalan', fontsize=16)

# Chart 1 — Survival Count
survived_counts = df['Survived'].value_counts().sort_index()
axes[0, 0].bar(
    ['Did Not Survive', 'Survived'],
    survived_counts.values,
    color=['#e74c3c', '#2ecc71']
)
axes[0, 0].set_title('Survival Count')
axes[0, 0].set_ylabel('Count')
axes[0, 0].grid(axis='y')

# Chart 2 — Survival by Class
survival_by_class = df.groupby('Passenger Class')['Survived'].mean() * 100
axes[0, 1].bar(
    survival_by_class.index.astype(str),
    survival_by_class.values,
    color=['#3498db', '#9b59b6', '#e67e22']
)
axes[0, 1].set_title('Survival Rate by Passenger Class')
axes[0, 1].set_ylabel('Survival Rate (%)')
axes[0, 1].grid(axis='y')

# Chart 3 — Survival by Gender
survival_by_gender = df.groupby('Sex')['Survived'].mean() * 100
axes[0, 2].bar(
    survival_by_gender.index,
    survival_by_gender.values,
    color=['#e74c3c', '#3498db']
)
axes[0, 2].set_title('Survival Rate by Gender')
axes[0, 2].set_ylabel('Survival Rate (%)')
axes[0, 2].grid(axis='y')

# Chart 4 — Age Distribution
axes[1, 0].hist(
    df['Age'],
    bins=30,
    color='#3498db',
    edgecolor='black'
)
axes[1, 0].set_title('Age Distribution')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Count')
axes[1, 0].grid(axis='y')

# Chart 5 — Family Group Survival
survival_by_family = df.groupby('Family Group')['Survived'].mean() * 100
axes[1, 1].bar(
    survival_by_family.index,
    survival_by_family.values,
    color=['#2ecc71', '#e67e22', '#e74c3c']
)
axes[1, 1].set_title('Survival Rate by Family Group')
axes[1, 1].set_ylabel('Survival Rate (%)')
axes[1, 1].grid(axis='y')

# Chart 6 — Fare Distribution
axes[1, 2].hist(
    df['Fare'],
    bins=30,
    color='#9b59b6',
    edgecolor='black'
)
axes[1, 2].set_title('Fare Distribution')
axes[1, 2].set_xlabel('Fare')
axes[1, 2].set_ylabel('Count')
axes[1, 2].grid(axis='y')

plt.tight_layout()
plt.savefig('titanic_eda.png', dpi=150, bbox_inches='tight')
print("\nVisualization saved as titanic_eda.png")

# =====================================================
# SECTION 7: Save
# =====================================================

df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned dataset saved successfully!")
print("Final Shape:", df.shape)
