#! /usr/bin/env python

from treeswift import *
from sys import argv
import random
from math import *

sep_vec_file = "separation_vectors.txt"

tree = read_tree_newick(argv[1])
sampleID = argv[2]
sep_intense = float(argv[3])
sigma = float(argv[4])

sep_vecs = {}
with open(sep_vec_file,'r') as fin:
    for line in fin:
        sID,cellID,sep_x,sep_y = line.strip().split()
        if sID == sampleID:
            frameID,_ = cellID.split('_')
            sep_vecs[int(frameID)-1] = (sep_intense*float(sep_x),sep_intense*float(sep_y))
for node in tree.traverse_preorder():
    if not node.is_leaf():
        if node.label == "virtual":
            node.children[0].sep_vec  = node.children[1].sep_vec = (0,0)       
        else:
            frameID,_ = node.label.split('_')
            sep_x,sep_y = sep_vecs[int(frameID)]
            node.children[0].sep_vec = (sep_x,sep_y)
            node.children[1].sep_vec = (-sep_x,-sep_y)

for node in tree.traverse_preorder(): 
    if node.is_root():
        node.x = 0
        node.y = 0
    else:
        x_par = node.parent.x
        y_par = node.parent.y
        sep_x,sep_y = node.sep_vec
        node.x = x_par + sep_x + random.gauss(mu=0,sigma=sigma*sqrt(node.edge_length))
        node.y = y_par + sep_y + random.gauss(mu=0,sigma=sigma*sqrt(node.edge_length))

with open(argv[5],'w') as fout:
    for node in tree.traverse_preorder():
        fout.write(node.label + "," + str(node.x) + "," + str(node.y) + "\n")        

with open(argv[6],'w') as fout:
    for node in tree.traverse_leaves():
        fout.write(node.label + "," + str(node.x) + "," + str(node.y) + "\n")        

with open(argv[7],'w') as fout:
    for node in tree.traverse_preorder():
        if not node.is_root():
            x,y = node.sep_vec
            fout.write(node.label + "," + str(x) + "," + str(y) + "\n")        
