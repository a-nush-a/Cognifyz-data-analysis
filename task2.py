import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset.csv')

# Count restaurants by city
city_count = df['City'].value_counts()

print("Top Cities by Restaurant Count")
print(city_count.head(10))

# Average rating by city
avg_rating = df.groupby('City')['Aggregate rating'].mean()

print("\nTop Cities by Average Rating")
print(avg_rating.sort_values(ascending=False).head(10))

# Highest rated city
highest_rating_city = avg_rating.idxmax()

print("\nHighest Average Rating City:", highest_rating_city)

print("Highest Rating:", avg_rating.max())

# Create graph
city_count.head(10).plot(kind='bar')

plt.title("Top 10 Cities by Restaurant Count")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")

plt.savefig("city_analysis.png")
plt.show()