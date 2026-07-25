import pandas as pd
import numpy as np

# =====================================================
# 1. Load data
# =====================================================
df = pd.read_csv('https://raw.githubusercontent.com/dsrscientist/dataset1/master/winequality-red.csv')

# =====================================================
# 2. dataset analysis
# =====================================================

# print("columns list:\n",df.columns)
# print("shape:\n",df.shape)
# print("missing valuse:\n",df.isnull().sum())
# print("data type analysis:\n",df.dtypes)
# print("all info:\n",df.describe)

# =====================================================
# 2.columns description
# =====================================================
'''
fixed acidity       → affects taste/stability
volatile acidity    → too high = vinegar taste
citric acid         → adds freshness
residual sugar      → sweetness level
chlorides           → salt content
free sulfur dioxide → preservative
total sulfur dioxide→ total preservative
density             → related to sugar/alcohol
pH                  → acidity level
sulphates           → another preservative
alcohol             → alcohol content
quality             → TARGET (what you're predicting)'''

# =====================================================
# 3. feature engineering
# =====================================================

# df['total acidity']=df['fixed acidity']+df['volatile acidity']+df['citric acid']
# print(df["total acidity"].head(10))
# print(df['residual sugar'].agg({'max','min','mean'}))

# def sweatnes_level(level):
#     if level>0 and level<2:
#         return 'off dry'
#     elif level>2 and level<8:
#         return 'dry'
#     else:
#         return 'sweet'
    
# df['sweetness']=df['residual sugar'].apply(sweatnes_level)
# print(df['sweetness'].head(20))

print(df['chlorides'].head(20))
print(df['chlorides'].agg({'max','min','mean'}))
def salt_level(chloride):
    if chloride <= 0.05:
        return 'Low Salt'
    elif chloride <= 0.10:
        return 'Medium Salt'
    else:
        return 'High Salt'
    


df['salt_category'] = df['chlorides'].apply(salt_level)
print("total values per category \n",df['salt_category'].value_counts())

# Does salt level affect quality?
print(pd.pivot_table(df,
    values  = 'quality',
    index   = 'salt_category',
    aggfunc = ['mean', 'count', 'min', 'max'],
    fill_value=0,
    margins=True
))


    
        