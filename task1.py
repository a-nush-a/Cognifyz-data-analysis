import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Dataset.csv')

print(df.head())
print(df.columns)
from collections import Counter

# Remove empty values and split cuisines
cuisines = df['Cuisines'].dropna().str.split(', ')

all_cuisines = []

# Combine all cuisines into one list
for cuisine_list in cuisines:
    all_cuisines.extend(cuisine_list)

# Count each cuisine
cuisine_count = Counter(all_cuisines)

# Get top 3 cuisines
top_3 = cuisine_count.most_common(3)

print(top_3)
total_restaurants = len(df)

for cuisine, count in top_3:
    percentage = (count / total_restaurants) * 100
    print(cuisine, ":", round(percentage, 2), "%")
names = [x[0] for x in top_3]
counts = [x[1] for x in top_3]

plt.bar(names, counts)

plt.title("Top 3 Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Count")

plt.savefig("top_cuisines.png")
plt.show()
