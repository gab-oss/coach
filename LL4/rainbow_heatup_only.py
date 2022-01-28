# Adding module path to sys path if not there, so rl_coach submodules can be imported
import os
import sys
import tensorflow as tf
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from rl_coach.coach import CoachInterface
import argparse

tf.reset_default_graph()
coach = CoachInterface(preset='Doom_Basic_Rainbow',
                    custom_parameter='heatup_steps=EnvironmentSteps(2500);improve_steps=TrainingSteps(0);steps_between_evaluation_periods=EnvironmentEpisodes(1);evaluation_steps=EnvironmentEpisodes(100)',
                    num_workers=1)
coach.run()
