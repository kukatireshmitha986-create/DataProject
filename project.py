import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("dataset/sales.csv")

# Data Cleaning
df = df.drop_duplicates()
df = df.fillna(df.mean(numeric_only=True))

# Save Cleaned Dataset
df.to_csv("cleaned data/cleaned_sales.csv", index=False)

# ---------------- CHART 1 ----------------
plt.figure(figsize=(8, 5))
sns.histplot(df['Today'], bins=20, kde=True)
plt.title("Distribution of Daily Returns")
plt.xlabel("Today")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("visuals/chart1.png")
plt.close()

# ---------------- CHART 2 ----------------
plt.figure(figsize=(8, 5))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visuals/chart2.png")
plt.close()

# ---------------- CHART 3 ----------------
plt.figure(figsize=(6, 6))

direction_counts = df['Direction'].value_counts()

plt.pie(
    direction_counts,
    labels=direction_counts.index,
    autopct='%1.1f%%'
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Sales Direction Analysis")
plt.tight_layout()
plt.savefig("visuals/chart3.png")
plt.close()

# ---------------- CHART 4 ----------------
yearly_sales = df.groupby('Year')['Today'].mean()

plt.figure(figsize=(8, 5))
plt.plot(
    yearly_sales.index,
    yearly_sales.values,
    marker='o'
)

plt.title("Average Return Trend by Year")
plt.xlabel("Year")
plt.ylabel("Average Return")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/chart4.png")
plt.close()

# ---------------- CHART 5 ----------------
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df[['Lag1', 'Lag2', 'Lag3', 'Lag4', 'Lag5']]
)

plt.title("Outlier Analysis")
plt.tight_layout()
plt.savefig("visuals/chart5.png")
plt.close()

print("Dashboard Charts Created Successfully!")