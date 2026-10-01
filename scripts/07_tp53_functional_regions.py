import pandas as pd

# Known functional regions of human TP53 protein
regions = {
    "Transactivation domain": (1, 61),
    "Proline-rich region": (64, 92),
    "DNA-binding domain": (102, 292),
    "Tetramerization domain": (325, 356),
    "Regulatory domain": (363, 393)
}

# Load mutation positions
data = pd.read_csv("../results/TP53_mutation_positions.csv")

# Check which region each position belongs to
results = []

for position, count in data["Count"].items():
    region_name = "Outside defined regions"

    for region, (start, end) in regions.items():
        if start <= position <= end:
            region_name = region
            break

    results.append({
        "Position": position,
        "Mutation_Count": count,
        "Functional_Region": region_name
    })

# Create result table
results_df = pd.DataFrame(results)

# Save results
results_df.to_csv(
    "../results/TP53_mutations_functional_regions.csv",
    index=False
)

# Count mutations by functional region
region_counts = results_df.groupby(
    "Functional_Region"
)["Mutation_Count"].sum().sort_values(ascending=False)

print("TP53 Mutations by Functional Region")
print("-----------------------------------")
print(region_counts)