# Week 5 Day 1 — Matplotlib Basics

## What is Matplotlib?
Matplotlib is Python's core visualization library.
It turns numbers into charts people can understand.

## Core Structure
Every chart follows the same pattern:
```python
import matplotlib.pyplot as plt
plt.chart_type(x_data, y_data)
plt.title('Title')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.show()
```

## Chart Types

| Function | Chart Type | Use When |
|---|---|---|
| plt.plot() | Line chart | Trends over time |
| plt.bar() | Bar chart | Comparing categories |
| plt.barh() | Horizontal bar | Long category names |
| plt.scatter() | Scatter plot | Relationship between two variables |
| plt.hist() | Histogram | Distribution of one variable |
| plt.pie() | Pie chart | Parts of a whole |

## Key Parameters

| Parameter | What it does |
|---|---|
| figsize=(w,h) | Set chart width and height |
| bins=n | Number of buckets in histogram |
| autopct='%1.1f%%' | Show percentages on pie chart |
| startangle=90 | Rotate pie chart start position |
| shadow=True | Add shadow to pie chart |
| colors=[...] | Custom colors (hex or named) |

## Saving Charts
```python
plt.savefig('filename.png')  # always before plt.show()
```

## Tasks
1. Line chart — monthly sales data
2. Bar chart — subject scores
3. Horizontal bar chart — same data
4. Scatter plot — age vs salary
5. Histogram — 500 random ages, bins=15
6. Pie chart — Titanic class distribution
7. Save one chart as .png
8. BONUS: Titanic survival bar chart using value_counts()SSS