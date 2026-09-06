import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# ------------------------------------------------------------------------------
# 0. DATA LOADING & PREPARATION
# ------------------------------------------------------------------------------
try:
    titanic = pd.read_csv(
        'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
    )
except Exception:
    local_csv = Path(__file__).resolve().parents[3] / 'titanic_cleaned.csv'
    if local_csv.exists():
        titanic = pd.read_csv(local_csv)
    else:
        titanic = pd.read_csv('titanic_cleaned.csv')

# Continuous numerical imputation using median
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
titanic['Fare'] = titanic['Fare'].fillna(titanic['Fare'].median())

# ==============================================================================
# DECONSTRUCTING: titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])
# ==============================================================================
# 1. titanic['Embarked'] (Target Series Selection):
#    Isolates the single categorical column as a Pandas Series.
# 2. .mode() (Categorical Central Tendency):
#    Calculates most frequent value ('S'). Cannot use mean/median on text.
# 3. [0] (Extracting Scalar String):
#    Pandas .mode() returns a Series (to handle ties). [0] extracts the scalar 'S'.
# 4. .fillna(...) (Imputation Engine):
#    Replaces missing NaN values with 'S'.
# 5. titanic['Embarked'] = ... (Reassignment):
#    Safely overwrites column with imputed Series. Never mix with inplace=True.
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])

sns.set_style('whitegrid')

print("Age null count:", titanic['Age'].isnull().sum())
print("Fare null count:", titanic['Fare'].isnull().sum())
print("Embarked null count:", titanic['Embarked'].isnull().sum())
print("-" * 50)

# ==============================================================================
# TASK 1: Groupby + Pandas .plot(kind='bar')
# ==============================================================================
# 1. Use groupby to find average Fare per Pclass
#    Chart it using .plot(kind='bar')
fare_per_class = titanic.groupby('Pclass')['Fare'].mean()
print("1. Average Fare per Pclass:\n", fare_per_class)

plt.figure(figsize=(8, 5))
fare_per_class.plot(kind='bar', color="#C31616", edgecolor='black')
plt.title("Average Fare by Passenger Class", fontsize=15, fontweight='bold', color="#8A0404")
plt.xlabel("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", fontsize=11)
plt.ylabel("Average Fare ($)", fontsize=11)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==============================================================================
# TASK 2: Groupby + Matplotlib plt.bar() with .index & .values
# ==============================================================================
# 2. Use groupby to find average Age per Embarked port
#    Chart it using plt.bar() with .index and .values
avg_age_port = titanic.groupby('Embarked')['Age'].mean()
print("\n2. Average Age per Embarked Port:\n", avg_age_port)

plt.figure(figsize=(8, 5))
port_names = {'C': 'Cherbourg (C)', 'Q': 'Queenstown (Q)', 'S': 'Southampton (S)'}
labels = [port_names.get(p, p) for p in avg_age_port.index]
plt.bar(labels, avg_age_port.values, color="#1f77b4", edgecolor='black', width=0.55)
plt.title("Average Passenger Age per Embarked Port", fontsize=15, fontweight='bold')
plt.xlabel("Embarked Port", fontsize=11)
plt.ylabel("Average Age (Years)", fontsize=11)
plt.ylim(0, 35)
plt.tight_layout()
plt.show()

# ==============================================================================
# TASK 3: Multi-Index Groupby + .unstack() + Seaborn Heatmap
# ==============================================================================
# 3. Use groupby(['Pclass','Sex']) to find survival rate
#    Convert to a pivot table via unstack(), then chart with sns.heatmap()
survival_pclass_sex = titanic.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack()
print("\n3. Survival Rate Pivot (Pclass x Sex):\n", survival_pclass_sex)

plt.figure(figsize=(7, 5))
sns.heatmap(data=survival_pclass_sex, annot=True, fmt='.2f', cmap='coolwarm', vmin=0, vmax=1)
plt.title("Survival Rate by Class and Sex", fontsize=15, fontweight='bold')
plt.xlabel("Gender", fontsize=11)
plt.ylabel("Passenger Class", fontsize=11)
plt.tight_layout()
plt.show()

# ==============================================================================
# TASK 4: value_counts() + Matplotlib Pie Chart
# ==============================================================================
# 4. Use value_counts() on 'Embarked'
#    Chart it as a pie chart with percentages
embarked_counts = titanic['Embarked'].value_counts()
print("\n4. Embarked Value Counts:\n", embarked_counts)

