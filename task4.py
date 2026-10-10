import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset.csv')

# Restaurants with highest ratings
top_rated = df[['Restaurant Name', 'Aggregate rating', 'Votes']]

top_rated = top_rated.sort_values(
    by=['Aggregate rating', 'Votes'],
    ascending=False
)

print("Top 10 Highest Rated Restaurants")
print(top_rated.head(10))

# Scatter plot between votes and ratings
plt.scatter(df['Votes'], df['Aggregate rating'])

plt.title("Votes vs Aggregate Rating")
plt.xlabel("Votes")
plt.ylabel("Aggregate Rating")

plt.savefig("votes_vs_rating.png")
plt.show()