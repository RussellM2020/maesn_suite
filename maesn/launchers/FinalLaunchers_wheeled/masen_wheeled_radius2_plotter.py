from sandbox.rocky.tf.algos.maml_trpo_plotter import MAMLTRPO
from rllab.baselines.linear_feature_baseline import LinearFeatureBaseline
from rllab.baselines.zero_baseline import ZeroBaseline
from rllab.envs.normalized_env import normalize
from rllab.misc.instrument import stub, run_experiment_lite
from sandbox.rocky.tf.policies.maml_minimal_gauss_mlp_policy_adaStep import MAMLGaussianMLPPolicy
from sandbox.rocky.tf.envs.base import TfEnv
#from rllab.envs.mujoco.pusher_env_morerandom_subsample_ec2 import  PusherEnvRandomized
#from rllab.envs.mujoco.blockpush_env_sparse import BlockPushEnvSparse
from rllab.envs.mujoco.wheeled_robot_goal_subsample import WheeledEnvGoal
import tensorflow as tf

fast_learning_rate = 1
baselines = ['linear']
fast_batch_size = 10  # 10 works for [0.1, 0.2], 20 doesn't improve much for [0,0.2]
meta_batch_size = 20
num_total_tasks = 100  # 10 also works, but much less stable, 20 is fairly stable, 40 is more stable
max_path_length = 200
num_grad_updates = 1
meta_step_size = 0.01
kl_weighting = 0.5
#kl_weighting = 0.05
kl_scheme = None
use_maml = True
latent_dim = 2

# initial_params_file = 'data/local/experiment/experiment_2017_11_04_18_39_40_0001/itr_49.pkl'

initParamFile = '/home/russellm/generativemodel_tasks/maml_rl_fullversion/data/local/preTrainDense-TrainSparse-masen-wheeledRobot-SparseBonus-UniformlySelTasks/fulltrpomasen1_ldim_2_fbs10_mbs20_flr_1metalr_0.1_step11kl_schemeNonekl_weighting0.5/itr_36.pkl'

stub(globals())

env = TfEnv( normalize(WheeledEnvGoal()))


#baseline = LinearFeatureBaseline(env_spec=env.spec)
#initParamFile ="/home/russellm/generativemodel_tasks/maml_rl_fullversion/data/s3/masen-wheeledRobot-radius2-train100-subsampling/fulltrpomasen1_ldim_2_fbs50_mbs20_flr_1metalr_0.01_step11kl_schemeNonekl_weighting"+str(kl_weighting)+"/itr_300.pkl"


#initParamFile = '/home/russellm/generativemodel_tasks/maml_rl_fullversion/data/s3/nipsRebuttal-preTrainDense-TrainSparse-masen-wheeledRobot-radius2-train100-subsampling/fulltrpomasen1_ldim_2_fbs50_mbs20_flr_1metalr_0.01_step11kl_schemeNonekl_weighting0.5/itr_10.pkl'

#initParamFile = '/home/russellm/generativemodel_tasks/maml_rl_fullversion/data/local/preTrainDense-TrainSparse-masen-wheeledRobot-radius2-train20-uniformlySelTasks/fulltrpomasen1_ldim_2_fbs10_mbs20_flr_1metalr_0.01_step11kl_schemeNonekl_weighting0.5/itr_28.pkl'

#"/home/russellm/generativemodel_tasks/maml_rl_fullversion/data/s3/masen-wheeledRobot-radius2-train100-subsampling/fulltrpomasen1_ldim_2_fbs50_mbs20_flr_1metalr_0.01_step11kl_schemeNonekl_weighting0.1/itr_300.pkl"

#"/home/russellm/generativemodel_tasks/maml_rl_fullversion/data/s3/masen-wheeledRobot-radius2-train100-subsampling/fulltrpomasen1_ldim_2_fbs50_mbs20_flr_1metalr_0.01_step11kl_schemeNonekl_weighting"+str(kl_weighting)+"/itr_320.pkl"

