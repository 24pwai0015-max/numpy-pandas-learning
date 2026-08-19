# Week 5 Day 3 — Subplots

## What Are Subplots?
Subplots let you display multiple charts in one figure — 
side by side or in a grid. Used in dashboards and reports 
to compare related data at a glance.

## Two Methods

### Method 1 — plt.subplot() (Quick)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)   # 1 row, 2 cols, position 1
plt.plot(x, y)
plt.title('Chart 1')

plt.subplot(1, 2, 2)   # 1 row, 2 cols, position 2
plt.bar(x, y)
plt.title('Chart 2')

plt.tight_layout()
plt.show()
```

### Method 2 — plt.subplots() (Recommended)
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x, y)
axes[0].set_title('Chart 1')

axes[1].bar(x, y)
axes[1].set_title('Chart 2')

plt.tight_layout()
plt.show()
```

## Grid Layout — Understanding Positions

### 1 Row, 2 Columns

## Key Difference — plt vs axes

| plt.subplot() | plt.subplots() |
|---|---|
| plt.title() | axes[i].set_title() |
| plt.xlabel() | axes[i].set_xlabel() |
| plt.ylabel() | axes[i].set_ylabel() |
| plt.grid() | axes[i].grid() |
| plt.plot() | axes[i].plot() |

## Important Parameters

| Parameter | What it does |
|---|---|
| figsize=(w, h) | Overall figure size |
| sharex=True | Share x axis across subplots |
| sharey=True | Share y axis across subplots |
| fig.suptitle() | Main title above all subplots |
| plt.tight_layout() | Fix spacing between subplots |

## When to Use Subplots
- Comparing multiple variables side by side
- Building dashboards
- Showing before/after cleaning
- Presenting multiple insights at once

## Tasks
1. 1x2 layout using plt.subplot() — line + bar
2. 2x1 layout using plt.subplot() — scatter + histogram
3. 1x2 layout using plt.subplots() — line + bar
4. 2x2 dashboard using plt.subplots() + fig.suptitle()
5. sharex=True — two charts sharing same x axis
6. BONUS: Titanic 2x2 dashboard


