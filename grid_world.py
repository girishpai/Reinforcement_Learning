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
        assert(self.current_state() in self.all_states)

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
        assert(self.current_state() in self.all_states)
                

    def game_over(self):
        return self.current_state not in self.actions

    def all_states(self):
        return set(self.actions.keys() + self.rewards.keys())
    


        
        
