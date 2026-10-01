import pandas as pd

# Load mutation position data
data = pd.read_csv("../results/TP53_mutation_positions.csv")

# The position is stored as the first column
data = data.rename(columns={data.columns[0]: "Position"})

# Create 50-amino-acid regions
def get_region(position):
    start = ((position - 1) // 50) * 50 + 1
    end = min(start + 49, 393)
    return f"{start}-{end}"

# Assign each position to a protein region
data["Protein_Region"] = data["Position"].apply(get_region)

# Count mutations in each region
region_counts = (
    data.groupby("Protein_Region")["Count"]
    .sum()
)

# Save results
region_counts.to_csv(
    "../results/TP53_region_distribution.csv",
    header=["Mutation_Count"]
)

print("TP53 Mutation Distribution Across Protein")
print("-----------------------------------------")
print(region_counts)