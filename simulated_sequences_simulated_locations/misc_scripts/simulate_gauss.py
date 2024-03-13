#! /usr/bin/env python

from treeswift import *
from sys import argv
import random
from math import *

tree = read_tree_newick(argv[1])
sigma = float(argv[2])

for node in tree.traverse_preorder(): 
    if node.is_root():
        node.x = 0
        node.y = 0
    else:
        x_par = node.parent.x
        y_par = node.parent.y
        node.x = random.gauss(mu=x_par, sigma=sigma*sqrt(node.edge_length))
        node.y = random.gauss(mu=y_par, sigma=sigma*sqrt(node.edge_length))

with open(argv[3],'w') as fout:
    for node in tree.traverse_preorder():
        fout.write(node.label + " " + str(node.x) + " " + str(node.y) + "\n")        

with open(argv[4],'w') as fout:
    for node in tree.traverse_leaves():
        fout.write(node.label + " " + str(node.x) + " " + str(node.y) + "\n")        
