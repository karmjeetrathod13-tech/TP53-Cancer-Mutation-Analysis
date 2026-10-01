import pandas as pd
import matplotlib.pyplot as plt

# Load hotspot-region data
data = pd.read_csv(
    "../results/TP53_Hotspots_Functional_Regions.csv"
)

# Sort by hotspot positions
data = data.sort_values(
    "Hotspot_Positions",
    ascending=False
)

# Plot
plt.figure(figsize=(10, 6))

plt.bar(
    data["Functional_Region"],
    data["Hotspot_Positions"]
)

plt.xlabel("TP53 Functional Region")
plt.ylabel("Number of Hotspot Positions")
plt.title("TP53 Mutation Hotspots Across Functional Regions")

plt.xticks(rotation=25)
plt.tight_layout()

# Save figure
plt.savefig(
    "../figures/TP53_Hotspots_Functional_Regions.png",
    dpi=300
)

plt.show()

print("Figure 12 created successfully.")