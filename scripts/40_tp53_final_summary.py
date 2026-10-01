import pandas as pd

summary = {
    "Total_samples": 952,
    "TP53_mutated_samples": 328,
    "TP53_WT_samples": 624,
    "TP53_mutation_percentage": 34.45,
    "Distinct_TP53_variants": 191,
    "Mutation_positions": 126,
    "DNA_binding_domain_mutation_count": 287,
    "DNA_binding_domain_percentage": 87.50,
    "Most_recurrent_position": 273,
    "Most_recurrent_position_count": 19,
    "Most_frequent_mutation": "R175H",
    "Most_frequent_mutation_count": 18,
    "Structural_PDB": "2XWR",
    "Selected_structural_mutations": 8
}

df = pd.DataFrame(
    list(summary.items()),
    columns=["Parameter", "Value"]
)

output_file = "../results/TP53_Final_Results_Summary.csv"

df.to_csv(output_file, index=False)

print("TP53 Final Results Summary")
print("--------------------------")
print(df.to_string(index=False))

print(f"\nSaved to: {output_file}")