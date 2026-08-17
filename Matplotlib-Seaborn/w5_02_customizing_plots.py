# ============================================================
# MATPLOTLIB — CHART CUSTOMIZATION (Organized & Fixed)
# ============================================================

import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# 1. BASIC DATA
# ============================================================

months = ['January', 'February', 'March', 'April', 'May']
sales = [1400, 2344, 1232, 1456, 5556]

subjects = ['Math', 'English', 'Science', 'History']
scores = [85, 72, 90, 68]
male_scores = [72, 90, 68, 100]
female_scores = [78, 88, 85, 75]

# ============================================================
# 2. LINE CHART CUSTOMIZATION
# ============================================================

# --- 2.1 Dashed Line with Circular Markers ---
plt.figure(figsize=(8, 6))
plt.plot(months, sales, color='black', linestyle='--', linewidth=2, marker='o', markersize=6)
plt.title('Monthly Sales 2024', fontsize=16, fontweight='bold')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- 2.2 Solid Line with Square Markers ---
plt.figure(figsize=(8, 6))
plt.plot(months, sales, color='black', linestyle='-', linewidth=2, marker='s', markersize=6)
plt.title('Monthly Sales 2024', fontsize=16, fontweight='bold')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- 2.3 Dotted Line with Triangular Markers ---
plt.figure(figsize=(8, 6))
plt.plot(months, sales, color='black', linestyle=':', linewidth=2, marker='^', markersize=6)
plt.title('Monthly Sales 2024', fontsize=16, fontweight='bold', color='#550E0E')
plt.xlabel('Months', fontsize=10)
plt.ylabel('Sales ($)', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================
# 3. BAR CHART — SAME COLOR
# ============================================================

plt.figure(figsize=(7, 5))
plt.bar(subjects, scores, color='#631212')
plt.title('Student Results', fontsize=16, fontweight='bold')
plt.xlabel('Subjects', fontsize=12)
plt.ylabel('Scores', fontsize=12)
plt.tight_layout()
plt.show()

# ============================================================
# 4. BAR CHART — DIFFERENT COLORS
# ============================================================

colors = ['#1A5C82', '#A74141', '#1EA196', '#000000']

plt.figure(figsize=(7, 5))
plt.bar(subjects, scores, color=colors)
plt.title('Student Results', fontsize=16, fontweight='bold')
plt.xlabel('Subjects', fontsize=12)
plt.ylabel('Scores', fontsize=12)
plt.tight_layout()
plt.show()

# ============================================================
# 5. MULTIPLE DATA SERIES (Line Chart)
# ============================================================

plt.figure(figsize=(8, 6))
plt.plot(subjects, male_scores, label='Male', color='blue', marker='o')
plt.plot(subjects, female_scores, label='Female', color='pink', marker='o')
plt.title('Scores by Gender', fontsize=16, fontweight='bold')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================
# 6. STACKED BAR CHART
# ============================================================

plt.figure(figsize=(8, 6))
plt.bar(subjects, male_scores, label='Male', color='blue')
plt.bar(subjects, female_scores, bottom=male_scores, label='Female', color='pink')
plt.title('Scores by Gender (Stacked)', fontsize=16, fontweight='bold')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 7. SETTING AXIS LIMITS
# ============================================================

plt.figure(figsize=(8, 6))
plt.plot(months, sales, color='#730C0C', marker='o', linewidth=2)
plt.ylim(0, 6000)                    # set y-axis range
# plt.xlim(0, 4)                     # example of x-axis limit (optional)
plt.title('Monthly Sales with Axis Limits', fontsize=16, fontweight='bold')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.grid(True, color='#09A73B', alpha=0.4)
plt.tight_layout()
plt.show()

# ============================================================
# 8. ANNOTATIONS (Pointing to Specific Points)
# ============================================================

plt.figure(figsize=(8, 6))
plt.plot(months, sales, color='#730C0C', marker='o', linewidth=2)

plt.annotate('Peak Sales!',
             xy=('May', 5556),           # point to annotate
             xytext=('March', 4000),     # text position
             arrowprops=dict(arrowstyle='fancy', color='black'),
             fontsize=12,
             fontweight='bold')

plt.title('Monthly Sales with Annotation', fontsize=16, fontweight='bold')
plt.xlabel('Months')
plt.ylabel('Sales ($)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================
# 9. KEY CUSTOMIZATION OPTIONS (Reference)
# ============================================================

"""
figsize       → controls chart size
color         → changes line/bar color
linestyle     → changes line style ('-', '--', ':', '-.')
linewidth     → changes line thickness
marker        → changes data point shape ('o', 's', '^', etc.)
markersize    → changes marker size
fontsize      → changes text size
fontweight    → makes text bold
xlabel / ylabel → labels the axes
title         → adds a chart title
legend        → identifies different data series
grid          → adds background grid
tight_layout  → prevents labels from being cut off
xlim / ylim   → set axis limits
annotate      → add text + arrow to a specific point
"""

# Common arrow styles for annotate:
# arrowprops = dict(arrowstyle='->')
# arrowprops = dict(arrowstyle='-|>')
# arrowprops = dict(arrowstyle='fancy')
# arrowprops = dict(arrowstyle='wedge')

