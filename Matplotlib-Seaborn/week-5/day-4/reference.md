# ⚡ Week 5 Day 4 — Seaborn Quick Reference

Fast syntax recipes for Seaborn's core statistical visualization methods.

---

## 🚀 Theme Setup
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')  # 'whitegrid' | 'darkgrid' | 'white' | 'dark' | 'ticks'
```

---

## 📋 Plot Recipes

### 1. Histogram / Distribution (`sns.histplot`)
```python
# Basic distribution
sns.histplot(data=df, x='column_name', bins=20, kde=True, color='#2b5c8f')

# Grouped distribution
sns.histplot(data=df, x='column_name', bins=20, hue='category_col', multiple='stack', palette='Set1')
plt.title('Distribution Analysis')
plt.show()
```

### 2. Category Averages Bar Chart (`sns.barplot`)
```python
# Computes mean and confidence interval automatically
sns.barplot(data=df, x='category_x', y='numeric_y', hue='split_category', palette='Blues_d')
plt.title('Category Comparison')
plt.show()
```

### 3. Boxplot & Outliers (`sns.boxplot`)
```python
# 5-number summary across categories
sns.boxplot(data=df, x='category_x', y='numeric_y', hue='split_category', palette='Set3', showfliers=True)
plt.title('Spread & Outlier Analysis')
plt.show()
```

### 4. Scatter Plot (`sns.scatterplot`)
```python
# Continuous relationship with categorical hue
sns.scatterplot(data=df, x='x_continuous', y='y_continuous', hue='category', palette='coolwarm', alpha=0.8)
plt.title('Bivariate Relationship')
plt.show()
```

### 5. Correlation Heatmap (`sns.heatmap`)
```python
corr_matrix = df.corr(numeric_only=True)

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1, square=True)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
```

### 6. Bivariate Matrix Grid (`sns.pairplot`)
```python
# Pairwise relationships across all numeric columns
g = sns.pairplot(df[['col1', 'col2', 'col3', 'target']], hue='target', palette='Set1', diag_kind='kde')
g.figure.subplots_adjust(top=0.92)
g.figure.suptitle('Pairwise Feature Matrix', fontweight='bold', fontsize=14)
plt.show()
```

---

## 🎨 Palette Quick Reference

| Palette Name | Type | Example Use |
|---|---|---|
| `'coolwarm'` / `'RdBu'` | Diverging | Correlation heatmaps, positive vs negative sentiment |
| `'Blues'` / `'YlGnBu'` | Sequential | Ordered continuous metrics, transaction amounts |
| `'Set1'` / `'Set2'` | Qualitative | Categorical classes, gender, binary survival |
| `'Pastel1'` / `'Pastel2'` | Soft Qualitative | Boxplots with multiple categories |
