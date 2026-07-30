import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("iris.csv")

# Histogram
print("Histogram")
df.hist(figsize=(8,6))
plt.show()

# Box Plot
print("Box Plot")
sns.boxplot(data=df.iloc[:, :4])
plt.show()

# Scatter Plot
print("Scatter Plot")
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.show()

# Heatmap
print("Heatmap")
sns.heatmap(df.iloc[:, :4].corr(), annot=True)
plt.show()

# Bar Chart
print("Bar Chart")
df["species"].value_counts().plot(kind="bar")
plt.title("Count of Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

print("Data Visualization Completed Successfully!")