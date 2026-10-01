import pandas as pd

# Load mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Remove WT samples
mutations = data[data["TP53"] != "WT"]["TP53"]

# Count each mutation
mutation_counts = mutations.value_counts()

# Save complete results
mutation_counts.to_csv("../results/TP53_mutation_types.csv", header=["Count"])

# Display results
print("Total distinct TP53 mutations:", len(mutation_counts))
print("\nTop 10 TP53 mutations:")
print(mutation_counts.head(10))