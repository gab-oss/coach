#!/bin/bash

# puts scenarios in the place where vizdoom can access them
VIZDOOM_ROOT="../coach_env/lib/python3.6/site-packages/vizdoom/"
CUSTOM_SCENARIOS="../rl_coach/environments/doom/custom/."
cp -a $CUSTOM_SCENARIOS $VIZDOOM_ROOT

