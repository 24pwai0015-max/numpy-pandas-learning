# =====================================================
# MONTH 1 FINAL PROJECT — Titanic EDA
# Arsalan | Week 4 Sunday
# =====================================================

import pandas as pd
import numpy as np

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
    "Pclass": "Passenger Class",
    "SibSp": "Siblings/Spouse",
    "Parch": "Parents/Children"
}, inplace=True)

df["Name"] = df["Name"].str.strip()
df["Sex"] = df["Sex"].str.strip()

df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

df.drop_duplicates(inplace=True)

print("\nRemaining Missing Values")
print(df.isnull().sum())

# =====================================================
# SECTION 3: Feature Engineering
# =====================================================

# -------- Title --------

df["Title"] = df["Name"].str.extract(r",\s*([^.]*)\.")

df["Title"] = df["Title"].replace(
    ["Capt", "Col", "Don", "Dr", "Jonkheer",
     "Lady", "Major", "Rev", "Sir", "Countess"],
    "Rare"
)

df["Title"] = df["Title"].replace(["Mlle", "Ms"], "Miss")
df["Title"] = df["Title"].replace("Mme", "Mrs")

# -------- Age Category --------

df["Age Category"] = pd.cut(
    df["Age"],
    bins=[0, 12, 19, 59, 100],
    labels=["Child", "Teen", "Adult", "Senior"],
    include_lowest=True
)

# -------- Family Size --------

df["Family Size"] = (
    df["Siblings/Spouse"]
    + df["Parents/Children"]
    + 1
)

# -------- Is Alone --------

df["Is Alone"] = np.where(df["Family Size"] == 1, "Yes", "No")

# -------- Family Group --------

def family_group(size):
    if size == 1:
        return "Solo"
    elif size <= 4:
        return "Small Family"
    else:
        return "Large Family"

df["Family Group"] = df["Family Size"].apply(family_group)

# -------- Fare Category --------

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

# -----------------------------------------------------

print("\n" + "=" * 60)
print("Q2. Survival Rate by Passenger Class")
print("=" * 60)

print(
    df.groupby("Passenger Class")["Survived"]
      .mean()
      .sort_values(ascending=False)
)

# -----------------------------------------------------

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

# -----------------------------------------------------

print("\n" + "=" * 60)
print("Q4. Age Category vs Survival")
print("=" * 60)

print(
    df.groupby("Age Category")["Survived"]
      .mean()
      .sort_values(ascending=False)
)

# -----------------------------------------------------

print("\n" + "=" * 60)
print("Q5. Family Group vs Survival")
print("=" * 60)

print(
    df.groupby("Family Group")["Survived"]
      .mean()
)

# -----------------------------------------------------

print("\n" + "=" * 60)
print("Q6. Title with Highest Survival")
print("=" * 60)

print(
    df.groupby("Title")["Survived"]
      .mean()
      .sort_values(ascending=False)
)

# -----------------------------------------------------

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

# -----------------------------------------------------

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
# SECTION 5: Key Findings Summary
# =====================================================

"""
Key Findings

1. Female passengers had a much higher survival rate than males.
2. First-class passengers had the highest survival rate.
3. Children generally survived more often than seniors.
4. Small families survived more often than large families.
5. Passengers with higher ticket fares generally had better survival chances.
6. Titles such as Mrs and Miss showed higher survival rates.
7. First-class females had the highest survival probability.
8. Third-class males had the lowest survival probability.
"""

# =====================================================
# SECTION 6: Save
# =====================================================

df.to_csv("titanic_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final Shape:", df.shape)