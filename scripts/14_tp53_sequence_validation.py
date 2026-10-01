import pandas as pd
import re

# Read TP53 protein sequence
with open("../data/TP53_protein.fasta", "r") as file:
    lines = file.readlines()

protein_sequence = "".join(
    line.strip()
    for line in lines
    if not line.startswith(">")
)

# Load original mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Keep mutated samples
mutations = data[data["TP53"] != "WT"]["TP53"]

results = []

for mutation in mutations:
    match = re.match(r"^([A-Z])(\d+)([A-Z*])", mutation)

    if match:
        original_aa = match.group(1)
        position = int(match.group(2))
        new_aa = match.group(3)

        if position <= len(protein_sequence):
            reference_aa = protein_sequence[position - 1]

            results.append({
                "Mutation": mutation,
                "Position": position,
                "Reported_Original": original_aa,
                "Reference_Amino_Acid": reference_aa,
                "New_Amino_Acid": new_aa,
                "Match": original_aa == reference_aa
            })

# Create result table
results_df = pd.DataFrame(results)

# Save results
results_df.to_csv(
    "../results/TP53_sequence_validation.csv",
    index=False
)

# Summary
print("TP53 Sequence Validation")
print("------------------------")
print("Mutations analyzed:", len(results_df))
print("Matching reference amino acid:",
      results_df["Match"].sum())
print("Non-matching:",
      (~results_df["Match"]).sum())

print("\nValidation completed.")