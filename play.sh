#!/bin/bash
# run after activating venv!
# example: bash run_preset Doom_Basic_DQN
VIZDOOM_ROOT="coach_env/lib/python3.6/site-packages/vizdoom/"
VIZDOOM_ROOT=$VIZDOOM_ROOT && coach -et rl_coach.environments.doom_environment:DoomEnvironmentParameters -lvl Basic --play



