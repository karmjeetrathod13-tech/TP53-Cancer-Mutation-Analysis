import pandas as pd
import matplotlib.pyplot as plt

# Load region distribution data
data = pd.read_csv("../results/TP53_region_distribution.csv")

# Rename columns
data.columns = ["Protein_Region", "Mutation_Count"]

# Sort regions by starting position
data["Start"] = data["Protein_Region"].str.split("-").str[0].astype(int)
data = data.sort_values("Start")

# Plot
plt.figure(figsize=(10, 6))

plt.bar(
    data["Protein_Region"],
    data["Mutation_Count"]
)

plt.xlabel("Protein Region (amino acid positions)")
plt.ylabel("Number of Mutations")
plt.title("Distribution of TP53 Mutations Across Protein Regions")

plt.xticks(rotation=45)
plt.tight_layout()

# Save figure
plt.savefig("../figures/TP53_Protein_Region_Distribution.png", dpi=300)

plt.show()

print("Figure 7 created successfully.")