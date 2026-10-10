import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset.csv')

# Count online delivery options
delivery_count = df['Has Online delivery'].value_counts()

print("Online Delivery Count")
print(delivery_count)

# Calculate percentage
delivery_percentage = (delivery_count / len(df)) * 100

print("\nOnline Delivery Percentage")
print(round(delivery_percentage, 2))

# Compare ratings
rating_comparison = df.groupby('Has Online delivery')['Aggregate rating'].mean()

print("\nAverage Ratings Comparison")
print(round(rating_comparison, 2))

# Create graph
rating_comparison.plot(kind='bar')

plt.title("Online Delivery vs Average Ratings")
plt.ylabel("Average Rating")

plt.savefig("online_delivery.png")
plt.show()