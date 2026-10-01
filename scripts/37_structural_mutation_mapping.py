import pandas as pd

# Selected TP53 mutations
mutations = [
    "R175H",
    "H179R",
    "Y220C",
    "R248W",
    "R273H",
    "R273C",
    "R280K",
    "R282W"
]

# Mutation frequency from our analysis
frequency = {
    "R175H": 18,
    "H179R": 6,
    "Y220C": 7,
    "R248W": 5,
    "R273H": 11,
    "R273C": 4,
    "R280K": 1,
    "R282W": 4
}

# Functional region
def get_region(position):
    if 102 <= position <= 292:
        return "DNA-binding Domain"
    elif 64 <= position <= 92:
        return "Proline-rich Region"
    elif 1 <= position <= 61:
        return "Transactivation Domain"
    elif 325 <= position <= 356:
        return "Tetramerization Domain"
    else:
        return "Other"

rows = []

for mutation in mutations:
    position = int(mutation[1:-1])

    rows.append({
        "Mutation": mutation,
        "Position": position,
        "Frequency": frequency[mutation],
        "Functional_Region": get_region(position),
        "Present_in_2XWR": "Yes",
        "Chains": "A, B"
    })

df = pd.DataFrame(rows)

output_file = "../results/TP53_Structural_Mutation_Mapping.csv"
df.to_csv(output_file, index=False)

print("TP53 Structural Mutation Mapping")
print("---------------------------------")
print(df.to_string(index=False))

print(f"\nSaved to: {output_file}")