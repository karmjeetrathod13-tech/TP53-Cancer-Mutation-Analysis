import pandas as pd
import matplotlib.pyplot as plt

# Load hotspot results
data = pd.read_csv("../results/TP53_mutation_hotspots.csv")

# Select top 15 hotspot positions
top15 = data.sort_values(
    "Unique_Mutation_Variants",
    ascending=False
).head(15)

# Create plot
plt.figure(figsize=(10, 6))
plt.bar(
    top15.index.astype(str),
    top15["Unique_Mutation_Variants"]
)

plt.title("TP53 Mutation Hotspots")
plt.xlabel("Amino Acid Position")
plt.ylabel("Number of Different Mutation Variants")

# Add values
for i, value in enumerate(top15["Unique_Mutation_Variants"]):
    plt.text(i, value + 0.05, str(value), ha="center")

plt.xticks(rotation=45)

# Save figure
plt.savefig(
    "../figures/TP53_Mutation_Hotspots.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()