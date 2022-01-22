#!/bin/bash
# run after activating venv!
# example: bash run_preset Doom_Basic_DQN
# add experiment dir and preset name as params
VIZDOOM_ROOT="coach_env/lib/python3.6/site-packages/vizdoom/"
VIZDOOM_ROOT=$VIZDOOM_ROOT && coach -p Doom_Basic_Rainbow 

