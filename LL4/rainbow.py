# Adding module path to sys path if not there, so rl_coach submodules can be imported
import os
import sys
import tensorflow as tf
module_path = os.path.abspath(os.path.join('..'))
# resources_path = os.path.abspath(os.path.join('Resources'))
if module_path not in sys.path:
    sys.path.append(module_path)
# if resources_path not in sys.path:
#     sys.path.append(resources_path)
    
from rl_coach.coach import CoachInterface

for i in range(15,20):
    tf.reset_default_graph()
    print("n_step = {}".format(i))
    coach = CoachInterface(preset='Doom_Basic_Rainbow',
                        # The optional custom_parameter enables overriding preset settings
                        custom_parameter='improve_steps=TrainingSteps(5000);agent_params.algorithm.n_step={}'.format(i),
                        # Other optional parameters enable easy access to advanced functionalities
                        num_workers=1, checkpoint_save_secs=10)

    coach.run()
