# Student Performance Dashboard

A Python-based analytics dashboard that explores a student performance dataset, generates statistical insights, and visualizes key trends using **Matplotlib** and **Seaborn**.

---

## Project Overview

This project analyzes student academic data to understand the relationship between study habits, attendance, assignments, and final exam performance. It produces a set of visual charts and summary statistics that highlight patterns in the data, which can later support performance-prediction modeling.

**Key outputs:**
- Dataset-level insights (total records, average marks, average attendance)
- Attendance distribution chart
- Marks distribution chart
- Feature correlation heatmap
- Performance category (grade) breakdown
- A combined dashboard image bringing all insights together

---

## Dataset Information

**File:** `student_performance.csv`
**Records:** 600
**Columns:**

| Column | Description |
|---|---|
| `Study_Hours_Per_Day` | Average hours a student studies per day |
| `Attendance_Percentage` | Class attendance percentage |
| `Assignments_Completed` | Number of assignments completed |
| `Previous_Semester_Marks` | Marks obtained in the previous semester |
| `Class_Participation` | Class participation score |
| `Final_Score` | Final exam score (target variable) |
| `Final_Performance_Grade` | Letter grade (A, B, C, D, F) derived from final score |

No missing values were found in the dataset.

---

## Model Used

This phase of the project focuses on **exploratory data analysis (EDA) and visualization** rather than predictive modeling. The correlation heatmap shows that `Assignments_Completed` (0.57) and `Previous_Semester_Marks` (0.51) have the strongest relationship with `Final_Score`, making them strong candidate features for a future predictive model (e.g., Linear Regression, Random Forest, or XGBoost).

---

## Installation Steps

1. **Clone or download** this project folder.
2. **Install required packages:**
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. **Place the dataset** (`student_performance.csv`) in the same folder as `dashboard.py`.
4. **Run the script:**
   ```bash
   python dashboard.py
   ```
5. Charts and insights will be saved automatically inside the `outputs/` folder.

---

## Screenshots

All generated charts are saved under `outputs/`:

| File | Description |
|---|---|
| `attendance_distribution.png` | Histogram of attendance percentages with average marker |
| `marks_distribution.png` | Histogram of final scores with average marker |
| `correlation_heatmap.png` | Correlation heatmap of all numeric features |
| `performance_categories.png` | Bar chart of grade distribution (A–F) |
| `full_dashboard.png` | Combined single-image dashboard with all insights and charts |
| `insights.txt` | Plain-text summary of dataset insights |

**Dataset Insights Summary:**
- Total Records: **600**
- Average Marks: **43.04**
- Average Attendance: **76.01%**

---

## Future Improvements

- Add an interactive **Chart.js / HTML dashboard** version for web-based viewing
- Build a predictive model (Random Forest / XGBoost) to forecast `Final_Score` and `Final_Performance_Grade`
- Add filters for comparing performance by attendance brackets or study-hour ranges
- Deploy the dashboard as a live web app (Flask/Streamlit)
- Add automated PDF report export of all insights and charts
