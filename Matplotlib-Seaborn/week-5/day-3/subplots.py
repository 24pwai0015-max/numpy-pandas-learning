import matplotlib.pyplot as plt
# method 1
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1200, 1500, 1800, 1400, 2000, 2200]

subjects = ['Math', 'English', 'Science', 'History']
scores = [85, 72, 90, 68]

male_score = [55, 67, 54, 68]
female_score = [33, 66, 77, 87]


# Create figure
plt.figure(figsize=(12, 8))


# -------------------------
# Plot 1: Sales
# -------------------------
plt.subplot(2, 2, 1)

plt.title(
    'Sales $ Analysis',
    color="#6F0707",
    fontsize=16,
    fontstyle='italic'
)

plt.plot(
    months,
    sales,
    color="#0D3FD4",
    linewidth=1,
    markersize=5,
    marker='o'
)

plt.xlabel('Months')
plt.ylabel('Sales $')
plt.ylim(0, 3000)
plt.grid(True, alpha=0.5)


# -------------------------
# Plot 2: Subjects vs Scores
# -------------------------
plt.subplot(2, 2, 2)

plt.title(
    'Subjects vs Scores',
    color="#6F0707",
    fontsize=16,
    fontstyle='italic'
)

plt.bar(
    subjects,
    scores,
    color="#0D3FD4"
)

plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.ylim(0, 100)


# -------------------------
# Plot 3: Male vs Female
# -------------------------
plt.subplot(2, 2, 3)

plt.title(
    'Gender Score Analysis',
    color="#6F0707",
    fontsize=16,
    fontstyle='italic'
)

plt.scatter(
    subjects,
    male_score,
    label='Male',
    color="#6F0707"
)

plt.scatter(
    subjects,
    female_score,
    label='Female',
    color="#11E9AF"
)

plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.ylim(0, 100)

plt.legend()


# Adjust spacing
plt.tight_layout()

# Display all plots
plt.show()

# method 2
fig, axes = plt.subplots(1, 2, figsize=(10, 6))  # ✅ added 's'

axes[0].set_title('months and sales analysis',
                  color="#E81010",
                  fontweight='bold',              # ✅ fixed
                  fontsize=16)
axes[0].plot(months, sales)
axes[0].set_xlabel('months')
axes[0].set_ylabel('sales')
axes[0].grid(True, alpha=0.5)

axes[1].bar(subjects, scores, color='green')
axes[1].set_title('Subject Scores')
axes[1].set_xlabel('Subject')
axes[1].set_ylabel('Score')

plt.tight_layout()   # ← add this too
plt.show()