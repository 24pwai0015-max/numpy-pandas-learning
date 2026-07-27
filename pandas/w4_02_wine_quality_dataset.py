import pandas as pd
import numpy as np

# =====================================================
# 1. Load Dataset
# =====================================================

df = pd.read_csv(
    "https://raw.githubusercontent.com/dsrscientist/dataset1/master/winequality-red.csv"
)

# =====================================================
# 2. Dataset Analysis
# =====================================================

print("Columns List:\n", df.columns)

print("Shape:\n", df.shape)
print("Missing Values:\n", df.isnull().sum())
print("Data Types:\n", df.dtypes)
print("Dataset Summary:\n", df.describe())

# =====================================================
# 3. Column Description
# =====================================================

"""
fixed acidity        → Affects taste and stability
volatile acidity     → Too high = vinegar taste
citric acid          → Adds freshness
residual sugar       → Sweetness level
chlorides            → Salt content
free sulfur dioxide  → Preservative
total sulfur dioxide → Total preservative
density              → Related to sugar/alcohol
pH                   → Acidity level
sulphates            → Another preservative
alcohol              → Alcohol content
quality              → TARGET (Wine quality)
"""

# =====================================================
# 4. Feature Engineering
# =====================================================

# -----------------------------------------------------
# Total Acidity
# -----------------------------------------------------

df['total acidity'] = (
    df['fixed acidity']
    + df['volatile acidity']
    + df['citric acid']
)

print(df['total acidity'].head(10))

# -----------------------------------------------------
# Sweetness Category
# -----------------------------------------------------

print(df['residual sugar'].agg({'max', 'min', 'mean'}))

def sweetness_level(level):
    if 0 < level < 2:
        return 'off dry'
    elif 2 < level < 8:
        return 'dry'
    else:
        return 'sweet'

df['sweetness'] = df['residual sugar'].apply(sweetness_level)

print(df['sweetness'].head(20))

# -----------------------------------------------------
# Salt Category
# -----------------------------------------------------

print(df['chlorides'].head(20))
print(df['chlorides'].agg({'max', 'min', 'mean'}))

def salt_level(chloride):
    if chloride <= 0.05:
        return 'Low Salt'
    elif chloride <= 0.10:
        return 'Medium Salt'
    else:
        return 'High Salt'

df['salt_category'] = df['chlorides'].apply(salt_level)

print(df['salt_category'].value_counts())

print(pd.pivot_table(
    df,
    values='quality',
    index='salt_category',
    aggfunc=['mean', 'count', 'min', 'max']
))

# -----------------------------------------------------
# Fixed Acidity Category
# -----------------------------------------------------

print(df['fixed acidity'].agg({'max', 'min', 'mean'}))

def acidity_level(level):
    if level >= 9:
        return 'high'
    elif level >= 4:
        return 'medium'
    else:
        return 'low'

df['acidity level'] = df['fixed acidity'].apply(acidity_level)

print(df['acidity level'].value_counts())

quality_affect = pd.pivot_table(
    df,
    values='fixed acidity',
    index='quality',
    columns='acidity level',
    aggfunc='mean',
    fill_value=0
)

print("Quality affected by fixed acidity:\n")
print(quality_affect)

# -----------------------------------------------------
# Volatile Acidity Category
# -----------------------------------------------------

print("+" * 60)

print(df['volatile acidity'].head(21))
print(df['volatile acidity'].agg({'max', 'min', 'mean'}))

def vinger_taste(level):
    if level < 0.4:
        return 'low vinger'
    elif level < 0.7:
        return 'medium vineger'
    else:
        return 'high vineger'

df['vineger taste'] = df['volatile acidity'].apply(vinger_taste)

print("Updated Columns:\n", df.columns)
print(df['vineger taste'].value_counts())

quality_effect1 = pd.pivot_table(
    df,
    values='volatile acidity',
    index='quality',
    columns='vineger taste',
    aggfunc='mean',
    fill_value=0
)

print(quality_effect1)