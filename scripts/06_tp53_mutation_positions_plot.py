import pandas as pd
import matplotlib.pyplot as plt

# Load mutation position data
data = pd.read_csv("../results/TP53_mutation_positions.csv")

# Select top 10 positions
top10 = data.sort_values("Count", ascending=False).head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(top10.index.astype(str), top10["Count"])

plt.title("Top 10 Frequently Mutated Positions in TP53")
plt.xlabel("Amino Acid Position")
plt.ylabel("Number of Mutations")

# Add values
for i, value in enumerate(top10["Count"]):
    plt.text(i, value + 0.3, str(value), ha="center")

# Save figure
plt.savefig(
    "../figures/Top_10_TP53_Mutation_Positions.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()