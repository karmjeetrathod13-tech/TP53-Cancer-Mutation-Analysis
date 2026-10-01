import pandas as pd
import matplotlib.pyplot as plt

# Load domain analysis
data = pd.read_csv(
    "../results/TP53_DNA_binding_domain_analysis.csv"
)

# Rename columns
data.columns = ["Region", "Mutation_Count"]

# Plot
plt.figure(figsize=(8, 6))

plt.bar(
    data["Region"],
    data["Mutation_Count"]
)

plt.xlabel("Protein Region")
plt.ylabel("Number of Mutations")
plt.title("TP53 Mutation Distribution in DNA-Binding Domain")

plt.xticks(rotation=15)
plt.tight_layout()

# Save figure
plt.savefig(
    "../figures/TP53_DNA_Binding_Domain_Distribution.png",
    dpi=300
)

plt.show()

print("Figure 9 created successfully.")