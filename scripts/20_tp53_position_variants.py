import pandas as pd
import re

# Load mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

mutations = data["TP53"].dropna()

position_variants = {}

# Extract amino-acid position from mutations
for mutation in mutations:
    mutation = str(mutation)

    match = re.search(r"[A-Z](\d+)[A-Z*]", mutation)

    if match:
        position = int(match.group(1))

        if position not in position_variants:
            position_variants[position] = set()

        position_variants[position].add(mutation)

# Create result table
results = []

for position, variants in position_variants.items():
    results.append({
        "Position": position,
        "Number_of_Variants": len(variants),
        "Variants": ", ".join(sorted(variants))
    })

result_df = pd.DataFrame(results)

# Sort by number of variants
result_df = result_df.sort_values(
    "Number_of_Variants",
    ascending=False
)

# Save results
result_df.to_csv(
    "../results/TP53_position_variants.csv",
    index=False
)

print("TP53 Positions With Multiple Mutation Variants")
print("-----------------------------------------------")
print(result_df.head(15).to_string(index=False))