import numpy as np
from grid_world import standard_grid,negative_grid
from iterative_policy_evaluation import print_values,print_policy

gamma = 0.9
theta = 10e-4
ALL_ACTIONS = ('U','D','L','R')

#This is deterministic
# p(s',r'|s,a) = 1 or 0

if __name__ == "__main__":

    grid = negative_grid()
    states = grid.all_states()

    #print("Rewards:")
    #print_values(grid.rewards,grid)

    #Initialize V
    V = {}
    for s in states:
        V[s] = 0.0

    while True:
        delta = 0
        for s in states:
            if s not in grid.actions:
                continue

            v = V[s]
            max_val = float("-inf")
            for action in grid.actions[s]:
                grid.set_state(s)
                r = grid.move(action)
                val = r + gamma * V[grid.current_state()]
                if val > max_val:
                    max_val = val
            V[s] = max_val
            delta = max(delta,abs(v-V[s]))

        if delta < theta:
            print_values(V,grid)
            break


    # Output a deterministic policy (which is optimal)
    pi = {}
    for s in grid.actions:
        max_val = float("-inf")
        for action in grid.actions[s]:
            grid.set_state(s)
            r = grid.move(action)
            val = r + V[grid.current_state()]
            if val > max_val :
                max_val = val
                max_action = action

        pi[s] = max_action

    print_policy(pi,grid)
            

    
            

    
    
