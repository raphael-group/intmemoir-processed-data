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



More details ---

A semi-simulated data. True trees and locations are obtained from intMemoir; only use trees that have 10 or more leaves (70/106 of the intMemoir data)
Sequences are simulated using Problin
* Number of sites (k): 10
* Alphabet for each site: [1,2]
* Mutation rate: 0.006 (expected number of mutations per time frame; estimated from the LT data of intMemoir)
* No missing data (phi = nu = 0)
* Number of replicates: 5 for each tree
