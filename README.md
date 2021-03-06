# Meta-Reinforcement Learning of Structured Exploration Strategies

This repo contains code accompaning the paper, 	[Meta-Reinforcement Learning of Structured Exploration Strategies (Gupta et al., NIPS 2018)](https://arxiv.org/abs/1802.07245). 

### Dependencies
This code is based off of the rllab code repository and can be installed in the same way (see below). This codebase is not necessarily backwards compatible with rllab.

The MAESN code uses the TensorFlow rllab version, so be sure to install TensorFlow v1.0+.

### Usage
Scripts for running the experiments found in the paper are located in `launchers/`. The scripts are setup to use local_docker or ec2. The MuJoCo environments are located in `rllab/envs/mujoco/`.

##### Training 

`python train.py <algo> --env <envName>`, where algo can be Maesn or LSBaseline, envName can be Ant, Pusher or Wheeled.
Hyperparameters can be set in the hyperparam_sweep file. For the LSBaseline, the `fast_learning_rate` must be 0.

##### Testing 

`python test.py <algo> --env <envName> --initial_params_file <fileName> --learning_rate <rate> --latent_dim <latentDim>`.

The meta-trained policy file must be placed in `metaTrainedPolices/`, and its name is then passed to `initial_params_file`.
Make sure that the rate and latentDim at testing are the same as the `fast_learning_rate` and `latent_dim` at training.

### aws ec2


The following image IDs are known to work
```
us-east-1 : ami-0bb2bf4857db440e0 
us-west-1 : ami-05e00979871a39188
us-west-2 : ami-0111a16ab53cb7ea9
```
Docker Image : `russellm888/rllab3`   

# rllab

[![Docs](https://readthedocs.org/projects/rllab/badge)](http://rllab.readthedocs.org/en/latest/)
[![Circle CI](https://circleci.com/gh/rllab/rllab.svg?style=shield)](https://circleci.com/gh/rllab/rllab)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/rllab/rllab/blob/master/LICENSE)
[![Join the chat at https://gitter.im/rllab/rllab](https://badges.gitter.im/rllab/rllab.svg)](https://gitter.im/rllab/rllab?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


rllab is a framework for developing and evaluating reinforcement learning algorithms. It includes a wide range of continuous control tasks plus implementations of the following algorithms:


- [REINFORCE](https://github.com/rllab/rllab/blob/master/rllab/algos/vpg.py)
- [Truncated Natural Policy Gradient](https://github.com/rllab/rllab/blob/master/rllab/algos/tnpg.py)
- [Reward-Weighted Regression](https://github.com/rllab/rllab/blob/master/rllab/algos/erwr.py)
- [Relative Entropy Policy Search](https://github.com/rllab/rllab/blob/master/rllab/algos/reps.py)
- [Trust Region Policy Optimization](https://github.com/rllab/rllab/blob/master/rllab/algos/trpo.py)
- [Cross Entropy Method](https://github.com/rllab/rllab/blob/master/rllab/algos/cem.py)
- [Covariance Matrix Adaption Evolution Strategy](https://github.com/rllab/rllab/blob/master/rllab/algos/cma_es.py)
- [Deep Deterministic Policy Gradient](https://github.com/rllab/rllab/blob/master/rllab/algos/ddpg.py)

rllab is fully compatible with [OpenAI Gym](https://gym.openai.com/). See [here](http://rllab.readthedocs.io/en/latest/user/gym_integration.html) for instructions and examples.

rllab only officially supports Python 3.5+. For an older snapshot of rllab sitting on Python 2, please use the [py2 branch](https://github.com/rllab/rllab/tree/py2).

rllab comes with support for running reinforcement learning experiments on an EC2 cluster, and tools for visualizing the results. See the [documentation](https://rllab.readthedocs.io/en/latest/user/cluster.html) for details.

The main modules use [Theano](http://deeplearning.net/software/theano/) as the underlying framework, and we have support for TensorFlow under [sandbox/rocky/tf](https://github.com/openai/rllab/tree/master/sandbox/rocky/tf).

### Documentation

Documentation is available online: [https://rllab.readthedocs.org/en/latest/](https://rllab.readthedocs.org/en/latest/).

### Citing rllab

If you use rllab for academic research, you are highly encouraged to cite the following paper:

- Yan Duan, Xi Chen, Rein Houthooft, John Schulman, Pieter Abbeel. "[Benchmarking Deep Reinforcement Learning for Continuous Control](http://arxiv.org/abs/1604.06778)". _Proceedings of the 33rd International Conference on Machine Learning (ICML), 2016._

### Credits

rllab was originally developed by Rocky Duan (UC Berkeley / OpenAI), Peter Chen (UC Berkeley), Rein Houthooft (UC Berkeley / OpenAI), John Schulman (UC Berkeley / OpenAI), and Pieter Abbeel (UC Berkeley / OpenAI). The library is continued to be jointly developed by people at OpenAI and UC Berkeley.

### Slides

Slides presented at ICML 2016: https://www.dropbox.com/s/rqtpp1jv2jtzxeg/ICML2016_benchmarking_slides.pdf?dl=0



