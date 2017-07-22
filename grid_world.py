#Grid world for running algorithms of reinforcement learning

class Grid:
    
    def __init__(self,width,height,start):
        self.width = width
        self.height = height
        self.i = start[0]
        self.j = start[1]

    def set(self,rewards,actions):
        self.rewards = rewards # Dict of possible rewards for each state (i,j) : r
        self.actions = actions # dict of possible actions for each state (i,j) : a ('U','D','L','R')

    def set_state(self,s):
        self.i = s[0]
        self.j = s[1]

    def current_state(self):
        return (self.i,self.j)

    def is_terminal(self,s):
        return s not in self.actions

    def move(self,action):
        if action in self.actions[self.current_state()] :
            if action == 'U':
                self.i -= 1
            elif action == 'D':
                self.i += 1
            elif action == 'L':
                self.j -= 1
            elif action == 'R':
                self.j += 1

        return self.rewards.get(self.current_state(),0)

    def undo_move(self,action):
        if action in self.actions[self.current_state()] :
            if action == 'U':
                self.i += 1
            elif action == 'D':
                self.i -= 1
            elif action == 'L':
                self.j += 1
            elif action == 'R':
                self.j -= 1
        assert(self.current_state() in self.all_states())
                

    def game_over(self):
        return self.current_state not in self.actions

    def all_states(self):
        return set(list(self.actions.keys()) + list(self.rewards.keys()))


"""

The grid looks like the following

.  .  .  1
.  x  . -1
s  .  .  .

x --> Location not acessible
s --> Start position
Number indicates reward. 
Effectively position (0,3) is Goal State for this grid. 

"""
def standard_grid():
    g = Grid(3,4,(2,0))
    rewards = {(0,3) : 1, (1,3):-1}
    actions = {
        (0,0) : ('D','R'),
        (0,1) : ('L','R'),
        (0,2) : ('L','R','D'),
        (1,0) : ('U','D'),
        (1,2) : ('U','D','R'),
        (2,0) : ('U','R'),
        (2,1) : ('L','R'),
        (2,2) : ('U','L','R'),
        (2,3) : ('L','U')
        }

    g.set(rewards,actions)
    return g


def negative_grid(step_cost = -0.1):
    g = standard_grid()
    rewards = {}
    for i in range(g.width):
        for j in range(g.height):
            rewards[(i,j)] = step_cost

    rewards[(0,3)] = 1
    rewards[(1,3)] = -1
    rewards.pop((1,1),None)
    g.set(rewards,g.actions)
    return g
'''
Grid from Sutton and Batro Example 4.1

G  .  .  .
.  .  .  .
.  .  .  .
.  .  .  G

All states immediate reward = -1. 
G = goal states (self absorbing). 

'''
def textbook_grid_4_1():
    g = Grid(4,4,(3,0))
    rewards = {}
    for i in range(g.width):
        for j in range(g.height):
            rewards[(i,j)] = -1.0
    
    actions = {
        (0,1) : ('L','D','R'),
        (0,2) : ('L','R','D'),
        (0,3) : ('L','D'),
        (1,0) : ('U','R','D'),
        (1,1) : ('U','D','R','L'),
        (1,2) : ('U','D','R','L'),
        (1,3) : ('U','D','L'),
        (2,0) : ('U','R','D'),
        (2,1) : ('L','R','U','D'),
        (2,2) : ('U','L','R','D'),
        (2,3) : ('L','U','D'),
        (3,0) : ('U','R'),
        (3,1) : ('L','R','U'),
        (3,2) : ('U','L','R')
        }

    g.set(rewards,actions)
    return g
    
    
    


        
        
