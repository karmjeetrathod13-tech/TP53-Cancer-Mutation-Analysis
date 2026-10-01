import pandas as pd

# Load mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

genes = [
    "TP53",
    "MDM2",
    "MDM4",
    "ATM",
    "CHEK2",
    "RPS6KA3"
]

results = []

total_samples = len(data)

for gene in genes:

    # WT = not mutated
    mutated = (
        data[gene].notna()
        & (data[gene].astype(str).str.strip().str.upper() != "WT")
    )

    mutation_count = mutated.sum()
    percentage = (mutation_count / total_samples) * 100

    results.append({
        "Gene": gene,
        "Mutated_Samples": mutation_count,
        "Total_Samples": total_samples,
        "Mutation_Percentage": round(percentage, 2)
    })

result_df = pd.DataFrame(results)

# Save results
result_df.to_csv(
    "../results/Gene_Mutation_Frequency.csv",
    index=False
)

print("Gene Mutation Frequency")
print("-----------------------")
print(result_df.to_string(index=False))