# ⚡ Week 5 Day 6 — Pandas + Matplotlib Quick Reference

A fast, copy-pasteable reference guide for integrating Pandas data manipulation with Matplotlib and Seaborn visualization.

---

## 🚀 Quick Syntax Cheat Sheet

### Pandas Built-in `.plot()`
```python
# Call directly on any aggregated Series or DataFrame
series.plot(kind='bar', color='skyblue', edgecolor='black')
series.plot(kind='barh', color='teal')         # Horizontal bars
series.plot(kind='line', marker='o')           # Line plot
series.plot(kind='pie', autopct='%1.1f%%')     # Pie plot
series.plot(kind='box')                        # Box plot
```

### Routing Plots to Subplot Axes (`ax=`)
```python
# Direct Pandas or Seaborn output into a specific subplot axis:
series.plot(kind='bar', ax=axes[row, col])
sns.heatmap(pivot_table, ax=axes[row, col])
```

---

## 📋 Production Recipes

### 1. Groupby + Pandas `.plot(kind='bar')`
```python
avg_metric = df.groupby('Category_Col')['Numeric_Col'].mean()

plt.figure(figsize=(8, 5))
avg_metric.plot(kind='bar', color='#C31616', edgecolor='black')
plt.title('Average Metric by Category', fontweight='bold', fontsize=14)
plt.xlabel('Category')
plt.ylabel('Average Value')
plt.xticks(rotation=0)  # Keep labels horizontal
plt.tight_layout()
plt.show()
```

### 2. Groupby + Matplotlib `plt.bar(index, values)`
```python
avg_series = df.groupby('Category_Col')['Numeric_Col'].mean()

plt.figure(figsize=(8, 5))
plt.bar(avg_series.index, avg_series.values, color='#1f77b4', edgecolor='black', width=0.5)
plt.title('Category Comparison', fontweight='bold', fontsize=14)
plt.xlabel('Category')
plt.ylabel('Metric')
plt.tight_layout()
plt.show()
```

### 3. Multi-Groupby + `.unstack()` + Heatmap
```python
# Convert 2-level Groupby into a 2D matrix
matrix = df.groupby(['Row_Col', 'Col_Col'])['Target_Col'].mean().unstack()

plt.figure(figsize=(7, 5))
sns.heatmap(matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=0, vmax=1)
plt.title('Interaction Matrix Heatmap', fontweight='bold', fontsize=14)
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.tight_layout()
plt.show()
```

### 4. `value_counts()` + Styled Pie Chart
```python
counts = df['Categorical_Col'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    counts,
    labels=counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=['#2ca02c', '#d62728', '#1f77b4'],
    explode=[0.05 if i == 0 else 0 for i in range(len(counts))],
    shadow=True
)
plt.title('Category Share Distribution', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.show()
```

### 5. Multi-Metric Named Aggregations (`.agg()`)
```python
summary_table = df.groupby('Group_Col').agg(
    rate=('Target_Binary_Col', 'mean'),
    average=('Continuous_Col', 'mean'),
    median=('Continuous_Col', 'median'),
    count=('Group_Col', 'count')
)

# Plot an individual metric from the table:
summary_table['rate'].plot(kind='bar', color='#2ca02c', edgecolor='black')
plt.xticks(rotation=0)
plt.title('Calculated Rate by Group')
plt.show()
```

### 6. Two-Way Pivot Table Heatmap
```python
pivot_matrix = df.pivot_table(
    values='Metric_Col',
    index='Row_Category',
    columns='Column_Category',
    aggfunc='mean'
)

plt.figure(figsize=(8, 6))
sns.heatmap(pivot_matrix, annot=True, fmt='.1f', cmap='YlGnBu')
plt.title('Pivot Table Cross-Analysis', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.show()
```

### 7. Executive 2x2 Analytical Dashboard
```python
fig, axes = plt.subplots(2, 2, figsize=(15, 11))

# Top-Left: Bar
metric_1.plot(kind='bar', ax=axes[0, 0], color='#d9534f', edgecolor='black')
axes[0, 0].set_title('Chart 1: Groupby Bar', fontweight='bold')
axes[0, 0].tick_params(axis='x', rotation=0)

# Top-Right: Heatmap
sns.heatmap(pivot_table, ax=axes[0, 1], annot=True, fmt='.1f', cmap='YlGnBu')
axes[0, 1].set_title('Chart 2: Heatmap Matrix', fontweight='bold')

# Bottom-Left: Pie
axes[1, 0].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
axes[1, 0].set_title('Chart 3: Composition Pie', fontweight='bold')

# Bottom-Right: Metric Bar
summary['rate'].plot(kind='bar', ax=axes[1, 1], color='#0275d8', edgecolor='black')
axes[1, 1].set_title('Chart 4: Summary Rate', fontweight='bold')
axes[1, 1].tick_params(axis='x', rotation=0)

fig.suptitle('Executive Analysis Dashboard', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

---

## 🎛️ Method Mapping Reference: `plt` vs `axes`

| Operation | Standalone Chart (`plt`) | Subplot Axis (`axes[row, col]`) |
|---|---|---|
| Set Title | `plt.title('Title')` | `ax.set_title('Title')` |
| Set X Label | `plt.xlabel('X')` | `ax.set_xlabel('X')` |
| Set Y Label | `plt.ylabel('Y')` | `ax.set_ylabel('Y')` |
| Set Y Limits | `plt.ylim(0, 100)` | `ax.set_ylim(0, 100)` |
| Set Grid | `plt.grid(True)` | `ax.grid(True)` |
| Rotate X Ticks | `plt.xticks(rotation=0)` | `ax.tick_params(axis='x', rotation=0)` |
| Add Master Title | `plt.suptitle('Main')` | `fig.suptitle('Main')` |

---

## 🎨 Recommended Palettes

| Palette / Colormap | Best Used For |
|---|---|
| `'coolwarm'` | Bipolar data (rates 0 to 1, correlation -1 to +1) |
| `'YlGnBu'` / `'Blues'` | Sequential magnitudes (fares, revenue, counts) |
| `'Set2'` / `'Pastel1'` | Categorical comparisons (gender, ports, classes) |
| `'viridis'` | Perceptually uniform continuous values |

---

## 💡 Top 3 Pro Tips
1. **Never use `plt.xlabel = 'text'`:** Calling functions requires parentheses: `plt.xlabel('text')`.
2. **Prevent label collision:** Always call `plt.tight_layout()` right before `plt.show()`.
3. **Always unpack `.mode()[0]`:** Imputing categorical nulls with `.mode()` needs `[0]` to convert the returned Pandas Series into a string scalar.
