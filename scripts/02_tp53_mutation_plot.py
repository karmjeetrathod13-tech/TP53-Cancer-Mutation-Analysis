import matplotlib.pyplot as plt

# TP53 mutation data
statuses = ["TP53 Mutated", "TP53 WT"]
counts = [328, 624]

# Create bar chart
plt.bar(statuses, counts)

# Add labels
plt.title("TP53 Mutation Status in Breast Cancer Samples")
plt.xlabel("TP53 Status")
plt.ylabel("Number of Samples")

# Add values above bars
for i, value in enumerate(counts):
    plt.text(i, value + 10, str(value), ha="center")

# Save the figure
plt.savefig("../figures/TP53_mutation_status.png", dpi=300, bbox_inches="tight")

# Display the plot
plt.show()