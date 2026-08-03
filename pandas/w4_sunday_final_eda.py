# =====================================================
# MONTH 1 FINAL PROJECT — Titanic EDA
# Arsalan | Week 4 Sunday
# =====================================================

import pandas as pd
import numpy as np

# =====================================================
# SECTION 1: Load & Inspect
# =====================================================
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
# print("initial columns list: \n",df.columns)
print("initial dataset shape: \n",df.shape)
print("initial data type list: \n",df.dtypes)
print("missing values: \n",df.isnull().sum())
print("dataset all info at initial stage: \n",df.describe())
# =====================================================
# SECTION 2: Data Cleaning
# =====================================================
print("dropped column 1: \n",df.drop(columns=['PassengerId'],inplace=True))
print("updated dataset after dropping 1 column: \n",df)
print("after dropping passendgerID:> columns list: \n",df.columns)
print()
# =====================================================
# SECTION 3: Feature Engineering
# =====================================================
# - title extraction
# - age_category
# - family_size
# - is_alone
# - fare_category

# =====================================================
# SECTION 4: Business Questions
# =====================================================
# Q1 through Q8

# =====================================================
# SECTION 5: Key Findings Summary
# =====================================================
# Comment block summarizing what you discovered

# =====================================================
# SECTION 6: Save
# =====================================================