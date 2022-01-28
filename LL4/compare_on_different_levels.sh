#!/bin/bash
VIZDOOM_ROOT="../coach_env/lib/python3.6/site-packages/vizdoom/"
EXP='experiments'
bash set_scenarios.sh

for lvl in "basic" "basic_mod" "deathmatch" "deatchmatch_mod" ; do
    for preset in "Doom_Basic_Rainbow" "Doom_Basic_QR_DQN" ; do
        DIR="${preset}_${lvl}"
        rm -rf $EXP/$DIR
        mkdir -p $EXP/$DIR
        cd $EXP/$DIR
        VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../preset_on_level.py $preset $lvl
        cd ../..
    done
done