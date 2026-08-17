import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months   = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales    = [1200, 1500, 1800, 1400, 2000, 2200]
subjects = ['Math', 'English', 'Science', 'History']
scores   = [85, 72, 90, 68]

# 1. Line chart with:
#    - custom color, linewidth=2.5
#    - marker='o', markersize=8
#    - title, xlabel, ylabel with fontsize
#    - grid with linestyle='--', alpha=0.6
#    - figsize=(10,6)
plt.figure(figsize=(10,6))
plt.title('Monthly sales',fontweight=16,fontstyle='italic',color="#140584")
plt.plot(months,sales, linewidth=2.5, marker='o',markersize=8,color="#2D0680")
plt.xlabel('months')
plt.ylabel('sales $')
plt.ylim(0,2500)
plt.grid(True,alpha=0.6,linestyle='--')
# plt.show()

# 2. Bar chart with:
#    - different color for each bar (use hex codes)
#    - title, xlabel, ylabel
#    - ylim(0, 100)
#    - tight_layout()
colors=["#0DBB50","#942B2B","#E8DDDD",'#000000',"#2047E1","#BA199C"]
plt.figure(figsize=(10,6))
plt.title('result analysis',fontweight=20,fontstyle='oblique',color="#140584")
plt.bar(subjects,scores, linewidth=2.5,color=colors)
plt.xlabel('subject')
plt.ylabel('score')
plt.ylim(0,100)
plt.tight_layout()
# plt.show()


# 3. Two lines on same chart:
male_scores   = [85, 72, 90, 68]
female_scores = [78, 88, 85, 75]
#    - different colors for each line
#    - labels + legend
#    - grid, title, xlabel, ylabel
plt.figure(figsize=(10,6))
plt.title('result analysis(male and female)',fontweight=20,fontstyle='oblique',color="#140584")
plt.plot(subjects,male_scores,label='Male',color="#D40EBA")
# plt.plot(subjects,scores)
plt.plot(subjects,female_scores,label='female',color="#14BADB")
plt.xlabel('subject')
plt.ylabel('score')
plt.grid(True,alpha=0.6,linestyle='--')
# plt.legend()
# plt.show()
# 4. Scatter plot with:
age    = [22, 25, 28, 30, 35, 40, 45, 50]
salary = [30000, 35000, 40000, 45000, 55000, 65000, 70000, 75000]
plt.figure(figsize=(10,6))
plt.title('salary vs age',fontweight=16,fontstyle='italic',color="#140584")
plt.scatter(salary,age, marker='^',color="#A60707")
plt.xlabel('salary')
plt.ylabel('age')
plt.xlim(0,80000)
plt.ylim(0,60)
plt.grid(True,alpha=0.6,linestyle='--')
# plt.show()
#    - color='red', marker='^', markersize=10
#    - title, xlabel, ylabel
#    - grid

# 5. Annotate your line chart from Task 1:
#    - Point to the highest sales month
#    - Add an arrow with text 'Peak!'
months   = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales    = [1200, 1500, 1800, 1400, 2000, 2200]
subjects = ['Math', 'English', 'Science', 'History']
scores   = [85, 72, 90, 68]
plt.figure(figsize=(10,6))
plt.title('Monthly sales',fontweight=16,fontstyle='italic',color="#140584")
plt.plot(months,sales, linewidth=2.5, marker='o',markersize=8,color="#2D0680")
plt.xlabel('months')
plt.ylabel('sales $')
plt.ylim(0,2500)
plt.grid(True,alpha=0.6,linestyle='--')
plt.annotate('peak!',
             xy=('Jun',2200),
             xytext=('May',1000),
             arrowprops=dict(arrowstyle='fancy',color='#000000'),
             fontweight=10,
             fontstyle='oblique')

# plt.show()
# 6. BONUS: Load Titanic cleaned CSV
#    - Bar chart of survival rate by Passenger class
#    - Use groupby().mean() to get rates
#    - Custom colors, title, labels, grid

'''you can see titanic.eda.py'''