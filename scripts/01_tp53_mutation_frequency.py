import pandas as pd

# Load the TP53 mutation data
data = pd.read_csv("../data/TP53_mutations.tsv", sep="\t")

# Count total samples
total_samples = len(data)

# Count TP53 wild-type samples
wt_samples = (data["TP53"] == "WT").sum()

# Count TP53 mutated samples
mutated_samples = total_samples - wt_samples

# Calculate percentages
wt_percentage = (wt_samples / total_samples) * 100
mutated_percentage = (mutated_samples / total_samples) * 100

# Display the results
print("Total samples:", total_samples)
print("TP53 mutated samples:", mutated_samples)
print("TP53 WT samples:", wt_samples)
print("TP53 mutated percentage:", round(mutated_percentage, 2), "%")
print("TP53 WT percentage:", round(wt_percentage, 2), "%")