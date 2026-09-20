# Results

CSV versions of the chapter tables. See [docs/case_study.md](../docs/case_study.md) for context and metric definitions.

| File | Chapter table |
|---|---|
| `table1_datasets.csv` | Table 1. Composition of the multimodal hurricane damage datasets |
| `table2_image_restoration.csv` | Table 2. Composite quality score Q before/after each restoration branch |
| `table3_severity_accuracy_ncse.csv` | Table 3. Severity-classification accuracy and Normalized Cross-Severity Error (NCSE) |
| `table4_indicator_recognition_overall.csv` | Table 4. Overall F1 / recall / precision / accuracy on five damage indicators |
| `table5_indicator_recognition_per_class.csv` | Table 5. Per-indicator recognition performance |

Q = 0.4·C + 0.4·S + 0.2·N (normalized contrast, sharpness, NIQE-proxy).
NCSE = (1/N) Σ |y_i − ŷ_i| / (K − 1), with K = 3 ordered severity levels.