algo = MAMLTRPO(
    env=env,
    policy=None,
    load_policy = initParamFile,
    baseline=None,
    batch_size=fast_batch_size, # number of trajs for grad update
    max_path_length=max_path_length,
    meta_batch_size=meta_batch_size,
    num_grad_updates=num_grad_updates,
    n_itr=1,
    use_maml=use_maml,
    step_size=meta_step_size,
    plot=False,
    latent_dim=latent_dim,
    num_total_tasks=num_total_tasks,
    kl_weighting=kl_weighting,
    #plottingFolder = "Sparse_BP_kl0.05_ldim2",
    visitationFolder = "masen_wheeled_sparseBonus",
    visitationFile = "pretrainDense_trainSparse_uniformlySelTasks_itr36",
    kl_scheme=kl_scheme,
    addedNoise = True,
)
run_experiment_lite(
    algo.train(),
    n_parallel=4,
    snapshot_mode="all",
    #python_command='python3',
    seed=1,
    # exp_prefix='plotter_masen_wheeledRobot_radius2_train100',
    # exp_name='fulltrpomasen'+str(int(use_maml))+'_ldim_'+str(latent_dim)+'_fbs'+str(fast_batch_size)+'_mbs'+str(meta_batch_size)+'_flr_' + str(fast_learning_rate) + 'metalr_' + str(meta_step_size) +'_step1'+str(num_grad_updates) + "kl_scheme" + str(kl_scheme) + "kl_weighting" + str(kl_weighting),
    #plot=False,
    #sync_s3_pkl=True,
    #mode="ec2",
    #pre_commands=["yes | pip install --upgrade pip",
    #               "yes | pip install tensorflow=='1.2.0'"]
)

# from sandbox.rocky.tf.algos.maml_trpo import MAMLTRPO
# from rllab.baselines.linear_feature_baseline import LinearFeatureBaseline
# from rllab.baselines.gaussian_mlp_baseline import GaussianMLPBaseline
# from rllab.baselines.zero_baseline import ZeroBaseline
# from rllab.envs.normalized_env import normalize
# from rllab.envs.mujoco.blockpush_env import BlockPushEnv
# from rllab.misc.instrument import stub, run_experiment_lite
# from sandbox.rocky.tf.policies.maml_minimal_gauss_mlp_policy import MAMLGaussianMLPPolicy
# from sandbox.rocky.tf.envs.base import TfEnv

# import tensorflow as tf

# fast_learning_rates = [0.01]
# baselines = ['linear']
# fast_batch_size = 100  # 10 works for [0.1, 0.2], 20 doesn't improve much for [0,0.2]
# meta_batch_size = 10  # 10 also works, but much less stable, 20 is fairly stable, 40 is more stable
# max_path_length = 100
# num_grad_updates = 1
# meta_step_size = 0.01
# kl_weightings = [0.01]
# use_maml = True

# for fast_learning_rate in fast_learning_rates:
#     for kl_weighting in kl_weightings:
#         stub(globals())

#         env = TfEnv(BlockPushEnv())
#         policy = MAMLGaussianMLPPolicy(
#             name="policy",
#             env_spec=env.spec,
#             grad_step_size=fast_learning_rate,
#             hidden_nonlinearity=tf.nn.relu,
#             hidden_sizes=(100,100),
#             latent_dim=2,
#             num_total_tasks=10,
#             init_std=10.
#         )

#         baseline = LinearFeatureBaseline(env_spec=env.spec)

#         algo = MAMLTRPO(
#             env=env,
#             policy=policy,
#             baseline=baseline,
#             batch_size=fast_batch_size, # number of trajs for grad update
#             max_path_length=max_path_length,
#             meta_batch_size=meta_batch_size,
#             num_grad_updates=num_grad_updates,
#             n_itr=500,
#             use_maml=use_maml,
#             step_size=meta_step_size,
#             plot=False,
#             latent_dim=2,
#             num_total_tasks=10,
#             kl_weighting=kl_weighting
#         )

#         run_experiment_lite(
#             algo.train(),
#             n_parallel=1,
#             snapshot_mode="all",
#             python_command='python3',
#             seed=1,
#             exp_prefix='MAML-retrained-backtonormal',
#             exp_name='trpomaml'+str(int(use_maml))+'_fbs'+str(fast_batch_size)+'_mbs'+str(meta_batch_size)+'_flr_' + str(fast_learning_rate) + 'metalr_' + str(meta_step_size) +'_step1'+str(num_grad_updates) + "kl_weight" + str(kl_weighting),
#             # sync_s3_pkl=True,
#             # mode='ec2',
#             plot=False,
#             # pre_commands=["yes | pip install --upgrade pip",
#             #           "yes | pip install tensorflow=='1.2.0'"]

#         )
#         # run_experiment_lite(
#         #     algo.train(),
#         #     n_parallel=1,
#         #     snapshot_mode="all",
#         #     python_command='python3',
#         #     seed=1,
#         #     exp_prefix='testing_newmaml',
#         #     exp_name='trpomaml'+str(int(use_maml))+'_fbs'+str(fast_batch_size)+'_mbs'+str(meta_batch_size)+'_flr_' + str(fast_learning_rate) + 'metalr_' + str(meta_step_size) +'_step1'+str(num_grad_updates) + "kl_weight" + str(kl_weighting),
#         #     plot=False,
#         # )
