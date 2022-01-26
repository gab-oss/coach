# Adding module path to sys path if not there, so rl_coach submodules can be imported
import os
import sys
import tensorflow as tf
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from rl_coach.coach import CoachInterface
import argparse

parser = argparse.ArgumentParser(description='Training parameters -- set the range of learning rate')
parser.add_argument('start', type=float, 
                    help='value of learning rate to start with')
parser.add_argument('stop', type=float, 
                    help='value of learning rate to stop with')
parser.add_argument('step', type=float,
                    help='iteration step')

args = parser.parse_args()

rate = args.start
while rate <= args.stop:
    tf.reset_default_graph()
    print("agent_params.network_wrappers['main'].learning_rate={}".format(rate))
    coach = CoachInterface(preset='Doom_Basic_Rainbow',
                        custom_parameter="agent_params.network_wrappers['main'].learning_rate={}".format(rate),
                        num_workers=1)
    coach.run()
    rate += args.step
