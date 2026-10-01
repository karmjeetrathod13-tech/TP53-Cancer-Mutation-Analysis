import pandas as pd
import re

# Load mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Extract TP53 mutations
mutations = data["TP53"].dropna()

# Extract simple amino-acid substitutions
substitutions = []

for mutation in mutations:
    match = re.match(r"^([A-Z])(\d+)([A-Z*])$", str(mutation))
    
    if match:
        original = match.group(1)
        position = match.group(2)
        new = match.group(3)
        
        substitutions.append(
            f"{original}{position}{new}"
        )

# Count substitutions
substitution_counts = pd.Series(substitutions).value_counts()

# Save results
substitution_counts.to_csv(
    "../results/TP53_amino_acid_substitutions.csv",
    header=["Count"]
)

print("Top TP53 Amino-Acid Substitutions")
print("----------------------------------")
print(substitution_counts.head(15))