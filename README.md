# TurtleBot3 Navigation based on RL with Sending Goals to NavStack

<p align="justify">
    In order to use this repository, you should put files in specific locations and then run. The objective is the navigation of a Turtlebot3 (Waffle model) without any sensor based on Reinforcement Learning (RL) that goals send in the form of sequences.
 </p>

**_NOTE_: This program is a simple version of the combination of RL, navigation and sending goals in ROS that can be definitely extended to other RL's methods or worlds. It was created for testing some basic features of RL along with navigation and hence you can use it, modify it, share it and so on without any permission!**

## Q-Learning based Navigation
<p align="justify">
  In this section, I explain the Q-learning based navigation and a brief about this method. For a better understanding of RL or Q-learning, google it and you can find tons of documents. 
  </p>

RL is an area of machine learning inspired by behaviourist psychology, concerned with how to take actions in an environment to maximize cumulative rewards. In fact, an agent does not have any data about the environment and just uses experiences to find an optimal action [^1]. The agent works in an environment based on Markov decision process (MDP) and for evaluation of its performance, there are two functions: value-function (state value) and Q-function (action value). The first function calculates the value of states under a policy and the latter represents the value of state-action pairs under a policy.

<img src="https://drive.google.com/uc?export=view&id=1c9LnShrP586bfPXWtju8ge15u5Lmiqcy" width="500" height="200" alt="RL process" align="middle">

Action-value techniques involve fitting a function, called the Q-values, that captures the expected return for taking a particular action at a particular state, and then following a particular policy thereafter [^2]. One form of Q-values based RL is Q-learning in which the agent maintains a table of *Q[S, A]*, where *S* is the set of states and *A* is the set of actions. Below figure shows the process of Q-learning.

<img src="https://drive.google.com/uc?export=view&id=1vmV6-BGJZqgsDGIoZUi84vCrAbnDn7eK" width="700" height="250" alt="Q-learning process" align="middle">

As mentioned above, Q-table updates in every cycle of execution of an action and receiving a reward based on the below equation:


<img src="https://drive.google.com/uc?export=view&id=1VpDmhPo3sUf7Kth1KydLVZT0fHjGefxf" alt="Q-learning formula" align="middle">


<p align="justify">
    Therefore, the reward function should be determined. Since the world that we want to test our program is a limited discrete square one, we can consider positive and negative rewards for each area. At first, see the working environment which consists of 16 areas and 4 obstacles. You can consider other environments with different features.
    </p>

<img src="https://drive.google.com/uc?export=view&id=1zc_CUuXLxaJQBaTBaqrfQ2AtNzdpUuCZ" alt="environment" align="middle">

<p align="justify">
    Each area is known with its number and the robot can determine its optimal path for going from one point to another without any sensor. When the robot wants to go from one area to another neighbourhood area, it receives a +1 reward. If there is an obstacle in the neighbourhood area, it will receive a -10 reward. For other options, there is not any reward. Thus, you can find with such a reward table, we guide the robot in the safest way. For instance, when the robot starts from the first area, it will receive +1 if it goes to areas number 2 and 5. Also, it will receive -10 and 0, if it goes to the sixth area and others, respectively. The reward for the last location is equal to 900. The rewards value and formation can be changed with respect to each environment.
    </p>
<p align="justify">
    Q-table is a 16 * 16 zero table that will be updated during episodes. In the Q-learning program, the user can determine the first and last location of the robot. Then robot tries to find an optimal path from the first point to the last point without hitting walls or obstacles. The path from the start location to the end location sends in the form of the goal's sequences that is explained in the next section. Summarily, in the programme, locations convert to the dedicated number of each area and then the Bellman equation updates in a loop ( total episode). Finally, the path with the highest value in the Q table will be chosen as an optimal path from start to end location. You can review the code in "qlearning.py" file.
    </p>
    
## Sending a Sequence of Goals to ROS

After Q-learning calculations for finding the optimal path from starting point to end location, it's necessary to send the goals of the robot's position as a node in ROS Navigation Stack. For more information about the program, visit this link: [Sending a sequence of Goals to ROS NavStack with Python](https://hotblackrobotics.github.io/en/blog/2018/01/29/seq-goals-py/) 

## Steps to Run the Code
In order to build an environment similar to mentioned one and deactivate the robot's sensors, put these files in suitable locations. Note that, due to working just based on the learning, the map is prepared beforehand because, without a laser scanner, it is hard and inefficient for the robot to mapping. Follow the below steps to run the code successfully:

1- Setup a workspace `catkin_ws` and create folder `src`. Then initialize `~/catkin_ws`.

2- Copy the `qlearning_navigation` folder from this repository and paste it in `~/catkin_ws/src` folder.

3- Install essential packages of Turtlebot3 from [THIS LINK](https://github.com/ROBOTIS-GIT/turtlebot3).

4- Move the `stage_2_map` folder from this repository to `~/catkin_ws/src/turtlebot3_nav-devel/src/simple_navigation_goals/config` folder.

5- Replace the `turtlebot3_waffle.urdf.xacro` file from this repository to `~/catkin_ws/src/turtlebot3/turtlebot3_description/urdf` folder.

6- Replace the `turtlebot3_stage_2.world` file from this repository to `~/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/worlds` folder.

7- Replace the `turtlebot3_stage_2.launch` file from this repository to `~/catkin_ws/src/turtlebot3_simulations/turtlebot3_gazebo/launch` folder.

8- Run the command `catkin_make` from the `~/catkin_ws` location. The files should be successfully compiled.

9- Source the workspace by running the command `source devel/setup.bash` from `~catkin_ws` location.

10- Run the following commands in different terminals from the location `~/catkin_ws`:

in first terminal: `roslaunch turtlebot3_gazebo turtlebot3_stage_2.launch`

in second terminal: `roslaunch qlearning_navigation qlearning_navigation.launch`

in third terminal: `python ~catkin_ws/src/qlearning_navigation/scripts/main_prog.py`

if you run by default, you will see the Turtlebot is moving from location 1 to location 15. For changing them, go to the `main_prog.py` file in `~catkin_ws/src/qlearning_navigation/scripts/` folder and alter these below lines. The locations should write in this style L1, L2, L3, ...

`start_location = "L1"

end_location = "L15"`


## References

[^1]: Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press
[^2]: [O'Donoghue, B., Munos, R., Kavukcuoglu, K., & Mnih, V. (2016). Combining policy gradient and Q-learning. arXiv preprint arXiv:1611.01626](https://arxiv.org/abs/1611.01626)
