import pandas as pd
import matplotlib.pyplot as plt

# Load functional region results
data = pd.read_csv("../results/TP53_mutations_functional_regions.csv")

# Count mutations in each region
region_counts = data.groupby(
    "Functional_Region"
)["Mutation_Count"].sum().sort_values(ascending=False)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(region_counts.index, region_counts.values)

plt.title("Distribution of TP53 Mutations Across Functional Regions")
plt.xlabel("Functional Region")
plt.ylabel("Number of Mutations")

plt.xticks(rotation=25, ha="right")

# Add values
for i, value in enumerate(region_counts.values):
    plt.text(i, value + 3, str(value), ha="center")

# Save figure
plt.savefig(
    "../figures/TP53_Functional_Region_Distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()