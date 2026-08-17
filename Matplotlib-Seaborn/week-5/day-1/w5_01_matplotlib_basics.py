# '''
# What is Matplotlib?

# pandas taught you to analyze data — find patterns, answer questions, 
# calculate statistics.

# Matplotlib teaches you to show data — turn those numbers into charts
# people can actually understand.'''



# '''
# pandas  → "survival rate for 1st class females is 96.8%"
# matplotlib → [a bar chart showing this visually]
# '''

# '''
# The Core Idea:
# Every matplotlib chart follows the same structure:

# import matplotlib.pyplot as plt

# # 1. Give it data
# plt.plot([1, 2, 3], [4, 5, 6])

# # 2. Show it
# plt.show()

# That's it at the most basic level.
# '''

# import matplotlib.pyplot as plt
# import numpy as np

# # plt.plot([1,2,3,4,5,6],[12.2,34,5,6,7,4])

# # # plt.show()
# # plt.title("marks analyzer")
# # students=['ali','ahmad','sara']
# # marks=[35,45,50]

# # plt.plot(students,marks)

# # plt.show()

# # Bar Chart
# # plt.title("marks analyzer")
# # students=['ali','ahmad','sara']
# # marks=[35,45,50]

# # plt.bar(students,marks)

# # plt.show()

# # horizontal bar chart

# # plt.title("marks analyzer")
# # students=['ali','ahmad','sara']
# # marks=[35,45,50]

# # plt.barh(students,marks)

# # plt.show()

# # scatter plot
# # plt.title("salary analysis")
# # age    = [22, 25, 28, 30, 35, 40]
# # salary = [30000, 35000, 40000, 45000, 55000, 65000]

# # plt.scatter(age,salary)

# # plt.show()


# # histogram


# # ages = np.random.randint(18, 70, 200)

# # plt.hist(ages, bins=10)
# # plt.show()

# # pie chart
# '''
# Matplotlib pie chart is a circular statistical graphic that shows proportions of a whole. 
# Each slice (wedge) represents a category’s share of the total.
# Basic idea

# The full circle = 100%
# Slice size is proportional to the value
# Great for showing composition (market share, budget breakdown, survey results, etc.)'''


# # import matplotlib.pyplot as plt

# # # Data
# # sizes = [35, 25, 20, 15, 5]
# # labels = ['Python', 'JavaScript', 'Java', 'C++', 'Other']
# # colors = ["#2f6b14", "#377cde", "#4546723a", '#F44336', '#000000']
# # # colors=["green","red","blue","yellow","purple"]
# # # colors are designed by hex codes
# # #RRGGBB red,green,blue hash tag represent the hexadecimal

# # # Create pie chart
# # plt.figure(figsize=(8, 6))
# # # 8 wdth
# # # 6 height
# # plt.pie(sizes, 
# #         labels=labels, 
# #         colors=colors,
# #         autopct='%1.1f%%',   # show percentage
# #         startangle=90,       # rotate so first slice starts at top
# #         shadow=True)         # add shadow for 3D effect

# # '''
# # plt.figure is the function that creates a new figure (the overall window/canvas)
# # in Matplotlib.



# # startangle in a Matplotlib pie chart controls the starting angle of the first slice.
# # What it does

# # By default, the first slice starts at 0° (the positive x-axis, pointing to the right).
# # startangle rotates the entire pie so the first slice begins at the angle you specify.
# # Angles are measured counter-clockwise from the positive x-axis.
# # '''


# # plt.title('Programming Language Popularity')
# # plt.axis('equal')            # makes the pie circular
# # plt.show()




# tasks
import matplotlib.pyplot as plt
import numpy as np

# 1. Line chart — plot these monthly sales
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [1200, 1500, 1800, 1400, 2000, 2200]
# Add title, xlabel, ylabel
# plt.figure(figsize=(6,6))
# plt.title("monthly sales")
# xlable=months
# ylables=sales
# plt.plot(xlable,ylables)
# plt.show()

# 2. Bar chart — plot these subject scores
subjects = ['Math', 'English', 'Science', 'History']
scores   = [85, 72, 90, 68]
# colors=[["#5b1111","#517b13","#6f6f0a"]]
# # Add title, xlabel, ylabel
# plt.figure(figsize=(6,6))
# plt.title("subject scores")
# xlable=subjects
# ylables=scores
# plt.bar(xlable,ylables)
# plt.show()

# 3. Horizontal bar chart — same data as task 2
# plt.figure(figsize=(6,6))
# plt.title("subject scores")
# xlable=subjects
# ylables=scores
# plt.barh(xlable,ylables)
# plt.show()
# 4. Scatter plot — age vs salary
age    = [22, 25, 28, 30, 35, 40, 45, 50]
salary = [30000, 35000, 40000, 45000, 55000, 65000, 70000, 75000]
# Add title, xlabel, ylabel
# plt.figure(figsize=(6,6))
# plt.title("age vs sallery")
# xlable=salary
# ylables=age
# plt.scatter(xlable,ylables)
# plt.show()

# 5. Histogram — generate 500 random ages between 18-80
#    use bins=15
ages = np.random.randint(18, 80, 500)
plt.figure(figsize=(10,5))
plt.title("random ages ")
plt.hist(ages,bins=15)
# 6. Pie chart — Titanic passenger class distribution
# labels = ['1st Class', '2nd Class', '3rd Class']
# sizes  = [216, 184, 491]
plt.show()
# use autopct='%1.1f%%'

# plt.figure(figsize=(10,5))
lables=['ecaprio','nelson','haseena']
sizes=[200,300,100]
colors=["#5b1111","#517b13","#6f6f0a"]
plt.figure(figsize=(6,6))
plt.pie(sizes,
        labels=lables,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True
        
        )
plt.title("titanic passeneger classes")
plt.axis('equal')
plt.savefig('pie chat.png')
plt.show()

# 7. Save any one of your charts as a .png file
# plt.savefig('pie chat.png')
# 8. BONUS: Load your Titanic cleaned CSV and plot:
#    - Bar chart of survival counts (Survived: 0 vs 1)
#    - Use value_counts() to get the data first