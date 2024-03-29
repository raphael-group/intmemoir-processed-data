This directory contains the data files for the intMEMOIR dataset where sequence information is simulated (see below) along with the location data (according to a Gaussian distriution) and tree topologies belongs to the true intMEMOIR data. Within each directory (named s*c*) there exists the following types of files

(1) k*_priors.csv (*=10,50,200)
(2) k*_character_matric.csv  (*=10,50,200)
(3) sim_leaf_sigma_*.txt (*=0.5, 1.5, 3)
(4) sim_location_sigma_*.txt
(5) true_tree.nwk

(1) The file contains an example of a prior file that can be provided to our model for the Q matrix (see PMM paper). Note this file is not required if one assumes a uniform distribution for this prior. Each site and each mutated state should have a row in this matrix, structured as:

site_number, state, probability 

(2) The first row is a header describing the contents of the subsequent matrix. The first column of the matrix is the name of a cell (in this case, 216_* refers to the fact that the leaves of the tree correspond to the 216th time sample of the video frame data from the intMEMOIR experiment). The remaining columns correspond to a given mutation site across the cells. In other words, for a given row of this matrix, the first entry is the name of the cell, the remaining 10 entries correspond to state the 10 mutation sites. The value after the "k" (i.e 50 for k50_character_matrix) refers to the number of sites we simulate. In the aforementioned case we simulated 50 sites according to our model. 

(3) This file contains the X-Y coordinates for each of the cells at the leaves of the tree. These should correspond to the cells in the character matrix in (1). Each line of this file should be of the form:

cell_name, x_coordinate, y_coordinate

A file exists for each value of sigma assumming a Brownian motion model for spatial evolution for each coordinate independently. For a file sim_leaf_sigma_*locations.txt, the value at * (for example 1.5) referes to leaf locations of a simulated tree with sigma=1.5

(4) This file contains the X-Y coordinate for each of the cells in the entire tree (not just the leaves). The form of this file should be the same as in the file describing the locations for the leaves of the tree (file (2)). The naming convention of the * value is the same as the one for the leaf locations. 

(5) This file contains the true tree topology for this experiment, in newick format.

Furthermore, we also include our own outputs of the results (see k*_problin.txt and k*_sigma*_spalin.txt) for the sequence only and sequence + spatial results, respectively. 

