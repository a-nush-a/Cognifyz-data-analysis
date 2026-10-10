import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset.csv')

# Count restaurants by price range
price_count = df['Price range'].value_counts()

print("Restaurant Count by Price Range")
print(price_count)

# Calculate percentage
percentage = (price_count / len(df)) * 100

print("\nPercentage Distribution")
print(round(percentage, 2))

# Create graph
price_count.plot(kind='bar')

plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Restaurant Count")

plt.savefig("price_distribution.png")
plt.show()