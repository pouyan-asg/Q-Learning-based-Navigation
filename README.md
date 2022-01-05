# TurtleBot3 Navigation based on RL with Sending Goals to NavStack

<p align="justify">
    In order to use this repository, you should put files in specific locations and then run. The objective is the navigation of a Turtlebot3 (Waffle model) without any sensor based on Reinforcement Learning (RL) that goals send in the form of sequences.
 </p>

**_NOTE_: This program is a simple version of the combination of RL, navigation and sending goals in ROS that can be definitely extended to other RL's methods or worlds. It was created for testing some basic features of RL along with navigation and hence you can use it, modify it, share it and so on without any permission!**

## Q-Learning based Navigation
<p align="justify">
  In this section, I explain the Q-learning based navigation and a brief about this method. For a better understanding of RL or Q-learning, google it and you can find tons of documents. 
  </p>
<p align="justify">
  RL is an area of machine learning inspired by behaviourist psychology, concerned with how to take actions in an environment to maximize cumulative rewards. In fact, an agent does not have any data about the environment and just uses experiences to find an optimal action. The agent works in an environment based on Markov decision process (MDP) and for evaluation of its performance, there are two functions: value-function (state value) and Q-function (action value). The first function calculates the value of states under a policy and the latter represents the value of state-action pairs under a policy.
  </p>

Action-value techniques involve fitting a function, called the Q-values, that captures the expected return for taking a particular action at a particular state, and then following a particular policy thereafter [^1]. One form of Q-values based RL is Q-learning in which the agent maintains a table of *Q[S, A]*, where *S* is the set of states and *A* is the set of actions. Below figure shows the process of Q-learning.

![Q-learning process](https://drive.google.com/uc?export=view&id=1vmV6-BGJZqgsDGIoZUi84vCrAbnDn7eK)






## References
[^1]: [O'Donoghue, B., Munos, R., Kavukcuoglu, K., & Mnih, V. (2016). Combining policy gradient and Q-learning. arXiv preprint arXiv:1611.01626](https://arxiv.org/abs/1611.01626)
