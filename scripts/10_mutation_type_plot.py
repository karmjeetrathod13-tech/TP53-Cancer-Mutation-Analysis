import pandas as pd
import matplotlib.pyplot as plt

# Load complete mutation classification
data = pd.read_csv(
    "../results/TP53_complete_mutation_classification.csv"
)

# Count mutation types
type_counts = data["Mutation_Type"].value_counts()

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(type_counts.index, type_counts.values)

plt.title("Types of TP53 Mutations")
plt.xlabel("Mutation Type")
plt.ylabel("Number of Samples")

plt.xticks(rotation=25, ha="right")

# Add values
for i, value in enumerate(type_counts.values):
    plt.text(i, value + 3, str(value), ha="center")

# Save corrected figure
plt.savefig(
    "../figures/TP53_Mutation_Types.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()