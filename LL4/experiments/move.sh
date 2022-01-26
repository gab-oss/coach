#!/bin/bash

for exp_type in */ ; do
	cd "${exp_type}/experiments"
	mkdir ../results
	for experiment in */ ; do
		cd $experiment
		cp worker_0.simple_rl_graph.main_level.main_level.agent_0.csv "../../results/${experiment::-1}"
		cd ..
	done
	cd ../..
done