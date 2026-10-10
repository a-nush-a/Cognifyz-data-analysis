import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset.csv')

# Remove empty cuisines
cuisine_data = df.dropna(subset=['Cuisines'])

# Split cuisines
cuisine_data['Cuisines'] = cuisine_data['Cuisines'].str.split(', ')

# Separate multiple cuisines into rows
exploded = cuisine_data.explode('Cuisines')

# Calculate average rating
avg_cuisine_rating = exploded.groupby('Cuisines')['Aggregate rating'].mean()

# Sort highest ratings
top_cuisines = avg_cuisine_rating.sort_values(ascending=False).head(10)

print("Top 10 Cuisines by Average Rating")
print(round(top_cuisines, 2))

# Create graph
top_cuisines.plot(kind='bar')

plt.title("Top 10 Cuisines by Average Rating")
plt.xlabel("Cuisine")
plt.ylabel("Average Rating")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_cuisine_ratings.png")
plt.show()