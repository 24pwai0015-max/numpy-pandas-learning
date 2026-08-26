import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

                                                    
'''
Histogram:
sns.histplot(data, x=)=>>>>>>>>>>>>>>>>>>	Distribution of one variable

themes:

sns.set_style('whitegrid')   # white background + grid ← most popular
sns.set_style('darkgrid')    # dark background + grid
sns.set_style('white')       # clean white, no grid
sns.set_style('dark')        # dark, no grid
sns.set_style('ticks')       # white + tick marks
'''



# step 1

tips=sns.load_dataset('tips')
sns.set_style('ticks')
print("columns list:\n",tips.columns)
# print("initial analysis:\n",tips.head())
# print("initial shape:\n",tips.shape)
# print("time analysis on valuse:\n",tips['time'].value_counts())
print("smoker analysis on valuse:\n",tips['smoker'].value_counts())
print("smoker unique analysis:",tips['smoker'].unique())
# print("smoker analysis:\n",tips['smoker'].iloc[50:101])
# print("data:",tips["time"].head(21))
print("dataset load successfully")

# step 2 choosed histogram

# sns.histplot(data=tips ,x='total_bill')
# plt.show()
# # step 3 add bins

# sns.histplot(data=tips ,x='total_bill' , bins=20)
# plt.show()

# step 4  hue


# sns.histplot(data=tips ,x='total_bill' , bins=20 , hue='time')
# plt.show()

'''
You never wrote plt.legend() — but a legend showed up anyway.
Why This Matters
Remember in matplotlib, you had to manually do:

plt.plot(x, y1, label='Male')
plt.plot(x, y2, label='Female')
plt.legend()   # ← had to call this yourself

In seaborn, hue= does all of that automatically:

hue='time' automatically:
1. Splits data into Lunch group and Dinner group
2. Colors each group differently
3. Creates the legend
4. Labels it correctly

You wrote ONE word. Seaborn did all 4 things.
This Is THE Core Idea of Seaborn
matplotlib: YOU tell it every single detail
seaborn:    YOU tell it WHAT you want split by, IT figures out the rest

hue= is seaborn's superpower — you'll use it constantly:'''


# Step 5 — Try a Different Column



# sns.histplot(data=tips ,x='total_bill' , bins=20 , hue='smoker')
# plt.show()

# step 6 avoid blending

sns.histplot(data=tips ,x='total_bill' , bins=20 , hue='smoker',multiple='stack')
plt.show()

'''# Other options for multiple=
multiple='layer'   # default — overlapping (what you just saw)
multiple='stack'   # stacked on top of each other
multiple='dodge'   # side by side bars
multiple='fill'    # stacked as percentages (100% height)'''


                                                                        #  histogram recap
'''
data=       → which DataFrame
x=          → which column to show distribution of
bins=       → how many buckets
hue=        → split by category (auto colors + legend)
multiple=   → how to handle overlapping hue groups'''
                                                                        # barplot
                                                                        

sns.barplot(data=tips,x='sex',y='total_bill')                                                                       
plt.show()

sns.barplot(data=tips, x='day', y='total_bill')
plt.show()

print("manaual calculation 1: \n",tips.groupby('day')['total_bill'].mean())

'''sns.barplot(data=tips, x='day', y='total_bill')

Behind the scenes, this is equivalent to:
tips.groupby('day')['total_bill'].mean()'''

sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
plt.show()

print("manaual calculation 2: \n",tips.groupby(['day','sex'])['total_bill'].mean())


# box plot

sns.boxplot(data=tips, x='day', y='total_bill')
plt.show()




'''
Boxplot With a Real-Life Example

Imagine 9 students' test scores, sorted from lowest to highest:

50, 55, 60, 65, 70, 75, 80, 85, 100

A boxplot cuts this into 4 equal groups (quarters).

Step-by-Step Breakdown

1. Find the Median (middle value)

50, 55, 60, 65, [70], 75, 80, 85, 100
                  ↑
              middle value = 70

This is the line inside the box.

2. Find the Middle 50% of Data (the box itself)

Split remaining data in half:

Lower half: 50, 55, 60, 65   → median of this = 57.5 (bottom of box)
Upper half: 75, 80, 85, 100  → median of this = 82.5 (top of box)
        ┌─────┐  ← 82.5 (top of box)
        │  70 │  ← 70 (median line)
        └─────┘  ← 57.5 (bottom of box)

The box contains the "typical middle" — 50% of all students scored between 57.5 and 82.5.

3. Whiskers (the lines sticking out)

        ┌─────┐
   ─────┤ 70  ├─────
        └─────┘

Left whisker  → goes down to lowest NORMAL value (50)
Right whisker → goes up to highest NORMAL value (85 or so)

4. Outliers (dots)

100 is unusually high compared to everyone else
→ shown as a separate DOT above the whisker, not connected
        ┌─────┐
   ─────┤ 70  ├─────        •  ← 100 (outlier)
        └─────┘
       50    85
Full Picture
                    • 100  ← outlier (unusually high)
                    
        ┌─────────┐
   ─────┤   70    ├─────
        └─────────┘
       50         85
   
   ↑              ↑     ↑        ↑
whisker         box    box    whisker
 (low)         bottom  top     (high)
In Plain English
Box     = "most students scored in this range"
Line    = "the middle score"
Whiskers = "the normal low and high scores"
Dots    = "weird scores that don't fit the pattern"'''

                                                        # histplot  → distribution of one variable
                                                        # barplot   → average comparison across categories 
                                                        # boxplot   → spread + outliers across categories 


sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.show()


# scatteplot


sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.show()

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.show()


# heat map

corellation=tips.corr(numeric_only=True)
print(corellation)

# sns.heatmap(corellation,annot=True,fmt='.2f',cmap='coolwarm')
# plt.show()

'''
Rule for Reading Correlation
1.0   → perfect relationship (always true — a column vs itself)
0.7-0.9 → strong relationship
0.4-0.6 → moderate relationship
0.0-0.3 → weak/no relationship
-1.0  → perfect NEGATIVE relationship (one goes up, other goes down)
'''

sns.heatmap(corellation, annot=True, fmt='.2f', cmap='coolwarm', vmin=0, vmax=1)
plt.show()


# pairplot

sns.pairplot(tips[['total_bill', 'tip', 'size']])
plt.show()


sns.pairplot(tips[['total_bill', 'tip', 'size', 'time']], hue='time')
plt.show()