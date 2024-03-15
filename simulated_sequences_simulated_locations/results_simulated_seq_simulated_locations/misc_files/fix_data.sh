


#! /bin/bash



for x in s*; do
	echo $x
    sed -r 's/ +/,/g' $x/sim_leaf_sigma_0.5.txt > $x/sim_leaf_sigma_0.5_fixed.txt 
    rm $x/sim_leaf_sigma_0.5.txt
    mv $x/sim_leaf_sigma_0.5_fixed.txt $x/sim_leaf_sigma_0.5.txt 

	sed -r 's/ +/,/g' $x/sim_leaf_sigma_1.5.txt > $x/sim_leaf_sigma_1.5_fixed.txt
	rm $x/sim_leaf_sigma_1.5.txt 
	mv $x/sim_leaf_sigma_1.5_fixed.txt $x/sim_leaf_sigma_1.5.txt 

	sed -r 's/ +/,/g' $x/sim_leaf_sigma_3.txt > $x/sim_leaf_sigma_3_fixed.txt 
	rm $x/sim_leaf_sigma_3.txt
	mv $x/sim_leaf_sigma_3_fixed.txt $x/sim_leaf_sigma_3.txt 

	sed -r 's/ +/,/g' $x/sim_leaf_sep_0.5.txt > $x/sim_leaf_sep_0.5_fixed.txt 
	rm $x/sim_leaf_sep_0.5.txt
	mv $x/sim_leaf_sep_0.5_fixed.txt $x/sim_leaf_sep_0.5.txt

	sed -r 's/ +/,/g' $x/sim_leaf_sep_1.txt > $x/sim_leaf_sep_1_fixed.txt 
	rm $x/sim_leaf_sep_1.txt
	mv $x/sim_leaf_sep_1_fixed.txt $x/sim_leaf_sep_1.txt

	sed -r 's/ +/,/g' $x/sim_leaf_sep_2.txt > $x/sim_leaf_sep_2_fixed.txt 
	rm $x/sim_leaf_sep_2.txt
	mv $x/sim_leaf_sep_2_fixed.txt $x/sim_leaf_sep_2.txt
done 

# python /Users/gary/Documents/Projects/spalin/problin/run_problin.py -c k10_character_matrix.csv -t true_tree.nwk -S sim_leaf_sigma_0.5.txt --delimiter comma -p k10_priors.csv -o k10_sigma05 --nInitials 10 --ultrametric --randomreps 3

# python /Users/gary/Documents/Projects/spalin/problin/run_problin.py -c $x/k10_r$r\_character_matrix.csv -t $x/true_tree.nwk -S $x/leaf_locations.txt --delimiter comma -p $x/k10_priors.csv -o $x/k10_r$r\_spalin_leaves.txt --nInitials 10 --ultrametric --randomreps 3 > $x/k10_r$r\_spalin_leaves.log 2>&1

