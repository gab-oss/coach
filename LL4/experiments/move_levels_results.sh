#!/bin/bash

for exp_type in Doom_*/ ; do
	cd "${exp_type}/experiments"
	mkdir -p ../../levels_results
	for experiment in */ ; do
		cd $experiment
		cp worker_0.simple_rl_graph.main_level.main_level.agent_0.csv "../../../levels_results/${exp_type::-1}.csv"
		cd ..
	done
	cd ../..
done