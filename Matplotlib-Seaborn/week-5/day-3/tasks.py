import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# =====================================================
# DATA
# =====================================================

months    = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales     = [1200, 1500, 1800, 1400, 2000, 2200]
subjects  = ['Math', 'English', 'Science', 'History']
scores    = [85, 72, 90, 68]
age       = [22, 25, 28, 30, 35, 40, 45, 50]
salary    = [30000, 35000, 40000, 45000, 55000, 65000, 70000, 75000]
ages_data = np.random.randint(18, 80, 300)

# =====================================================
# TASK 1 — METHOD 1: plt.subplot() — 1 row, 2 cols
# Left: line chart | Right: bar chart
# =====================================================

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.title('Monthly Sales ($)', fontsize=16, fontweight='bold', color='#000000')
plt.plot(months, sales, color="#6E0808", marker='o', markersize=5)
plt.xlabel('Months')
plt.ylabel('Sales $')
plt.ylim(0, 3000)
plt.annotate('Peak of Month',
             fontsize=12, fontweight='bold',
             xy=('Jun', 2200),
             xytext=('Mar', 2500),
             arrowprops=dict(arrowstyle='->', color='#000000'))
plt.grid(True, alpha=0.5)

plt.subplot(1, 2, 2)
plt.title('Subject Scores', fontsize=16, fontweight='bold', color='#000000')
plt.bar(subjects, scores, color="#224C8A")
plt.xlabel('Subjects')
plt.ylabel('Score')
plt.ylim(0, 100)

plt.tight_layout()
plt.show()

# =====================================================
# TASK 2 — METHOD 1: plt.subplot() — 2 rows, 1 col
# Top: scatter plot | Bottom: histogram
# =====================================================

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.title('Age vs Salary', fontsize=16, fontweight='bold', color='#000000')
plt.scatter(age, salary, color="#6E0808", marker='o')
plt.xlabel('Age')
plt.ylabel('Salary $')
plt.xlim(0, 60)
plt.ylim(0, 80000)
plt.annotate('Peak Salary',
             fontsize=12, fontweight='bold',
             xy=(50, 75000),
             xytext=(30, 45000),
             arrowprops=dict(arrowstyle='->', color='#000000'))
plt.grid(True, alpha=0.5)

plt.subplot(2, 1, 2)
plt.title('Age Distribution', fontsize=16, fontweight='bold', color='#000000')
plt.hist(ages_data, bins=15, color="#FB1010")
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(True, alpha=0.5)

plt.tight_layout()
plt.show()

# =====================================================
# TASK 3 — METHOD 2: plt.subplots() — 1 row, 2 cols
# axes[0]: line chart | axes[1]: bar chart
# =====================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].set_title('Monthly Sales', fontsize=16, fontweight='bold', color='#000000')
axes[0].plot(months, sales, color="#000000", marker="o", markersize=5)
axes[0].set_xlabel('Months')
axes[0].set_ylabel('Sales $')
axes[0].set_ylim(0, 2500)
axes[0].grid(True, alpha=0.5)

axes[1].set_title('Subject Scores', fontsize=16, fontweight='bold', color='#000000')
axes[1].bar(subjects, scores, color="#224C8A")
axes[1].set_xlabel('Subjects')
axes[1].set_ylabel('Score')
axes[1].set_ylim(0, 100)

plt.tight_layout()
plt.show()

# =====================================================
# TASK 4 — METHOD 2: plt.subplots() — 2x2 Dashboard
# Top left: line | Top right: bar
# Bottom left: scatter | Bottom right: histogram
# =====================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# Top left — line chart
axes[0, 0].set_title('Monthly Sales ($)', fontsize=14, fontweight='bold')
axes[0, 0].plot(months, sales, color="#6E0808", marker='o', markersize=5)
axes[0, 0].set_xlabel('Months')
axes[0, 0].set_ylabel('Sales $')
axes[0, 0].set_ylim(0, 3000)
axes[0, 0].annotate('Peak!',
                    xy=('Jun', 2200),
                    xytext=('Mar', 2500),
                    arrowprops=dict(arrowstyle='->', color='#000000'))