plt.figure(figsize=(7, 7))
colors = ["#2ca02c", "#d62728", "#1f77b4"]
explode = (0.05, 0, 0)
port_full_labels = [f"{port_names.get(k, k)}: {v}" for k, v in embarked_counts.items()]

plt.pie(
    embarked_counts,
    labels=port_full_labels,
    colors=colors,
    autopct='%1.1f%%',
    startangle=140,
    explode=explode,
    shadow=True
)
plt.title("Passenger Boarding Distribution by Port", fontsize=15, fontweight='bold')
plt.tight_layout()
plt.show()

# ==============================================================================
# TASK 5: Multi-Metric Aggregation with .agg() + Bar Chart
# ==============================================================================
# 5. Use agg() to get survival_rate, avg_age, avg_fare, count per Pclass
#    Print the full summary table
#    Then chart just the survival_rate column as a bar chart
class_summary = titanic.groupby('Pclass').agg(
    survival_rate=('Survived', 'mean'),
    avg_age=('Age', 'mean'),
    avg_fare=('Fare', 'mean'),
    passenger_count=('Survived', 'count')
)
print("\n5. Class Summary via .agg():\n", class_summary)

plt.figure(figsize=(8, 5))
class_summary['survival_rate'].plot(kind='bar', color='#2ca02c', edgecolor='black')
plt.title("Survival Rate by Class (Extracted from .agg() Summary)", fontsize=14, fontweight='bold')
plt.xlabel("Passenger Class", fontsize=11)
plt.ylabel("Survival Rate (0 - 1.0)", fontsize=11)
plt.ylim(0, 1)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==============================================================================
# TASK 6: pd.pivot_table() Matrix + Seaborn Heatmap
# ==============================================================================
# 6. Create a pivot_table: average Fare, index=Pclass, columns=Embarked
#    Visualize with sns.heatmap(annot=True, fmt='.1f')
fare_pivot = titanic.pivot_table(
    values='Fare',
    index='Pclass',
    columns='Embarked',
    aggfunc='mean'
)
print("\n6. Average Fare Pivot Table (Pclass x Embarked):\n", fare_pivot)

plt.figure(figsize=(8, 6))
sns.heatmap(fare_pivot, annot=True, fmt='.1f', cmap='YlGnBu')
plt.title("Average Fare Matrix: Class vs Embarked Port ($)", fontsize=14, fontweight='bold')
plt.xlabel("Embarked Port", fontsize=11)
plt.ylabel("Passenger Class", fontsize=11)
plt.tight_layout()
plt.show()

# ==============================================================================
# TASK 7 (BONUS): Executive 2x2 Analytical Dashboard
# ==============================================================================
# 7. Build a 2x2 dashboard combining 4 different pandas+chart combos:
#    - Top left: groupby.plot() bar chart
#    - Top right: pivot_table heatmap
#    - Bottom left: value_counts pie chart
#    - Bottom right: agg() summary bar chart
#    Add fig.suptitle('Titanic Analysis Dashboard')
fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# Top-Left: Groupby Average Fare
fare_per_class.plot(kind='bar', ax=axes[0, 0], color='#d9534f', edgecolor='black')
axes[0, 0].set_title('Avg Fare by Class (groupby.plot)', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Pclass')
axes[0, 0].set_ylabel('Fare ($)')
axes[0, 0].tick_params(axis='x', rotation=0)

# Top-Right: Pivot Table Heatmap
sns.heatmap(fare_pivot, ax=axes[0, 1], annot=True, fmt='.1f', cmap='YlGnBu')
axes[0, 1].set_title('Avg Fare Matrix (pivot_table Heatmap)', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Embarked Port')
axes[0, 1].set_ylabel('Pclass')

# Bottom-Left: Port Distribution Pie
axes[1, 0].pie(
    embarked_counts,
    labels=embarked_counts.index,
    autopct='%1.1f%%',
    colors=['#5cb85c', '#f0ad4e', '#5bc0de'],
    startangle=140
)
axes[1, 0].set_title('Embarked Port Share (value_counts.pie)', fontsize=12, fontweight='bold')

# Bottom-Right: Survival Rate from .agg()
class_summary['survival_rate'].plot(kind='bar', ax=axes[1, 1], color='#0275d8', edgecolor='black')
axes[1, 1].set_title('Survival Rate by Class (agg.plot)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Pclass')
axes[1, 1].set_ylabel('Survival Rate')
axes[1, 1].set_ylim(0, 1)
axes[1, 1].tick_params(axis='x', rotation=0)

fig.suptitle('Titanic Analysis Dashboard — Integrated Pandas & Visualizations', fontsize=17, fontweight='bold')
plt.tight_layout()
plt.show()