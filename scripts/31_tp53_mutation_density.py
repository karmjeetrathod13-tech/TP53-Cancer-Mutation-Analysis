import pandas as pd

# Load mutation position data
data = pd.read_csv(
    "../results/TP53_mutation_positions.csv"
)

# Rename first column to Position
data = data.rename(
    columns={data.columns[0]: "Position"}
)

# Create 25-amino-acid windows
def get_window(position):
    start = ((position - 1) // 25) * 25 + 1
    end = min(start + 24, 393)
    return f"{start}-{end}"

# Assign each mutation position to a window
data["Window"] = data["Position"].apply(get_window)

# Calculate mutation counts
density = (
    data.groupby("Window")["Count"]
    .sum()
    .reset_index()
)

# Sort windows by starting position
density["Start"] = (
    density["Window"]
    .str.split("-")
    .str[0]
    .astype(int)
)

density = density.sort_values("Start")

# Remove helper column
density = density.drop(columns=["Start"])

# Save results
density.to_csv(
    "../results/TP53_25aa_Mutation_Density.csv",
    index=False
)

print("TP53 Mutation Density Across 25-aa Windows")
print("--------------------------------------------")
print(density.to_string(index=False))