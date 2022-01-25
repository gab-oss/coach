#!/bin/bash
# run after activating venv!
VIZDOOM_ROOT="../coach_env/lib/python3.6/site-packages/vizdoom/"
EXP='experiments'

bash set_scenarios.sh
for LEVEL in "basic" "basic_mod" "deathmatch" "deathmatch_mod"
do
    DIR="rainbow_level_${LEVEL}"
    rm -rf $EXP/$DIR
    mkdir -p $EXP/$DIR
    cd $EXP/$DIR
    VIZDOOM_ROOT=$VIZDOOM_ROOT && coach -r -p Doom_Basic_Rainbow_New_Params -lvl $LEVEL
    cd ../..
done