import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset.csv')

# Top voted restaurants
top_voted = df[['Restaurant Name', 'Votes']].sort_values(by='Votes', ascending=False)

print("Top 10 Restaurants by Votes")
print(top_voted.head(10))

# Create graph
top10 = top_voted.head(10)

plt.bar(top10['Restaurant Name'], top10['Votes'])

plt.title("Top 10 Restaurants by Votes")
plt.xlabel("Restaurant Name")
plt.ylabel("Votes")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("top_voted_restaurants.png")
plt.show()