import pandas as pd
import re

# Load mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Keep only mutated samples
mutations = data[data["TP53"] != "WT"]["TP53"]

# Extract amino acid position from mutation names
positions = []

for mutation in mutations:
    match = re.search(r"[A-Z](\d+)", mutation)
    if match:
        positions.append(int(match.group(1)))

# Count mutations at each position
position_counts = pd.Series(positions).value_counts().sort_index()

# Save results
position_counts.to_csv(
    "../results/TP53_mutation_positions.csv",
    header=["Count"]
)

print("Total mutation positions:", len(position_counts))
print("\nMost frequently mutated positions:")
print(position_counts.sort_values(ascending=False).head(10))