#!/bin/bash

# move results of running presets on different levels into one folder, ./level_results
for exp_type in Doom_*/ ; do
	cd "${exp_type}/experiments"
	mkdir -p ../../levels_results
	for experiment in */ ; do
		cd $experiment
		cp -rf worker_0.simple_rl_graph.main_level.main_level.agent_0.csv "../../../levels_results/${exp_type::-1}.csv"
		cd ..
	done
	cd ../..
done