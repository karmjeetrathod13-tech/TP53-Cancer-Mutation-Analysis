import pandas as pd
import matplotlib.pyplot as plt

# Load substitution data
data = pd.read_csv(
    "../results/TP53_amino_acid_substitutions.csv"
)

# Rename columns
data.columns = ["Substitution", "Count"]

# Select top 15
data = data.head(15)

# Plot
plt.figure(figsize=(10, 6))

plt.bar(
    data["Substitution"],
    data["Count"]
)

plt.xlabel("Amino-Acid Substitution")
plt.ylabel("Number of Samples")
plt.title("Top 15 TP53 Amino-Acid Substitutions")

plt.xticks(rotation=45)
plt.tight_layout()

# Save figure
plt.savefig(
    "../figures/Top_15_TP53_Substitutions.png",
    dpi=300
)

plt.show()

print("Figure 8 created successfully.")