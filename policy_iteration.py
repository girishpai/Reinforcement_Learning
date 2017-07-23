import numpy as np
from grid_world import negative_grid
from iterative_policy_evaluation import print_values,print_policy

THETA = 1e-3
gamma = 0.9
ALL_ACTIONS = ('U','D','L','R')

#This is a deterministic enviroment
# p(s',r'|s,a) = 1 or 0

if __name__ == "__main__" :
    grid = negative_grid()


    states = grid.all_states()
    #Initialize value function with 0
    #Initialize policy to random action for each state
    V = {}
    pi = {}
    for i in range(grid.width):
        for j in range(grid.height):
          V[(i,j)] = 0.0

    for s in grid.actions:
        pi[s] = np.random.choice(ALL_ACTIONS)


    while True:
        #Policy Evaluation
        while True :
            delta = 0
            old_v = 0.0
            for s in states:
                if s not in pi:
                    continue

                grid.set_state(s)
                old_v = V[s]
                action = pi[s]
                r = grid.move(action)
                new_state = grid.current_state()
                V[s] = r + gamma * V[new_state]
                delta = max(delta,abs(old_v - V[s]))
            
            if delta < THETA :
                break

        
        #Policy Improvement
        policy_stable = True
        for s in states:
            if s not in pi:
                continue
            old_action = pi[s]
            max_val = float("-inf")
            for action in grid.actions[s]:
                grid.set_state(s)
                r = grid.move(action)
                new_state = grid.current_state()
                val = r + gamma * V[new_state]
                if val > max_val :
                    max_val = val
                    max_action = action
            pi[s] = max_action
            if old_action != pi[s] :
                policy_stable = False

        if policy_stable == True :
            print_policy(pi,grid)
            break
            
                
    

        
                
                
        
                
    
    
