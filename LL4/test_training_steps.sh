#!/bin/bash
# run after activating venv!
# example: bash run_preset Doom_Basic_DQN
VIZDOOM_ROOT="coach_env/lib/python3.6/site-packages/vizdoom/"
EXP='experiments'

DIR='rainbow_default'
mkdir -p $EXP/$DIR
cd $EXP/$DIR
VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_default.py 10
cd ../..

#DIR='rainbow_training_steps_every_3500'
#mkdir -p $EXP/$DIR
#cd $EXP/$DIR
#VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_training_steps.py 1000 18500 3500
#cd ../..

DIR='rainbow_training_steps_10k'
mkdir -p $EXP/$DIR
cd $EXP/$DIR
VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_training_steps.py 10000 10001 1
cd ../..

# DIR='rainbow_n_step_2_20_3'
# mkdir -p $EXP/$DIR
# cd $EXP/$DIR
# VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_n_step.py 2 20 3
#cd ../..

# DIR='rainbow_discount_70_120_10'
# mkdir -p $EXP/$DIR
# cd $EXP/$DIR
# VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_discount.py 70 120 10
#cd ../..

# DIR='rainbow_policy'
# mkdir -p $EXP/$DIR
# cd $EXP/$DIR
# VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_policy.py
#cd ../..
