import pandas as pd
import re

# Load TP53 mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Keep mutated samples
mutations = data[data["TP53"] != "WT"]["TP53"]


def classify_mutation(mutation):
    if "fs" in mutation:
        return "Frameshift"
    elif "*" in mutation:
        return "Nonsense"
    elif "del" in mutation.lower():
        return "Deletion"
    elif "ins" in mutation.lower():
        return "Insertion"
    elif re.match(r"^[A-Z]\d+[A-Z]$", mutation):
        return "Missense"
    else:
        return "Other"


# Classify mutations
mutation_types = mutations.apply(classify_mutation)

# Count mutation types
type_counts = mutation_types.value_counts()

# Save results
type_counts.to_csv(
    "../results/TP53_mutation_type_classification.csv",
    header=["Count"]
)

print("TP53 Mutation Type Classification")
print("---------------------------------")
print(type_counts)