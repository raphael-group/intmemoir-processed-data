# Processed and Simulated intMEMOIR data

This repository holds intMEMOIR data that was used for the recent ISMB submission "Maximum Likelihood Phylogeographic Inference of Cell Motility and Cell Division from Spatial Lineage Tracing Data"

There are 3 setups that were used in this paper:

- Fully simulated data (simulated sequences and simulated locations) (the raw data can be downloaded from the original authors, but we also store data files we used within a .zip in this directory as well).
- Semi-Synthetic data (simulated sequences, but using real locations)
- Real data (sequences and locations both come from real intMEMOIR experiments)

These each correspond to one of the three directories in this repository. Each directory contains a README.txt that describes in more detail the structure of each of the files in that directory. As a quick primer, the main important files across all settings (fully simulated, semi-synthetic, real data)

### Character matrix file:
The first row is a header describing the contents of the subsequent matrix. The first column of the matrix is the name of a cell (in this case, 216_* refers to the fact that the leaves of the tree correspond to the 216th time sample of the video frame data from the intMEMOIR experiment). The remaining columns correspond to a given mutation site across the cells. In other words, for a given row of this matrix, the first entry is the name of the cell, the remaining 10 entries correspond to state the 10 mutation sites. For example:

| cell  | s1 | s2 | s3 |
| ------------- | ------------- | ------------- | ------------- |
| cell_1  | 2  | 0  | 1  |
| cell_2  | 2  | 2  | 1  |
| cell_3  | 1 | 2  | 0  |

### Location file(s):
Each line in this .txt file is corresponds to a cell, followed by its x and y coordinates, for example
```
cell_1,3.3,4.5
cell_2,5.3,2.1
cell_3,1.0,3.2
```

### Tree .nwk file
A .nwk file containing the true tree.

Instructions on how to use the above files to run our method (as well as code for our method itself) is in the repository: https://github.com/raphael-group/Spatial-Division/
