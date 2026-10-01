import pandas as pd

# Load mutation density data
data = pd.read_csv(
    "../results/TP53_25aa_Mutation_Density.csv"
)

# Calculate total mutations
total_mutations = data["Count"].sum()

# Calculate percentage contribution
data["Percentage"] = (
    data["Count"] / total_mutations * 100
).round(2)

# Sort by mutation count
data = data.sort_values(
    "Count",
    ascending=False
)

# Save results
data.to_csv(
    "../results/TP53_Mutation_Density_Summary.csv",
    index=False
)

print("TP53 High-Density Mutation Regions")
print("----------------------------------")

print(
    data[
        ["Window", "Count", "Percentage"]
    ].to_string(index=False)
)

print("\nTotal mutation count:", total_mutations)