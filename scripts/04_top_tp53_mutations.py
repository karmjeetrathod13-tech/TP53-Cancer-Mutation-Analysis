import pandas as pd
import matplotlib.pyplot as plt

# Load mutation counts
data = pd.read_csv("../results/TP53_mutation_types.csv")

# Select the top 10 mutations
top10 = data.head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(top10["TP53"], top10["Count"])

# Labels and title
plt.title("Top 10 Most Frequent TP53 Mutations")
plt.xlabel("TP53 Mutation")
plt.ylabel("Number of Samples")

# Add values above bars
for i, value in enumerate(top10["Count"]):
    plt.text(i, value + 0.5, str(value), ha="center")

# Save figure
plt.savefig(
    "../figures/Top_10_TP53_Mutations.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()