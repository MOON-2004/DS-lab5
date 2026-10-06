# Data Science Lab 05

## Probability Simulation & Exploratory Data Analysis (EDA)

**Course:** Data Science Lab
**Topic:** Probability Notebooks & EDA Workflow

---

## 📌 Lab Overview

This lab focuses on simulating common probability distributions using Python and performing **Exploratory Data Analysis (EDA)** on datasets.

The lab covers:

* Probability distribution simulation
* Random data generation using NumPy
* Histograms and data visualization
* Loading and inspecting datasets using Pandas
* Missing value detection
* Duplicate detection and removal
* Univariate analysis
* Bivariate analysis
* Correlation analysis
* Categorical analysis using `groupby()`
* Outlier detection using the IQR method
* Git and GitHub workflow

---

## 🛠️ Tools & Libraries

* Python 3.x
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Git
* GitHub
* VS Code / Jupyter Notebook

### Install Required Libraries

```bash
pip install numpy pandas matplotlib seaborn
```

---

# 📚 Lab Concepts

## Probability Distributions

The following distributions are simulated using NumPy:

* Uniform Distribution
* Normal (Gaussian) Distribution
* Binomial Distribution
* Poisson Distribution

Random samples are generated using functions from `numpy.random`.

---

## Exploratory Data Analysis (EDA)

EDA is used to understand the structure and quality of a dataset before further analysis.

The lab uses:

```python
df.shape
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
```

It also includes:

* Histograms
* Boxplots
* Scatter plots
* Correlation matrices
* Correlation heatmaps
* `value_counts()`
* `groupby()`

---

# 🧪 Lab Tasks

## Task 1 — Die Simulation

A fair six-sided die is simulated **1000 times** using:

```python
np.random.randint(1, 7, size=1000)
```

The program:

1. Prints the first 10 rolls.
2. Counts how many times each face appears.
3. Calculates empirical probability.
4. Compares empirical probability with theoretical probability `1/6`.
5. Creates a histogram of the die rolls.
6. Saves the histogram as:

```text
die_rolls.png
```

### Repository

```text
lab5-die-simulation
```

### Files

```text
die_simulation.py
die_rolls.png
```

---

## Task 2 — Student Performance EDA

A `student_performance.csv` dataset containing 12 students is created and analyzed.

Columns:

```text
StudentID
Gender
StudyHours
Attendance(%)
Marks
```

The dataset contains:

* 2 missing Marks values
* 1 duplicate row

The program:

1. Loads the CSV using `pd.read_csv()`.
2. Displays the dataset shape and information.
3. Detects missing values.
4. Detects duplicate rows.
5. Removes the duplicate row.
6. Fills missing Marks using the column median.
7. Creates a Marks histogram.
8. Creates a Marks boxplot.
9. Creates a Study Hours vs Marks scatter plot.
10. Calculates the numeric correlation matrix.
11. Uses `groupby("Gender")` to compare average Marks and Attendance.

### Repository

```text
lab5-student-eda
```

### Files

```text
student_eda.py
student_performance.csv
marks_histogram.png
marks_boxplot.png
studyhours_vs_marks.png
```

---

## Task 3 — Delivery Time Simulation

A `delivery_times.csv` dataset containing 100 synthetic deliveries is analyzed.

Columns:

```text
OrderID
DeliveryTime(min)
```

The program:

1. Calculates the mean delivery time.
2. Calculates the standard deviation.
3. Simulates 100 expected delivery times using a Normal distribution.
4. Compares real and simulated delivery times using overlapping histograms.
5. Checks for missing values.
6. Creates a delivery-time boxplot.
7. Calculates the 25th, 50th, and 75th percentiles.
8. Calculates the IQR.
9. Uses the IQR method to identify outliers.
10. Calculates the percentage of deliveries flagged as outliers.

### Repository

```text
lab5-delivery-sim
```

### Files

```text
delivery_sim.py
delivery_times.csv
delivery_comparison_histogram.png
delivery_boxplot.png
```

---

# 📊 Visualizations

The lab produces the following visualizations:

### Task 1

```text
die_rolls.png
```

Histogram showing the frequency of each die face.

### Task 2

```text
marks_histogram.png
marks_boxplot.png
studyhours_vs_marks.png
```

These visualize the distribution of Marks, possible outliers, and the relationship between Study Hours and Marks.

### Task 3

```text
delivery_comparison_histogram.png
delivery_boxplot.png
```

These compare real and simulated delivery times and help identify unusual delivery times.

---

# 📈 Outlier Detection

Task 3 uses the **Interquartile Range (IQR)** method.

```text
IQR = Q3 - Q1
```

The outlier boundaries are:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Values outside these boundaries are flagged as potential outliers.

---

# 🔀 Git Workflow

Each task is organized as a Git repository.

Basic workflow:

```bash
git init
git status
git add .
git commit -m "Complete Lab 5 task"
git remote add origin <github-repository-url>
git branch -M main
git push -u origin main
```

The completed repositories are pushed to GitHub along with the Python scripts, datasets, and generated plots.

---



## 🎯 Learning Outcomes

After completing this lab, the following skills are practiced:

* Simulating probability distributions with NumPy
* Generating random data
* Working with Pandas DataFrames
* Inspecting datasets
* Handling missing values
* Removing duplicate records
* Performing univariate and bivariate analysis
* Calculating correlations
* Grouping and summarizing categorical data
* Detecting outliers using IQR
* Creating data visualizations
* Managing projects with Git
* Uploading projects to GitHub

---
