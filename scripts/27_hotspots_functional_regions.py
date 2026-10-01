import pandas as pd

# Load mutation hotspot data
hotspots = pd.read_csv(
    "../results/TP53_position_variants.csv"
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

# Apply classification
hotspots["Functional_Region"] = hotspots["Position"].apply(
    get_functional_region
)

# Count hotspot positions in each region
region_summary = (
    hotspots.groupby("Functional_Region")
    .agg(
        Hotspot_Positions=("Position", "count"),
        Total_Variants=("Number_of_Variants", "sum")
    )
    .sort_values(
        "Hotspot_Positions",
        ascending=False
    )
)

# Save result
region_summary.to_csv(
    "../results/TP53_Hotspots_Functional_Regions.csv"
)

print("TP53 Hotspots by Functional Region")
print("-----------------------------------")
print(region_summary)