import numpy as np
import matplotlib.pyplot as plt
from grid_world import standard_grid,negative_grid
from grid_world import textbook_grid_4_1
import random

#Set a threshhold for convergence
theta = 10e-4

def print_values(V,g):
    for i in range(g.width):
        print("-----------------------------------------")
        for j in range(g.height):
            v = V.get((i,j),0)

            if (v >= 0) :
                print(" %.2f|" % v,end = '')
            else :
                print("%.2f|" %v,end = '')
        print("")

#Print the policy (action taken at each state)
#Works only for deterministic policies
def print_policy(P,g) :
    for i in range(g.width):
        print("------------------------------------")
        for j in range(g.height):
            a = P.get((i,j),'')
            print(" %s |" % a,end = '')

        print("")


if __name__ == "__main__":

    grid = negative_grid()
    #grid = textbook_grid_4_1()
    V = {}

    states = grid.all_states()

    
    #Uniform Random Policy
    #Initialize value function to 0 for all states
    for s in states:
        V[s] = 0.0

    #Discount factor
    gamma = 1.0


    
    #Repeat until convergence
    while True:
        delta = 0
        for s in states:
            v = V[s]
            new_v = 0.0
            for action in grid.actions.get(s,()) :
                grid.set_state(s)
                pi =  1/len(grid.actions[s])
                r = grid.move(action)
                s_p = grid.current_state()
                new_v += pi * (r + gamma * V[s_p])
            V[s] = new_v
            delta = max(delta,abs(v - V[s]))
            
        if delta <  theta :
            break

    print_values(V,grid)    


    #Fixed policy

    policy = {
    (2, 0): 'U',
    (1, 0): 'U',
    (0, 0): 'R',
    (0, 1): 'R',
    (0, 2): 'R',
    (1, 2): 'R',
    (2, 1): 'R',
    (2, 2): 'R',
    (2, 3): 'U',
    }
    print_policy(policy, grid)
                
    for s in states:
        V[s] = 0.0

    #Discount factor
    gamma = 0.9


    
    #Repeat until convergence
    while True:
        delta = 0
        for s in states:
            v = V[s]
            new_v = 0.0
            if s in policy : 
                grid.set_state(s)
                action = policy[s]
                r = grid.move(action)
                s_p = grid.current_state()
                new_v += (r + gamma * V[s_p])
            V[s] = new_v
            delta = max(delta,abs(v - V[s]))
            
        if delta <  theta :
            break

    print_values(V,grid)    
            

    
            

        
