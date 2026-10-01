import pandas as pd

# Load mutation position frequencies
position_data = pd.read_csv(
    "../results/TP53_mutation_positions.csv"
)

# Rename first column to Position
position_data = position_data.rename(
    columns={position_data.columns[0]: "Position"}
)

# Load number of variants at each position
variant_data = pd.read_csv(
    "../results/TP53_position_variants.csv"
)

# Merge datasets
data = pd.merge(
    position_data,
    variant_data[["Position", "Number_of_Variants", "Variants"]],
    on="Position",
    how="left"
)

# Assign functional regions
def get_functional_region(position):

    if 1 <= position <= 61:
        return "Transactivation Domain"

    elif 64 <= position <= 92:
        return "Proline-rich Region"

    elif 102 <= position <= 292:
        return "DNA-binding Domain"

    elif 325 <= position <= 356:
        return "Tetramerization Domain"

    elif 363 <= position <= 393:
        return "Regulatory Region"

    else:
        return "Other/Unannotated"

data["Functional_Region"] = data["Position"].apply(
    get_functional_region
)

# Sort by mutation frequency
data = data.sort_values(
    "Count",
    ascending=False
)

# Select top 20 recurrent sites
top_sites = data.head(20)

# Save result
top_sites.to_csv(
    "../results/TP53_Recurrent_Mutation_Sites.csv",
    index=False
)

print("Top 20 Recurrent TP53 Mutation Sites")
print("-------------------------------------")

print(
    top_sites[
        [
            "Position",
            "Count",
            "Number_of_Variants",
            "Functional_Region",
            "Variants"
        ]
    ].to_string(index=False)
)