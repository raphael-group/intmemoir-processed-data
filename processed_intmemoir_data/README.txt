This directory contains the data files for the intMEMOIR dataset. Within each directory (named s*c*) there exists 4 files:

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