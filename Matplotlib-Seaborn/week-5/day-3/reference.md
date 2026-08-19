# Week 5 Day 3 — Subplots Quick Reference

## Method 1 — plt.subplot()
```python
plt.figure(figsize=(12, 5))

plt.subplot(rows, cols, position)
plt.plot(x, y)
plt.title('Title')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.5)

plt.tight_layout()
plt.show()
```

## Method 2 — plt.subplots() 1D
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(x, y)
axes[0].set_title('Chart 1')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].grid(True, alpha=0.5)

axes[1].bar(x, y)
axes[1].set_title('Chart 2')

plt.tight_layout()
plt.show()
```

## Method 2 — plt.subplots() 2D Grid
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, y)
axes[0, 0].set_title('Top Left')

axes[0, 1].bar(x, y)
axes[0, 1].set_title('Top Right')

axes[1, 0].scatter(x, y)
axes[1, 0].set_title('Bottom Left')

axes[1, 1].hist(data, bins=10)
axes[1, 1].set_title('Bottom Right')

fig.suptitle('Dashboard Title', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
```

## Shared Axes
```python
# Share x axis
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Share y axis
fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)
```

## Figure Level vs Axes Level

| Action | Figure Level | Axes Level |
|---|---|---|
| Title | plt.title() | ax.set_title() |
| X label | plt.xlabel() | ax.set_xlabel() |
| Y label | plt.ylabel() | ax.set_ylabel() |
| Grid | plt.grid() | ax.grid() |
| X limits | plt.xlim() | ax.set_xlim() |
| Y limits | plt.ylim() | ax.set_ylim() |
| Legend | plt.legend() | ax.legend() |
| Plot | plt.plot() | ax.plot() |
| Bar | plt.bar() | ax.bar() |
| Scatter | plt.scatter() | ax.scatter() |
| Histogram | plt.hist() | ax.hist() |

## Common Layouts

```python
# Side by side (2 charts)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Stacked (2 charts)
fig, axes = plt.subplots(2, 1, figsize=(8, 10))

# 2x2 dashboard (4 charts)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1x3 (3 charts side by side)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
```

## Pro Tips
- Always use plt.tight_layout() — prevents labels overlapping
- fig.suptitle() for dashboard heading
- sharex=True when charts share same time/category axis
- figsize width should grow with number of columns
- figsize height should grow with number of rows