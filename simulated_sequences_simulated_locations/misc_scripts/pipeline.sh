#! /bin/bash

bash copy_data.sh
# simulate Brownian motion only 
for x in s*; do
   echo $x
    python ~/my_gits/problin/simulate_sequence.py -k 10 --alphabetsize 2 -t $x/true_tree.nwk -r 1 --mu 0.006 -p $x/k10
    python ~/my_gits/problin/simulate_sequence.py -k 50 --alphabetsize 2 -t $x/true_tree.nwk -r 1 --mu 0.006 -p $x/k50
    python ~/my_gits/problin/simulate_sequence.py -k 200 --alphabetsize 2 -t $x/true_tree.nwk -r 1 --mu 0.006 -p $x/k200
    for sigma in 0.5 1.5 3; do
        echo $x $sigma
        python simulate_gauss.py $x/true_tree.nwk $sigma $x/sim_location_sigma_$sigma\.txt $x/sim_leaf_sigma_$sigma\.txt
    done    
done    

# estimate separation force from data
bash get_sep_vector.sh

# simulate Brownian motion with separation force
sigma=1.5
for x in s*; do
    echo $x
    for sep_intense in 0.5 1 2; do
        python simulate_cellDiv.py $x/true_tree.nwk $x $sep_intense $sigma $x/sim_location_sep_$sep_intense\.txt $x/sim_leaf_sep_$sep_intense\.txt $x/sep_vec_sep_$sep_intense\.txt
    done    
done    
