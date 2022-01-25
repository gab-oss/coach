# Adding module path to sys path if not there, so rl_coach submodules can be imported
import os
import sys
import tensorflow as tf
    
from rl_coach.coach import CoachInterface
import argparse

parser = argparse.ArgumentParser(description='Default algorithm parameters')
parser.add_argument('num', type=int, 
                    help='number of runs')

args = parser.parse_args()

for i in range(args.num):
    tf.reset_default_graph()
    coach = CoachInterface(preset='Doom_Basic_Rainbow',
                        num_workers=1)
    coach.run()
