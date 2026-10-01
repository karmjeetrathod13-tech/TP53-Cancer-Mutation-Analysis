import pandas as pd
import re

# Load mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Keep mutated samples
mutations = data[data["TP53"] != "WT"]["TP53"]

# Classify every mutation
results = []

for mutation in mutations:

    if "_splice" in mutation:
        mutation_type = "Splice-site"

    elif "delins" in mutation:
        mutation_type = "Deletion-insertion"

    elif "del" in mutation.lower():
        mutation_type = "Deletion"

    elif "ins" in mutation.lower():
        mutation_type = "Insertion"

    elif "fs" in mutation:
        mutation_type = "Frameshift"

    elif "*" in mutation:
        mutation_type = "Nonsense"

    elif re.match(r"^[A-Z]\d+[A-Z]$", mutation):
        mutation_type = "Missense"

    else:
        mutation_type = "Other"

    results.append({
        "Mutation": mutation,
        "Mutation_Type": mutation_type
    })

# Create table
results_df = pd.DataFrame(results)

# Count mutation types
type_counts = results_df["Mutation_Type"].value_counts()

# Save complete classification
results_df.to_csv(
    "../results/TP53_complete_mutation_classification.csv",
    index=False
)

print("Complete TP53 Mutation Classification")
print("-------------------------------------")
print(type_counts)

print("\nTotal mutation entries:", len(results_df))