axes[0, 0].grid(True, alpha=0.5)

# Top right — bar chart
axes[0, 1].set_title('Subject Scores', fontsize=14, fontweight='bold')
axes[0, 1].bar(subjects, scores, color="#224C8A")
axes[0, 1].set_xlabel('Subjects')
axes[0, 1].set_ylabel('Score')
axes[0, 1].set_ylim(0, 100)

# Bottom left — scatter plot
axes[1, 0].set_title('Age vs Salary', fontsize=14, fontweight='bold')
axes[1, 0].scatter(age, salary, color="#6E0808", marker='o')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Salary $')
axes[1, 0].set_xlim(0, 60)
axes[1, 0].set_ylim(0, 80000)
axes[1, 0].grid(True, alpha=0.5)

# Bottom right — histogram
axes[1, 1].set_title('Age Distribution', fontsize=14, fontweight='bold')
axes[1, 1].hist(ages_data, bins=15, color="#FB1010")
axes[1, 1].set_xlabel('Age')
axes[1, 1].set_ylabel('Count')
axes[1, 1].grid(True, alpha=0.5)

fig.suptitle('My Dashboard', fontsize=20, fontweight='bold')
plt.tight_layout()
plt.show()

# =====================================================
# TASK 5 — sharex=True
# 2 rows, 1 col — top: line chart, bottom: bar chart
# Both share the same months x axis
# =====================================================

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

axes[0].set_title('Monthly Sales (Line)', fontsize=16, fontweight='bold')
axes[0].plot(months, sales, color="#000000", marker="o", markersize=5)
axes[0].set_ylabel('Sales $')
axes[0].set_ylim(0, 2500)
axes[0].grid(True, alpha=0.5)

axes[1].set_title('Monthly Sales (Bar)', fontsize=16, fontweight='bold')
axes[1].bar(months, sales, color="#224C8A")
axes[1].set_xlabel('Months')
axes[1].set_ylabel('Sales $')
axes[1].set_ylim(0, 2500)

plt.tight_layout()
plt.show()

# =====================================================
# TASK 6 — BONUS: Titanic 2x2 Dashboard
# =====================================================

titanic = pd.read_csv(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
)
titanic['Age'].fillna(titanic['Age'].median(), inplace=True)
titanic.rename(columns={'Pclass': 'Passenger class'}, inplace=True)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Top left — survival count
survival_counts = titanic['Survived'].value_counts()
axes[0, 0].bar(['Did not Survive', 'Survived'],
               survival_counts.values,
               color=['#E74C3C', '#2ECC71'])
axes[0, 0].set_title('Survival Count', fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel('Count')
axes[0, 0].grid(True, alpha=0.5)

# Top right — survival rate by class
survival_rate = titanic.groupby('Passenger class')['Survived'].mean() * 100
axes[0, 1].bar(['1st', '2nd', '3rd'],
               survival_rate.values,
               color='#3498DB')
axes[0, 1].set_title('Survival Rate by Class', fontsize=14, fontweight='bold')
axes[0, 1].set_ylabel('Survival Rate (%)')
axes[0, 1].set_ylim(0, 100)
axes[0, 1].grid(True, alpha=0.5)

# Bottom left — age distribution
axes[1, 0].hist(titanic['Age'], bins=20, color='#9B59B6')
axes[1, 0].set_title('Age Distribution', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Age')
axes[1, 0].set_ylabel('Count')
axes[1, 0].grid(True, alpha=0.5)

# Bottom right — fare distribution
axes[1, 1].hist(titanic['Fare'], bins=20, color='#F39C12')
axes[1, 1].set_title('Fare Distribution', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Fare ($)')
axes[1, 1].set_ylabel('Count')
axes[1, 1].grid(True, alpha=0.5)

fig.suptitle('Titanic Dashboard', fontsize=20, fontweight='bold')
plt.tight_layout()
plt.show()