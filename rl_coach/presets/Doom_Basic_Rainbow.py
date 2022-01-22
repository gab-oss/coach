from rl_coach.agents.dqn_agent import DQNAgentParameters, DQNNetworkParameters
from rl_coach.agents.rainbow_dqn_agent import RainbowDQNAgentParameters
from rl_coach.architectures.head_parameters import QuantileRegressionQHeadParameters
from rl_coach.base_parameters import VisualizationParameters, PresetValidationParameters
from rl_coach.core_types import CsvDataset, TrainingSteps, EnvironmentEpisodes, EnvironmentSteps
from rl_coach.environments.doom_environment import DoomEnvironmentParameters
from rl_coach.exploration_policies.boltzmann import BoltzmannParameters
from rl_coach.exploration_policies.bootstrapped import BootstrappedParameters
from rl_coach.exploration_policies.greedy import GreedyParameters
from rl_coach.exploration_policies.parameter_noise import ParameterNoiseParameters
from rl_coach.graph_managers.basic_rl_graph_manager import BasicRLGraphManager
from rl_coach.graph_managers.graph_manager import ScheduleParameters
from rl_coach.memories.episodic.episodic_experience_replay import EpisodicExperienceReplayParameters
from rl_coach.memories.memory import MemoryGranularity
from rl_coach.memories.non_episodic.experience_replay import ExperienceReplayParameters
from rl_coach.schedules import LinearSchedule

from rl_coach.core_types import PickledReplayBuffer



####################
# Graph Scheduling #
####################

schedule_params = ScheduleParameters()
schedule_params.improve_steps = TrainingSteps(10000)
schedule_params.steps_between_evaluation_periods = EnvironmentEpisodes(8) # kiedy skończyć
schedule_params.evaluation_steps = EnvironmentEpisodes(4)
schedule_params.heatup_steps = EnvironmentSteps(1000)


#########
# Agent #
#########
agent_params = RainbowDQNAgentParameters()

# DQN params
agent_params.algorithm.num_steps_between_copying_online_weights_to_target = EnvironmentSteps(100)
agent_params.algorithm.discount = 0.99
agent_params.algorithm.num_consecutive_playing_steps = EnvironmentSteps(1)

# NN configuration
agent_params.network_wrappers['main'].learning_rate = 0.00025
agent_params.network_wrappers['main'].replace_mse_with_huber_loss = False

# ER size
agent_params.memory.max_size = (MemoryGranularity.Transitions, 40000)

agent_params.memory.beta = LinearSchedule(0.4, 1, 10000)
agent_params.memory.alpha = 0.5
agent_params.memory = ExperienceReplayParameters()
agent_params.memory.load_memory_from_file_path = PickledReplayBuffer('/home/gabe/coach/experiments/gfd/22_01_2022-18_43/replay_buffer.p')


###############
# Environment #
###############
env_params = DoomEnvironmentParameters(level='basic')

########
# Test #
########
preset_validation_params = PresetValidationParameters()
preset_validation_params.test = True
preset_validation_params.min_reward_threshold = 20
preset_validation_params.max_episodes_to_achieve_reward = 400


#default policy: ParameterNoise
#agent_params.exploration = BootstrappedParameters()
#agent_params.exploration = GreedyParameters()

#default n_step = 3
agent_params.algorithm.n_step = 10



graph_manager = BasicRLGraphManager(agent_params=agent_params, env_params=env_params,
                                    schedule_params=schedule_params, vis_params=VisualizationParameters(),
                                    preset_validation_params=preset_validation_params)
