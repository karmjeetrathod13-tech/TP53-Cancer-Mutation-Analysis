from Bio.PDB import MMCIFParser

cif_file = "../data/2XWR.pdb"

parser = MMCIFParser(QUIET=True)
structure = parser.get_structure("TP53", cif_file)

target_positions = [175, 179, 220, 248, 273, 280, 282]

print("TP53 Structure Information")
print("--------------------------")

for model in structure:
    print(f"Model: {model.id}")

    for chain in model:
        print(f"Chain: {chain.id}")

        for position in target_positions:
            if position in chain:
                residue = chain[position]
                print(f"  Position {position}: {residue.resname}")

    print()