pdb_file = "../data/2XWR.pdb"

target_positions = [175, 179, 220, 248, 273, 280, 282]

residues = {}

with open(pdb_file, "r") as file:
    for line in file:
        if line.startswith("ATOM"):
            parts = line.split()

            try:
                res_name = parts[5]
                chain = parts[6]
                res_num = int(parts[16])
            except (IndexError, ValueError):
                continue

            if res_num in target_positions:
                residues[(chain, res_num)] = res_name

print("TP53 PDB Residue Check")
print("-----------------------")

for position in target_positions:
    found = [
        (chain, name)
        for (chain, pos), name in residues.items()
        if pos == position
    ]

    if found:
        print(f"{position}: FOUND -> {found}")
    else:
        print(f"{position}: NOT FOUND")

print("\nCheck complete.")