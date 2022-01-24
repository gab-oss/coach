# Adding module path to sys path if not there, so rl_coach submodules can be imported
import os
import sys
import tensorflow as tf
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from rl_coach.coach import CoachInterface
import argparse

parser = argparse.ArgumentParser(description='Discount as int (without decimal point)')
parser.add_argument('start', type=int, 
                    help='starting value')
parser.add_argument('stop', type=int, 
                    help='stopping value')
parser.add_argument('step', type=int,
                    help='step')

args = parser.parse_args()


for i in range(args.start,args.stop,args.step):
    tf.reset_default_graph()
    discount = i/100
    print("agent_params.algorithm.discount={}".format(i))
    coach = CoachInterface(preset='Doom_Basic_Rainbow',
                        custom_parameter='agent_params.algorithm.discount={}'.format(i),
                        num_workers=1, checkpoint_save_secs=30)

    coach.run()
