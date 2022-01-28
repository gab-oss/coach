#!/bin/bash

# move results (csv) to one folder for every type of experiment, ./[experiment_type]/results/
for exp_type in */ ; do
	cd "${exp_type}/experiments"
	mkdir -p ../results
	for experiment in */ ; do
		cd $experiment
		cp -rf worker_0.simple_rl_graph.main_level.main_level.agent_0.csv "../../results/${experiment::-1}.csv"
		cd ..
	done
	cd ../..
done