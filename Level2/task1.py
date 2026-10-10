import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset.csv')

# Display rating information
print("Aggregate Rating Statistics")
print(df['Aggregate rating'].describe())

# Count ratings
rating_count = df['Aggregate rating'].value_counts().sort_index()

print("\nRating Counts")
print(rating_count)

# Create histogram
plt.hist(df['Aggregate rating'], bins=10)

plt.title("Distribution of Aggregate Ratings")
plt.xlabel("Ratings")
plt.ylabel("Number of Restaurants")

plt.savefig("rating_distribution.png")
plt.show()