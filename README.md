# In-Silico Analysis of Somatic Mutations in the Human TP53 Gene

## Overview

This project presents a computational analysis of somatic mutations in the human **TP53 (Tumor Protein p53)** gene using publicly available cancer genomic data.

The study focuses on identifying mutation frequencies, mutation types, recurrent mutation positions, protein-region distribution, co-mutation patterns, mutation density and structural locations of selected TP53 mutations.

The analysis was performed using Python and publicly available biological databases and structural resources.

---

## Research Question

What are the major types and distributions of somatic mutations reported in the human TP53 gene, and which regions of the encoded protein are frequently affected?

---

## Objectives

- Determine the frequency of TP53 mutations in the selected dataset.
- Identify different TP53 mutation types and variants.
- Analyze the distribution of mutations across the TP53 protein.
- Identify recurrent mutation positions and hotspots.
- Examine mutation distribution across defined functional regions.
- Analyze TP53 co-mutation patterns with selected related genes.
- Map selected recurrent mutations onto a 3D TP53 structure.
- Interpret the observed mutation patterns computationally.

---

## Dataset

The mutation dataset was obtained from **cBioPortal for Cancer Genomics**.

**Study:** TCGA Breast Invasive Carcinoma (BRCA)

**Dataset:** `brca_tcga_gdc`

**Total samples analyzed:** 952

### TP53 Mutation Status

| Status | Samples | Percentage |
|---|---:|---:|
| TP53 mutated | 328 | 34.45% |
| TP53 wild type | 624 | 65.55% |

---

## Reference Information

| Resource | Identifier |
|---|---|
| NCBI TP53 mRNA | NM_000546.6 |
| NCBI TP53 protein | NP_000537.3 |
| UniProt TP53 | P04637 |
| Structural model | PDB: 2XWR |

---

# Analysis Workflow

```text
Cancer Mutation Dataset
          ↓
TP53 Mutation Filtering
          ↓
Mutation Frequency Analysis
          ↓
Mutation Type Classification
          ↓
Mutation Position Analysis
          ↓
Hotspot Identification
          ↓
Protein Region Analysis
          ↓
Co-mutation Analysis
          ↓
Mutation Density Analysis
          ↓
Structural Mapping
          ↓
3D Visualization
          ↓
Biological Interpretation