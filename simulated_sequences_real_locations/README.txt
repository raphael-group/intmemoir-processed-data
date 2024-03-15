This directory contains the data files for the intMEMOIR dataset where sequence information is simulated (see below), but the location information and tree topologies belongs to the true intMEMOIR data. Within each directory (named s*c*) there exists the following types of files

(1) k10_priors.csv
(2) k10_r*_character_matric.csv (*=1,2,3,4,5)
(3) leaf_locations.txt
(4) true_locations.txt
(5) true_tree.nwk

(1) The file contains an example of a prior file that can be provided to our model for the Q matrix (see PMM paper). Note this file is not required if one assumes a uniform distribution for this prior. Each site and each mutated state should have a row in this matrix, structured as:

site_number, state, probability 

(2) The first row is a header describing the contents of the subsequent matrix. The first column of the matrix is the name of a cell (in this case, 216_* refers to the fact that the leaves of the tree correspond to the 216th time sample of the video frame data from the intMEMOIR experiment). The remaining columns correspond to a given mutation site across the cells. In other words, for a given row of this matrix, the first entry is the name of the cell, the remaining 10 entries correspond to state the 10 mutation sites. 

(3) This file contains the X-Y coordinates for each of the cells at the leaves of the tree. These should correspond to the cells in the character matrix in (1). Each line of this file should be of the form:

cell_name, x_coordinate, y_coordinate

(4) This file contains the X-Y coordinate for each of the cells in the entire tree (not just the leaves). The form of this file should be the same as in the file describing the locations for the leaves of the tree (file (2)). 

(5) This file contains the true tree topology for this experiment, in newick format.

Furthermore, inside the results directory we also have an identical directory structure (a directory for each tree named s*c*). Inside each of these subdirectories we have the following files: (1) k10_r#_problin.txt (2) k10_r#_spalin.txt, (3) k10_r#_spalin-divide-beta*.txt, (4) k10_r#_spalin_spatialonly.txt, (5) k10_r#_spalin-divide-beta5_spatialonly.txt. We describe each of these files below:

(1) Contains the results of the sequence-only model for the data belonging to that directory. 
(2) Contains the results of the sequence+location model assumming brownian motion (no symmetric displacement).
(3) A set of files corresponding to the sequence+location model results for different radius amounts (value specified by * value). 
(4) The results of the location model only assuming Brownian motion.
(5) The results of the location only model assuming symmetric diplacement with radius=5.

For every results file, the # indicates the replicate number (there should be 5 replicates for each directory).

For every results file (the .txt files), there is an identical log file with the same name but with the .log extension.

More details ---

A semi-simulated data. True trees and locations are obtained from intMemoir; only use trees that have 10 or more leaves (70/106 of the intMemoir data)
Sequences are simulated using Problin
* Number of sites (k): 10
* Alphabet for each site: [1,2]
* Mutation rate: 0.006 (expected number of mutations per time frame; estimated from the LT data of intMemoir)
* No missing data (phi = nu = 0)
* Number of replicates: 5 for each tree
