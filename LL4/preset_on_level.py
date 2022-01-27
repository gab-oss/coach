# Adding module path to sys path if not there, so rl_coach submodules can be imported
import os
import sys
import tensorflow as tf
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from rl_coach.coach import CoachInterface
import argparse

parser = argparse.ArgumentParser(description='Set preset and level')
parser.add_argument('preset', type=str, 
                    help='preset name')
parser.add_argument('lvl', type=str, 
                    help='level name')

args = parser.parse_args()

tf.reset_default_graph()
print("{} on level {}".format(args.preset, args.lvl))
coach = CoachInterface(preset=args.preset,
                    custom_parameter="env_params=DoomEnvironmentParameters(level={})".format(args.lvl),
                    num_workers=1)
coach.run()