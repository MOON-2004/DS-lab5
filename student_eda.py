import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Create student dataset
# --------------------------------------------------

data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11],

    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Male"
    ],

    "StudyHours": [
        2, 4, 3, 6,
        5, 7, 4, 8,
        3, 6, 5, 5
    ],

    "Attendance(%)": [
        75, 85, 80, 90,
        82, 95, 78, 92,
        76, 88, 84, 84
    ],

    "Marks": [
        60, 75, None, 88,
        70, 92, 65, 95,
        None, 82, 74, 74
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset as CSV
df.to_csv("student_performance.csv", index=False)

# Load CSV
df = pd.read_csv("student_performance.csv")

# --------------------------------------------------
# 2. Initial inspection
# --------------------------------------------------

print("Shape:", df.shape)

print("\nData information:")
df.info()

# --------------------------------------------------
# 3. Missing values and duplicates
# --------------------------------------------------

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# --------------------------------------------------
# 4. Remove duplicate row
# --------------------------------------------------

df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print("Shape:", df.shape)

# --------------------------------------------------
# 5. Fill missing Marks with median
# --------------------------------------------------

median_marks = df["Marks"].median()

df["Marks"] = df["Marks"].fillna(median_marks)

print("\nMedian Marks:", median_marks)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# --------------------------------------------------
# 6. Histogram of Marks
# --------------------------------------------------

plt.figure(figsize=(6, 4))

plt.hist(df["Marks"], bins=6, edgecolor="black")

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")

plt.savefig("marks_histogram.png")

plt.show()

# --------------------------------------------------
# 7. Boxplot of Marks
# --------------------------------------------------

plt.figure(figsize=(5, 4))

plt.boxplot(df["Marks"])

plt.ylabel("Marks")
plt.title("Marks Boxplot")

plt.savefig("marks_boxplot.png")

plt.show()

# --------------------------------------------------
# 8. Scatter plot
# --------------------------------------------------

plt.figure(figsize=(6, 4))

plt.scatter(df["StudyHours"], df["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.savefig("studyhours_vs_marks.png")

plt.show()

# --------------------------------------------------
# 9. Correlation matrix
# --------------------------------------------------

correlation = df[
    ["StudyHours", "Attendance(%)", "Marks"]
].corr()

print("\nCorrelation Matrix:")
print(correlation)

# --------------------------------------------------
# 10. Groupby Gender
# --------------------------------------------------

gender_summary = df.groupby("Gender")[
    ["Marks", "Attendance(%)"]
].mean()

print("\nAverage Marks and Attendance by Gender:")
print(gender_summary)