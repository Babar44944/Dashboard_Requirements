"""
Student Performance Dashboard
==============================
Generates dataset insights and visualizations (Matplotlib + Seaborn)
for the Student Performance dataset.

Author: Babar Ali
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------------------------------------------------
# Config
# ----------------------------------------------------------------
DATA_PATH = "student_performance.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 110
PALETTE = "viridis"

# ----------------------------------------------------------------
# Load Data
# ----------------------------------------------------------------
df = pd.read_csv(DATA_PATH)

# ----------------------------------------------------------------
# 1. Dataset Insights
# ----------------------------------------------------------------
total_records = len(df)
avg_marks = df["Final_Score"].mean()
avg_attendance = df["Attendance_Percentage"].mean()

print("=" * 50)
print("DATASET INSIGHTS")
print("=" * 50)
print(f"Total Records      : {total_records}")
print(f"Average Marks       : {avg_marks:.2f}")
print(f"Average Attendance  : {avg_attendance:.2f}%")
print("=" * 50)

# Save insights to a text file (used later by README / dashboard summary)
with open(os.path.join(OUTPUT_DIR, "insights.txt"), "w") as f:
    f.write("DATASET INSIGHTS\n")
    f.write("=" * 30 + "\n")
    f.write(f"Total Records      : {total_records}\n")
    f.write(f"Average Marks      : {avg_marks:.2f}\n")
    f.write(f"Average Attendance : {avg_attendance:.2f}%\n")

# ----------------------------------------------------------------
# 2. Chart 1 - Attendance Distribution
# ----------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Attendance_Percentage"], bins=20, kde=True, color="#4C72B0")
plt.axvline(avg_attendance, color="red", linestyle="--", linewidth=1.5,
            label=f"Average = {avg_attendance:.1f}%")
plt.title("Attendance Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "attendance_distribution.png"))
plt.close()

# ----------------------------------------------------------------
# 3. Chart 2 - Marks Distribution
# ----------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Final_Score"], bins=20, kde=True, color="#55A868")
plt.axvline(avg_marks, color="red", linestyle="--", linewidth=1.5,
            label=f"Average = {avg_marks:.1f}")
plt.title("Marks Distribution", fontsize=14, fontweight="bold")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "marks_distribution.png"))
plt.close()

# ----------------------------------------------------------------
# 4. Chart 3 - Feature Correlation Heatmap
# ----------------------------------------------------------------
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            linewidths=0.5, square=True, cbar_kws={"shrink": 0.8})
plt.title("Feature Correlation Heatmap", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "correlation_heatmap.png"))
plt.close()

# ----------------------------------------------------------------
# 5. Chart 4 - Performance Categories
# ----------------------------------------------------------------
plt.figure(figsize=(8, 5))
grade_order = ["A", "B", "C", "D", "F"]
grade_counts = df["Final_Performance_Grade"].value_counts().reindex(grade_order)
colors = sns.color_palette(PALETTE, len(grade_order))
ax = sns.barplot(x=grade_counts.index, y=grade_counts.values, hue=grade_counts.index, palette=colors, legend=False)
for i, v in enumerate(grade_counts.values):
    ax.text(i, v + 5, str(v), ha="center", fontweight="bold")
plt.title("Performance Categories (Grade Distribution)", fontsize=14, fontweight="bold")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "performance_categories.png"))
plt.close()

# ----------------------------------------------------------------
# 6. Combined Dashboard (single image, all 4 charts + insights)
# ----------------------------------------------------------------
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, height_ratios=[0.4, 1, 1])

# --- Insights header ---
ax_header = fig.add_subplot(gs[0, :])
ax_header.axis("off")
ax_header.text(0.5, 0.7, "Student Performance Dashboard",
                fontsize=22, fontweight="bold", ha="center")
insight_text = (
    f"Total Records: {total_records}      |      "
    f"Average Marks: {avg_marks:.2f}      |      "
    f"Average Attendance: {avg_attendance:.2f}%"
)
ax_header.text(0.5, 0.2, insight_text, fontsize=13, ha="center", color="#333333")

# --- Attendance Distribution ---
ax1 = fig.add_subplot(gs[1, 0])
sns.histplot(df["Attendance_Percentage"], bins=20, kde=True, color="#4C72B0", ax=ax1)
ax1.axvline(avg_attendance, color="red", linestyle="--", linewidth=1.2)
ax1.set_title("Attendance Distribution", fontweight="bold")

# --- Marks Distribution ---
ax2 = fig.add_subplot(gs[1, 1])
sns.histplot(df["Final_Score"], bins=20, kde=True, color="#55A868", ax=ax2)
ax2.axvline(avg_marks, color="red", linestyle="--", linewidth=1.2)
ax2.set_title("Marks Distribution", fontweight="bold")

# --- Correlation Heatmap ---
ax3 = fig.add_subplot(gs[2, 0])
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5,
            square=True, cbar=False, ax=ax3, annot_kws={"size": 8})
ax3.set_title("Feature Correlation Heatmap", fontweight="bold")

# --- Performance Categories ---
ax4 = fig.add_subplot(gs[2, 1])
sns.barplot(x=grade_counts.index, y=grade_counts.values, hue=grade_counts.index, palette=colors, legend=False, ax=ax4)
for i, v in enumerate(grade_counts.values):
    ax4.text(i, v + 5, str(v), ha="center", fontweight="bold", fontsize=9)
ax4.set_title("Performance Categories", fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "full_dashboard.png"), dpi=130)
plt.close()

print("\nAll charts + dashboard saved in the 'outputs' folder.")
