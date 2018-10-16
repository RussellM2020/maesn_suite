from sandbox.rocky.tf.algos.maml_trpo import MAMLTRPO
from rllab.baselines.linear_feature_baseline import LinearFeatureBaseline
from rllab.baselines.zero_baseline import ZeroBaseline
from rllab.envs.normalized_env import normalize
from rllab.misc.instrument import stub, run_experiment_lite
from sandbox.rocky.tf.policies.maml_minimal_gauss_mlp_policy import MAMLGaussianMLPPolicy
from sandbox.rocky.tf.envs.base import TfEnv
#from rllab.envs.mujoco.wheeled_robot_goal_c1 import WheeledEnvGoal
from rllab.envs.mujoco.wheeled_robot_goal_subsample import WheeledEnvGoal
#from rllab.envs.mujoco.blockpush_env_sparse import BlockPushEnvSparse

import tensorflow as tf

fast_learning_rate = 0
baselines = ['linear']
fast_batch_size = 50  # 10 works for [0.1, 0.2], 20 doesn't improve much for [0,0.2]
meta_batch_size = 20
num_total_tasks = 100  # 10 also works, but much less stable, 20 is fairly stable, 40 is more stable
max_path_length = 200
num_grad_updates = 1
meta_step_size = 0.01
kl_weightings = [ 0, 0.01]
#kl_weighting = 0.001
kl_scheme = None
use_maml = True
latent_dims = [2]

# initial_params_file = 'data/local/experiment/experiment_2017_11_04_18_39_40_0001/itr_49.pkl'

for latent_dim in latent_dims:
    for kl_weighting in kl_weightings:
        stub(globals())

        env = TfEnv( normalize(WheeledEnvGoal()))
        policy = MAMLGaussianMLPPolicy(
            name="policy",
            env_spec=env.spec,
            grad_step_size=fast_learning_rate,
            hidden_nonlinearity=tf.nn.relu,
            hidden_sizes=(100,100),
            latent_dim=latent_dim,
            num_total_tasks=num_total_tasks,
        )

        baseline = LinearFeatureBaseline(env_spec=env.spec)

        algo = MAMLTRPO(
            env=env,
            policy=policy,
            baseline=baseline,
            batch_size=fast_batch_size, # number of trajs for grad update
            max_path_length=max_path_length,
            meta_batch_size=meta_batch_size,
            num_grad_updates=num_grad_updates,
            n_itr=500,
            use_maml=use_maml,
            step_size=meta_step_size,
            plot=False,
            latent_dim=latent_dim,
            num_total_tasks=num_total_tasks,
            kl_weighting=kl_weighting,
            #plottingFolder = "Sparse_BP_kl0.05_ldim2",
            kl_scheme=kl_scheme
        )
        run_experiment_lite(
            algo.train(),
            n_parallel=4,
            snapshot_mode="all",
            #python_command='python3',
            seed=1,
            exp_prefix='LatentSpaceBaseline_wheeledRobot_radius2_train100_subsample',
            exp_name='fulltrpomasen'+str(int(use_maml))+'_ldim_'+str(latent_dim)+'_fbs'+str(fast_batch_size)+'_mbs'+str(meta_batch_size)+'_flr_' + str(fast_learning_rate) + 'metalr_' + str(meta_step_size) +'_step1'+str(num_grad_updates) + "kl_scheme" + str(kl_scheme) + "kl_weighting" + str(kl_weighting),
            plot=False,
            sync_s3_pkl=True,
            mode="ec2",
            pre_commands=["yes | pip install --upgrade pip",
                           "yes | pip install tensorflow=='1.2.0'"]
        )
