import pandas as pd

# Load mutation position data
data = pd.read_csv("../results/TP53_mutation_positions.csv")

# The first column contains the amino-acid position
data = data.rename(columns={data.columns[0]: "Position"})

# Classify positions
def classify_domain(position):
    if 102 <= position <= 292:
        return "DNA-binding Domain"
    else:
        return "Outside DNA-binding Domain"

data["Region"] = data["Position"].apply(classify_domain)

# Calculate total mutation counts
domain_counts = (
    data.groupby("Region")["Count"]
    .sum()
    .sort_values(ascending=False)
)

# Save results
domain_counts.to_csv(
    "../results/TP53_DNA_binding_domain_analysis.csv",
    header=["Mutation_Count"]
)

print("TP53 DNA-Binding Domain Analysis")
print("---------------------------------")
print(domain_counts)

total = domain_counts.sum()

print("\nPercentage Distribution:")
for region, count in domain_counts.items():
    percentage = (count / total) * 100
    print(f"{region}: {count} ({percentage:.2f}%)")