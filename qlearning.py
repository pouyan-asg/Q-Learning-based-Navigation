#based on Square WORLD environment with 4 obstacles

import numpy as np
import math
import random


gamma = 0.75  # Discount factor
alpha = 0.9  # Learning rate
episode = 1000
location_to_state_coordination = {"L1": [1.5, 1.5, 0], "L2": [1.5, 0.5, 0], "L3": [1.5, -0.5, 0], "L4": [1.5, -1.5, 0], "L5": [0.5, 1.5, 0],
                    "L6": [0.5, 0.5, 0], "L7": [0.5, -0.5, 0], "L8": [0.5, -1.5, 0], "L9": [-0.5, 1.5, 0], "L10": [-0.5, 0.5, 0],
                     "L11": [-0.5, -0.5, 0], "L12": [-0.5, -1.5, 0], "L13": [-1.5, 1.5, 0], "L14": [-1.5, 0.5, 0],
                     "L15": [-1.5, -0.5, 0], "L16": [-1.5, -1.5, 0]}

location_to_state = {"L1": 0, "L2": 1, "L3": 2, "L4": 3, "L5": 4, "L6": 5, "L7": 6, "L8": 7, "L9": 8, "L10": 9,
                     "L11": 10, "L12": 11, "L13": 12, "L14": 13, "L15": 14, "L16": 15}

actions = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
rewards = np.array([[0, 1, 0, 0, 1, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1, -10, -10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0, -10, -10, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, -10, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 0, -10, 0, 0, 1, -10, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0, 0, -10, 0, 0, 0, -10, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, -10, 0, 0, 0, -10, 0, 0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, -10, 1, 0, 0, -10, 0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, -10, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 1, -10, -10, 0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, -10, -10, 1, 0, 1, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -10, 1, 0, 0, 1, 0]])

def optimal_route(start_location, end_location):

    # X_start = 0
    # Y_start = 0
    # X_end_new = (math.ceil(X_end)-0.5)
    # Y_end_new = (math.ceil(Y_end) - 0.5)
    Q = np.zeros([16, 16])
    rewards_new = np.copy(rewards)
    ending_state = location_to_state[end_location]
    rewards_new[ending_state, ending_state] = 900

    for i in range(episode):
        print(f"this is {i} episode")
        current_state = random.choice([0, 1, 2, 3, 4, 7, 8, 11, 12, 13, 14, 15])
        print(f"current state is {current_state}")
        playable_states = []
        for j in range(0, 16):
            if rewards_new[current_state, j] > 0:
                playable_states.append(j)
        print(f"the playable states are {playable_states}")
        next_state = np.random.choice(playable_states)
        print(f"the next state is {next_state}")
        TD = rewards_new[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state, ])] \
             - Q[current_state, next_state]
        Q[current_state, next_state] += alpha * TD
        print(Q)

    # Initialize the optimal route with the starting location
    route = [start_location]
    next_location = start_location

    while next_location != end_location:
        starting_state = location_to_state[start_location]
        next_state = np.argmax(Q[starting_state, ])
        state_to_location = dict((state, location) for location, state in location_to_state.items())
        next_location = state_to_location[next_state]
        route.append(next_location)
        start_location = next_location
    return route

def location_to_coordination(result):
    points = [location_to_state_coordination[result[res + 1]] for res in range(len(result) - 1)]
    A = []
    for i in range(len(points)):
        for j in range(3):
            A.append(points[i][j])
    return A


# ------------------------------------RUN-----------------
# start_location="L1"
# # end_location = input("please tell me the end location: ")
# end_location = "L15"
# points_seq = location_to_coordination(optimal_route(start_location, end_location))
# print(points_seq)
# n = 3
# # Returns a list of lists [[point1], [point2],...[pointn]]
# points = [points_seq[i:i + n] for i in range(0, len(points_seq), n)]
# print(points)
# result = optimal_route(start_location, end_location)
# print(result)
