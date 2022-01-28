# Adding module path to sys path if not there, so rl_coach submodules can be imported
import os
import sys
import tensorflow as tf

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from rl_coach.coach import CoachInterface

policies = ["EGreedyParameters();agent_params.exploration.epsilon_schedule = LinearSchedule(1.0, 0.01, 10000)"]

for p in policies:
    tf.reset_default_graph()
    print("agent_params.exploration={}".format(p))
    coach = CoachInterface(preset='Doom_Basic_QR_DQN',
                           custom_parameter='agent_params.exploration={}'.format(p),
                           num_workers=1)
    coach.run()
