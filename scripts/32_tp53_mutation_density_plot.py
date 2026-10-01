import pandas as pd
import matplotlib.pyplot as plt

# Load mutation density data
data = pd.read_csv(
    "../results/TP53_25aa_Mutation_Density.csv"
)

# Extract window starting positions
data["Start"] = (
    data["Window"]
    .str.split("-")
    .str[0]
    .astype(int)
)

# Plot
plt.figure(figsize=(11, 6))

plt.bar(
    data["Start"],
    data["Count"],
    width=20
)

plt.xlabel("TP53 Protein Position")
plt.ylabel("Number of Mutations")
plt.title("TP53 Mutation Density Across 25-Amino-Acid Windows")

plt.xticks(data["Start"])
plt.tight_layout()

# Save figure
plt.savefig(
    "../figures/TP53_25aa_Mutation_Density.png",
    dpi=300
)

plt.show()

print("Figure 14 created successfully.")