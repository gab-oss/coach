#!/bin/bash
# run after activating venv!
VIZDOOM_ROOT="../coach_env/lib/python3.6/site-packages/vizdoom/"
EXP='experiments'

# run once with a chosen number of training steps 
START=15000
STOP=15001
STEP=1
DIR="rainbow_training_steps_${START}"
rm -rf $EXP/$DIR
mkdir -p $EXP/$DIR
cd $EXP/$DIR
VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_training_steps.py $START $STOP $STEP
cd ../..

# run with a range of n_step values
START=3
STOP=23
STEP=4
DIR="rainbow_n_step_${START}_${STOP}_${STEP}"
rm -rf $EXP/$DIR
mkdir -p $EXP/$DIR
cd $EXP/$DIR
VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_n_step.py $START $STOP $STEP
cd ../..

# run with a range of discount values
START=11
STOP=100
STEP=11
DIR="rainbow_discount_${START}_${STOP}_${STEP}"
rm -rf $EXP/$DIR
mkdir -p $EXP/$DIR
cd $EXP/$DIR
VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_discount.py $START $STOP $STEP
cd ../..

# run with different exploration policies (defined in test file)
DIR='rainbow_policy'
rm -rf $EXP/$DIR
mkdir -p $EXP/$DIR
cd $EXP/$DIR
VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_policy.py
VIZDOOM_ROOT=$VIZDOOM_ROOT && coach -r -p Doom_Basic_Rainbow
cd ../..

# run with a wider range of learning rates
START=0.00001
STOP=0.99999
STEP=0.2222
DIR="rainbow_learning_rate_${START}_${STOP}_${STEP}"
rm -rf $EXP/$DIR
mkdir -p $EXP/$DIR
cd $EXP/$DIR
VIZDOOM_ROOT=$VIZDOOM_ROOT && python3.6 ../../rainbow_learning_rate.py $START $STOP $STEP
cd ../..
