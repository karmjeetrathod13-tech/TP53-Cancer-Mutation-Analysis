import pandas as pd

# Load mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

genes = [
    "MDM2",
    "MDM4",
    "ATM",
    "CHEK2",
    "RPS6KA3"
]

# Select TP53-mutated samples
tp53_mutated = data[
    data["TP53"].astype(str).str.strip().str.upper() != "WT"
].copy()

results = []

total_tp53 = len(tp53_mutated)

for gene in genes:

    # Count mutations in the same TP53-mutated samples
    mutated = (
        tp53_mutated[gene].notna()
        & (tp53_mutated[gene].astype(str).str.strip().str.upper() != "WT")
    )

    count = mutated.sum()
    percentage = (count / total_tp53) * 100

    results.append({
        "Gene": gene,
        "TP53_Mutated_Samples": total_tp53,
        "CoMutated_Samples": count,
        "Percentage_of_TP53_Mutated": round(percentage, 2)
    })

result_df = pd.DataFrame(results)

# Save results
result_df.to_csv(
    "../results/TP53_Comutation_Analysis.csv",
    index=False
)

print("TP53 Co-Mutation Analysis")
print("-------------------------")
print(result_df.to_string(index=False))