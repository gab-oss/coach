#!/bin/bash
# run after activating venv!
# example: bash run_preset.sh Doom_Basic_DQN
VIZDOOM_ROOT="coach_env/lib/python3.6/site-packages/vizdoom/"
VIZDOOM_ROOT=$VIZDOOM_ROOT && coach -r -p $1 -lvl deathmatch
