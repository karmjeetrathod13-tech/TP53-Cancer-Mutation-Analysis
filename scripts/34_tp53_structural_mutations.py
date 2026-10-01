import pandas as pd

# Selected recurrent TP53 mutations
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

# Create table
data = pd.DataFrame({
    "Mutation": mutations,
    "Position": [175, 179, 220, 248, 273, 273, 280, 282]
})

# Assign functional region
data["Functional_Region"] = "DNA-binding Domain"

# Save
data.to_csv(
    "../results/TP53_Selected_Structural_Mutations.csv",
    index=False
)

print("Selected TP53 Mutations for Structural Analysis")
print("-----------------------------------------------")
print(data.to_string(index=False))