results_text = """
TP53 RESULTS AND INTERPRETATION
================================

1. TP53 Mutation Frequency
--------------------------
A total of 952 samples were analyzed. Among them, 328 samples
contained TP53 mutations, while 624 samples were classified as
wild type. Therefore, TP53 mutations were observed in 34.45% of
the analyzed samples.

Interpretation:
TP53 alterations were observed in a substantial proportion of
the analyzed breast cancer samples. This result is specific to
the selected dataset and should not be generalized to all cancers.

2. Mutation Diversity
---------------------
The analysis identified 191 distinct TP53 mutation variants
distributed across 126 protein positions.

Interpretation:
The presence of many distinct variants indicates considerable
variation in the types and positions of TP53 alterations within
the dataset.

3. Recurrent Mutation Sites
---------------------------
Position 273 was the most frequently mutated position, with
19 mutation entries. Other frequently affected positions
included 175, 220, 342, 193, 196, 248 and 179.

Interpretation:
The repeated occurrence of mutations at particular positions
suggests that some TP53 sites are recurrently altered in the
analyzed samples.

4. Mutation Types
-----------------
The complete mutation classification identified missense,
frameshift, nonsense, splice-site, deletion and
deletion-insertion events.

Interpretation:
The dataset contains multiple molecular types of TP53
alterations rather than a single mutation mechanism.

5. Protein Region Distribution
------------------------------
Using the defined TP53 protein regions, 287 of the 328 mutation
entries were located within the DNA-binding domain (102-292),
representing 87.50% of the mutation entries.

Interpretation:
The analyzed mutations were concentrated strongly within the
defined DNA-binding region. This observation is dataset-specific
and reflects the mutation positions present in this study.

6. Structural Mapping
---------------------
Eight recurrent TP53 mutations were selected for structural
analysis: R175H, H179R, Y220C, R248W, R273H, R273C, R280K
and R282W.

All selected positions were present in both chains of the
2XWR TP53 structure.

Interpretation:
Structural mapping demonstrates that several recurrent mutation
sites are located within the TP53 DNA-binding domain and can be
visualized directly on a three-dimensional protein structure.

7. Overall Interpretation
-------------------------
The analysis shows that TP53 mutations in the selected dataset
are diverse but are not uniformly distributed across the
protein. Several recurrent mutation positions occur within the
DNA-binding domain, and selected recurrent sites can be mapped
onto the three-dimensional TP53 structure.

These findings provide a computational overview of TP53 mutation
patterns in the analyzed dataset. The results describe
associations within the dataset and do not by themselves
establish that individual mutations cause cancer or directly
produce specific structural or functional effects.
"""

output_file = "../results/TP53_Results_Interpretation.txt"

with open(output_file, "w") as file:
    file.write(results_text.strip())

print(results_text)
print(f"\nSaved to: {output_file}")