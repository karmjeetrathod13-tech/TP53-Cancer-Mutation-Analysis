import pandas as pd

# Read TP53 protein FASTA
with open("../data/TP53_protein.fasta", "r") as file:
    lines = file.readlines()

# Remove FASTA header and join sequence
protein_sequence = "".join(
    line.strip()
    for line in lines
    if not line.startswith(">")
)

# Get protein length
protein_length = len(protein_sequence)

print("TP53 protein length:", protein_length)

# Load mutation positions from RESULTS folder
data = pd.read_csv("../results/TP53_mutation_positions.csv")

# Check whether each mutation position is within the protein
data["Within_Protein"] = data.index.map(
    lambda position: position <= protein_length
)

# Save mapping results
data.to_csv(
    "../results/TP53_protein_position_mapping.csv",
    index=False
)

print("Total mutation positions:", len(data))
print(
    "Positions within TP53 protein:",
    data["Within_Protein"].sum()
)
print(
    "Positions outside TP53 protein:",
    (~data["Within_Protein"]).sum()
)

print("\nProtein mapping analysis completed.")