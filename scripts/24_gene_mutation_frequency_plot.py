import pandas as pd
import matplotlib.pyplot as plt

# Load gene mutation frequency data
data = pd.read_csv(
    "../results/Gene_Mutation_Frequency.csv"
)

# Sort from highest to lowest
data = data.sort_values(
    "Mutation_Percentage",
    ascending=False
)

# Plot
plt.figure(figsize=(9, 6))

plt.bar(
    data["Gene"],
    data["Mutation_Percentage"]
)

plt.xlabel("Gene")
plt.ylabel("Mutation Frequency (%)")
plt.title("Mutation Frequency Across TP53-Related Genes")

plt.tight_layout()

# Save figure
plt.savefig(
    "../figures/TP53_Related_Gene_Mutation_Frequency.png",
    dpi=300
)

plt.show()

print("Figure 10 created successfully.")