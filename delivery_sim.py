import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Create synthetic delivery dataset
# --------------------------------------------------

np.random.seed(42)

# Generate 95 normal delivery times
normal_times = np.random.normal(
    loc=32,
    scale=6,
    size=95
)

# Add some intentionally long deliveries
outliers = np.array([60, 65, 70, 72, 75])

# Combine normal deliveries and outliers
delivery_times = np.concatenate(
    [normal_times, outliers]
)

# Make sure delivery times are positive
delivery_times = np.round(delivery_times, 1)

# Create order IDs
order_ids = np.arange(1, 101)

# Create DataFrame
df = pd.DataFrame({
    "OrderID": order_ids,
    "DeliveryTime(min)": delivery_times
})

# Save CSV
df.to_csv("delivery_times.csv", index=False)

# --------------------------------------------------
# 2. Calculate mean and standard deviation
# --------------------------------------------------

mean_time = df["DeliveryTime(min)"].mean()
std_time = df["DeliveryTime(min)"].std()

print(
    f"Real delivery times -- Mean: "
    f"{mean_time:.2f} min "
    f"Std: {std_time:.2f} min"
)

# --------------------------------------------------
# 3. Simulate 100 delivery times
# --------------------------------------------------

simulated_times = np.random.normal(
    loc=mean_time,
    scale=std_time,
    size=100
)

print(
    f"Simulated 100 values from "
    f"Normal(mean={mean_time:.2f}, "
    f"std={std_time:.2f})"
)

# --------------------------------------------------
# 4. Check missing values
# --------------------------------------------------

missing_values = df["DeliveryTime(min)"].isnull().sum()

print("\nMissing values:", missing_values)

# --------------------------------------------------
# 5. Calculate percentiles
# --------------------------------------------------

q1 = df["DeliveryTime(min)"].quantile(0.25)
q2 = df["DeliveryTime(min)"].quantile(0.50)
q3 = df["DeliveryTime(min)"].quantile(0.75)

print(
    f"Percentiles -- 25th: {q1:.2f} "
    f"50th: {q2:.2f} "
    f"75th: {q3:.2f}"
)

# --------------------------------------------------
# 6. IQR calculation
# --------------------------------------------------

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(
    f"IQR outlier bounds: "
    f"{lower_bound:.2f} - {upper_bound:.2f}"
)

# --------------------------------------------------
# 7. Find outliers
# --------------------------------------------------

outlier_mask = (
    (df["DeliveryTime(min)"] < lower_bound)
    |
    (df["DeliveryTime(min)"] > upper_bound)
)

outliers_df = df[outlier_mask]

print(
    "\nOutliers detected:",
    len(outliers_df)
)

print(outliers_df)

# --------------------------------------------------
# 8. Calculate outlier percentage
# --------------------------------------------------

outlier_percentage = (
    len(outliers_df) / len(df)
) * 100

print(
    f"Percentage flagged as outliers: "
    f"{outlier_percentage:.2f}%"
)

# --------------------------------------------------
# 9. Compare real and simulated data
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["DeliveryTime(min)"],
    bins=15,
    alpha=0.6,
    label="Real Delivery Times"
)

plt.hist(
    simulated_times,
    bins=15,
    alpha=0.6,
    label="Simulated Delivery Times"
)

plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Frequency")
plt.title("Real vs Simulated Delivery Times")

plt.legend()

plt.savefig("delivery_comparison_histogram.png")

plt.show()

# --------------------------------------------------
# 10. Boxplot
# --------------------------------------------------

plt.figure(figsize=(5, 4))

plt.boxplot(df["DeliveryTime(min)"])

plt.ylabel("Delivery Time (minutes)")
plt.title("Delivery Time Boxplot")

plt.savefig("delivery_boxplot.png")

plt.show()