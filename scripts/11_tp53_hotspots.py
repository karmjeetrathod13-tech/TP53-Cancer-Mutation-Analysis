import pandas as pd
import re

# Load TP53 mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Keep mutated samples
mutations = data[data["TP53"] != "WT"]["TP53"]

# Extract amino-acid positions
position_data = []

for mutation in mutations:
    match = re.search(r"[A-Z](\d+)", mutation)

    if match:
        position = int(match.group(1))
        position_data.append({
            "Mutation": mutation,
            "Position": position
        })

position_df = pd.DataFrame(position_data)

# Count different mutation variants at each position
hotspots = (
    position_df.groupby("Position")["Mutation"]
    .nunique()
    .sort_values(ascending=False)
)

# Save results
hotspots.to_csv(
    "../results/TP53_mutation_hotspots.csv",
    header=["Unique_Mutation_Variants"]
)

print("TP53 Mutation Hotspots")
print("----------------------")
print(hotspots.head(15))