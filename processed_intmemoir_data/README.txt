This directory contains the data files for the intMEMOIR dataset. Within each data directory (named s*c*) there exists 4 files:

(1) characters.txt
(2) leaf_locations.txt
(3) true_locations.txt
(4) true_tree.nwk

We describe each of the above in more detail.

(1) The first row is a header describing the contents of the subsequent matrix. The first column of the matrix is the name of a cell (in this case, 216_* refers to the fact that the leaves of the tree correspond to the 216th time sample of the video frame data from the intMEMOIR experiment). The remaining columns correspond to a given mutation site across the cells. In other words, for a given row of this matrix, the first entry is the name of the cell, the remaining 10 entries correspond to state the 10 mutation sites. 

(2) This file contains the X-Y coordinates for each of the cells at the leaves of the tree. These should correspond to the cells in the character matrix in (1). Each line of this file should be of the form:

cell_name, x_coordinate, y_coordinate

(3) This file contains the X-Y coordinate for each of the cells in the entire tree (not just the leaves). The form of this file should be the same as in the file describing the locations for the leaves of the tree (file (2)). 

(4) This file contains the true tree topology for this experiment, in newick format.

We store some of the files for the raw intMEMOIR files in a zip file in this directory. The original authors of intMEMOIR include a complete version of their raw data, and we refer those interested to download those files directly from them. 

Furthermore, inside the results directory we also have an identical directory structure (a directory for each tree named s*c*). Inside each of these subdirectories we have the following files: (1) problin.txt (2) spalin.txt, (3) spalin-divide-beta*.txt, (4) spalin_spatialonly.txt, (5) spalin-divide-beta5_spatialonly.txt. We describe each of these files below:

(1) Contains the results of the sequence-only model for the data belonging to that directory. 
(2) Contains the results of the sequence+location model assumming brownian motion (no symmetric displacement).
(3) A set of files corresponding to the sequence+location model results for different radius amounts (value specified by * value). 
(4) The results of the location model only assuming Brownian motion.
(5) The results of the location only model assuming symmetric diplacement with radius=5.

For every results file (the .txt files), there is an identical log file with the same name but with the .log extension.

Compiled results are stored in intmem_sigma_results.csv (for sigma estimates), and intmem_brlen_results.csv (for branch length estimates)
