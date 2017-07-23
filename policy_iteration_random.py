import numpy as np
from grid_world import negative_grid
from iterative_policy_evaluation import print_values,print_policy

THETA = 1e-3
gamma = 0.9
ALL_ACTIONS = ('U','D','L','R')

#This has stochastic state transitions for given action
#It will be implemented giving a 0.5 probablity to the intended action and distribute equally the remaining prob
# to the other actions
# p(s',r'|s,a_intended) = 0.5
# p(s',r'|s,a_remaining) = 0.5 / (total number of remaining actions)


if __name__ == "__main__" :
    grid = negative_grid(step_cost = -1.0)

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

                old_v = V[s]
                new_v = 0.0
                for action in ALL_ACTIONS:
                    if action == pi[s]:
                        prob = 0.5
                    else :
                        prob = 0.5 / (len(ALL_ACTIONS)-1)
                    grid.set_state(s)
                    r = grid.move(action)
                    new_state = grid.current_state()
                    new_v += prob * (r + gamma * V[new_state])

                V[s] = new_v
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
            for action_chosen in ALL_ACTIONS:
                val = 0.0
                for action_taken in ALL_ACTIONS:
                    if action_taken == action_chosen:
                        prob = 0.5
                    else :
                        prob = 0.5 / (len(ALL_ACTIONS) - 1)
                    grid.set_state(s)
                    r = grid.move(action_taken)
                    new_state = grid.current_state()
                    val += prob * (r + gamma * V[new_state])
                
                if val > max_val :
                    max_val = val
                    max_action = action_chosen
            pi[s] = max_action
            if old_action != pi[s] :
                policy_stable = False

        if policy_stable == True :
            print_policy(pi,grid)
            break
            
                
    

        
                
                
        
                
    
    
