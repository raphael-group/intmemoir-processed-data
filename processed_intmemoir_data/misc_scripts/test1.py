#! /usr/bin/env python

from problin_libs.sequence_lib import read_sequences
from problin_libs.ML_solver import ML_solver
from problin_libs.EM_solver import EM_solver
from problin_libs.SpaLin_solver import SpaLin_solver
from sys import argv
from treeswift import *
import os

k = 10
m = 3
Q = []

for i in range(k):
    q = {j+1:1/m for j in range(m)}
    q[0] = 0
    Q.append(q)

data = "s20c2" 
print("dataset",data)
msa,_ = read_sequences(data+"/characters.txt",filetype="charMtrx")
with open(data+"/true_tree.nwk",'r') as f:
    T = f.read().strip()

leaf_locations = {}
with open(data+"/leaf_locations.txt",'r') as fin:
    for line in fin:
        cellID,x,y = line.strip().split(",")
        leaf_locations[cellID] = (float(x),float(y))

#print("Optimization without using locations")
D = {'charMtrx':msa}
prior = {'Q':Q}
params = {'nu':1e-8,'phi':1e-8}
mySolver = ML_solver(T,D,prior,params)
mySolver.optimize(initials=20,fixed_nu=1e-8,fixed_phi=1e-8,verbose=False,ultra_constr=True)
mySolver.tree.write_tree_newick(data+"/without_location.nwk")

print("Optimization using locations")
sigma = 22.470982031241125 # pre-estimated from data
params['sigma'] = sigma
D['locations'] = leaf_locations 
#mySolver = SpaLin_solver(msa,Q,T,leaf_locations,sigma)
mySolver = SpaLin_solver(T,D,prior,params)
mySolver.optimize(initials=20,fixed_nu=1e-8,fixed_phi=1e-8,verbose=True)
mySolver.tree.write_tree_newick(data+"/with_location.nwk")
with open(data+"/with_location.log",'w') as fout:    
    fout.write("sigma: " + str(mySolver.params.sigma) + "\n")
    for cell in mySolver.inferred_locations:
        x,y = mySolver.inferred_locations[cell]
        fout.write(cell + " " + str(x) + " " + str(y) + "\n")
