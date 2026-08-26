import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Robust data loading with fallback if online dataset is unavailable
try:
    titanic = pd.read_csv(
        'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    )
except Exception:
    titanic = pd.read_csv('titanic_cleaned.csv')

# Handle missing values
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Fare'] = titanic['Fare'].fillna(titanic['Fare'].median())

print("Null values in Age:", titanic['Age'].isnull().sum())
print("Null values in Fare:", titanic['Fare'].isnull().sum())

# Set global Seaborn style
sns.set_style('whitegrid')

# ---------------------------------------------------------
# 1. histplot — Age distribution
#    - bins=20
#    - Add title
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.title('Age Distribution of Passengers', fontweight='bold', fontsize=14, color="#A30A0A")
sns.histplot(data=titanic, x='Age', bins=20, color='#2b5c8f', kde=True)
plt.xlabel('Age')
plt.ylabel('Passenger Count')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 2. histplot — Age distribution split by Survived
#    - use hue='Survived'
#    - Add title
#    - Predict first: do survivors skew younger or older?
# Prediction: Younger passengers (children) had higher survival rates
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.title('Age Distribution Split by Survival Status', fontweight='bold', fontsize=14, color="#A30A0A")
sns.histplot(data=titanic, x='Age', bins=20, hue='Survived', multiple='stack', palette='Set1')
plt.xlabel('Age')
plt.ylabel('Passenger Count')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 3. barplot — Survival rate by Pclass
#    - x='Pclass', y='Survived'
#    - Predict first: which class survives most?
# Prediction: 1st class had highest survival rate
# ---------------------------------------------------------
plt.figure(figsize=(7, 5))
plt.title('Survival Rate by Passenger Class (Pclass)', fontweight='bold', fontsize=14, color="#A30A0A")
sns.barplot(data=titanic, x='Pclass', y='Survived', palette='Blues_d')
plt.xlabel('Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)')
plt.ylabel('Survival Rate (Mean)')
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

print("\nMean survival rate per class:")
print(titanic.groupby('Pclass')['Survived'].mean())

# ---------------------------------------------------------
# 4. barplot — Survival rate by Pclass split by Sex
#    - use hue='Sex'
#    - Predict first: does the gender gap hold across all classes?
# Prediction: Yes, females had dramatically higher survival rates in every class
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.title('Survival Rate by Pclass Split by Sex', fontweight='bold', fontsize=14, color="#A30A0A")
sns.barplot(data=titanic, x='Pclass', y='Survived', hue='Sex', palette='Set2')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.ylim(0, 1)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 5. boxplot — Age distribution by Pclass
#    - x='Pclass', y='Age'
#    - Predict first: which class has older passengers?
# Prediction: 1st class has older passengers (higher median age ~37)
# ---------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.title('Age Distribution by Passenger Class', fontweight='bold', fontsize=14, color="#A30A0A")
sns.boxplot(data=titanic, x='Pclass', y='Age', palette='Pastel1')
plt.xlabel('Passenger Class')
plt.ylabel('Age')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 6. boxplot — Fare distribution by Pclass split by Sex
#    - use hue='Sex'
# Note: Fixed y='Fare' (was previously y='Age')
# ---------------------------------------------------------
plt.figure(figsize=(9, 6))
plt.title('Fare Distribution by Pclass Split by Sex', fontweight='bold', fontsize=14, color="#A30A0A")
sns.boxplot(data=titanic, x='Pclass', y='Fare', hue='Sex', palette='Set3', showfliers=False)
plt.xlabel('Passenger Class')
plt.ylabel('Fare ($) [Outliers hidden for clarity]')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 7. heatmap — correlation of all numeric columns
#    - annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1
#    - Which two columns have the strongest correlation with Survived?
# Result: Pclass (-0.34) and Fare (+0.26) have the strongest correlations with Survived
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.title('Correlation Heatmap of Numeric Features', fontweight='bold', fontsize=14, color="#A30A0A")
correlation = titanic.corr(numeric_only=True)
print("\nCorrelation Matrix:\n", correlation)

sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1, square=True)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 8. scatterplot — Age vs Fare
#    - hue='Survived'
#    - Predict first: do survivors cluster in a particular age/fare zone?
# Prediction: Survivors cluster at higher fares (wealthier cabins) and young age (<10)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.title('Age vs Fare by Survival Status', fontweight='bold', fontsize=14, color="#A30A0A")
sns.scatterplot(data=titanic, x='Age', y='Fare', hue='Survived', palette='coolwarm', alpha=0.8)
plt.xlabel('Age')
plt.ylabel('Fare ($)')
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# 9. pairplot — Age, Fare, Survived, Pclass
#    - hue='Survived'
# Note: Figure-level title applied using g.figure.suptitle()
# ---------------------------------------------------------
g = sns.pairplot(
    titanic[['Age', 'Fare', 'Pclass', 'Survived']],
    hue='Survived',
    palette='Set1',
    diag_kind='kde'
)
g.figure.subplots_adjust(top=0.93)
g.figure.suptitle('Pairwise Relationships by Survival Status', fontweight='bold', fontsize=15, color="#A30A0A")
plt.show()

# ---------------------------------------------------------
# 10. BONUS: Which single chart tells the survival story best?
#     Pick one, add a clear title, and explain in a comment why.
# ---------------------------------------------------------
# Chart Choice: Task 4 — Barplot of Survival by Class & Gender.
# Reason: It immediately proves the two most impactful survival factors on Titanic:
# 1. Social Class (1st > 2nd > 3rd class survival rate)
# 2. Gender (females prioritized across all classes)
plt.figure(figsize=(8, 5))
plt.title('The Survival Story: Women and Upper-Class Passengers First', fontweight='bold', fontsize=14, color="#140584")
sns.barplot(data=titanic, x='Pclass', y='Survived', hue='Sex', palette=['#3498db', '#e74c3c'])
plt.xlabel('Passenger Class (1st, 2nd, 3rd)')
plt.ylabel('Survival Probability (0 to 1)')
plt.ylim(0, 1)
plt.tight_layout()
plt.show()