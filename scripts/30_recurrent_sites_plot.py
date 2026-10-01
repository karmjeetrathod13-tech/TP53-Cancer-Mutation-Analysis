import pandas as pd
import matplotlib.pyplot as plt

# Load recurrent mutation sites
data = pd.read_csv(
    "../results/TP53_Recurrent_Mutation_Sites.csv"
)

# Select top 15 sites
data = data.head(15)

# Plot
plt.figure(figsize=(10, 6))

plt.bar(
    data["Position"].astype(str),
    data["Count"]
)

plt.xlabel("TP53 Amino-Acid Position")
plt.ylabel("Number of Mutated Samples")
plt.title("Top 15 Recurrent TP53 Mutation Sites")

plt.tight_layout()

# Save figure
plt.savefig(
    "../figures/Top_15_TP53_Recurrent_Sites.png",
    dpi=300
)

plt.show()

print("Figure 13 created successfully.")