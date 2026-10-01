import pandas as pd
import matplotlib.pyplot as plt

# Load co-mutation data
data = pd.read_csv(
    "../results/TP53_Comutation_Analysis.csv"
)

# Sort by percentage
data = data.sort_values(
    "Percentage_of_TP53_Mutated",
    ascending=False
)

# Plot
plt.figure(figsize=(9, 6))

plt.bar(
    data["Gene"],
    data["Percentage_of_TP53_Mutated"]
)

plt.xlabel("Gene")
plt.ylabel("Samples with Co-Mutation (%)")
plt.title("Co-Mutation Profile Among TP53-Mutated Samples")

plt.tight_layout()

# Save figure
plt.savefig(
    "../figures/TP53_Comutation_Profile.png",
    dpi=300
)

plt.show()

print("Figure 11 created successfully.")