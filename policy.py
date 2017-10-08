class Policy:
    def __init__(self):
        self.matrix = []

    def get_state_action(self, index):
        if index < len(self.matrix):
            return self.matrix[index][0], self.matrix[index][1]
        else:
            print("Out of bounds when looking for a particular policy")
            return

    def insert_action(self, index, action):
        if index < len(self.matrix):
            policytuple = self.matrix[index]
            policytuple[1] = action
            self.matrix[index] = policytuple
        else:
            print("Out of bounds when inserting an action in policy")
            return

    def insert_state(self, index, state):
        if index < len(self.matrix):
            policytuple = self.matrix[index]
            policytuple[0] = state
            self.matrix[index] = policytuple
        else:
            print("Out of bounds when inserting a state in policy")
            return

    def insert_state_action(self, index, state, action):
        if index < len(self.matrix):
            policytuple = self.matrix[index]
            policytuple[0] = state
            policytuple[1] = action
            self.matrix[index] = policytuple
        else:
            print("Out of bounds when inserting a state and action in policy")
            return

    def init_policy(self, length):
        self.matrix = [[0, 0] for i in range(length)]

    def init_policy_MC(self, length):
        self.matrix = [[0, 0, 0] for i in range(length)]

    def state_exists(self, state):
        index = 0
        while index < len(self.matrix):
            if state == self.matrix[index][0]:
                return index
        return -1

    def get_action_given_state(self, state):
        index = self.state_exists(self,state)
        if index == -1:
            print("State not in policy")
            return
        else:
            return self.matrix[index][1], self.matrix[index][2]

    def update_action_for_state(self, state, new_action, new_reward):
        index = self.state_exists(self,state)
        if index == -1:
            print("State not in policy")
            return
        else:
            self.matrix[index][1] = new_action
            self.matrix[index][2] = new_reward

    def insert_state_action_reward(self, index, state, action, reward):
        if index < len(self.matrix):
            policytuple = self.matrix[index]
            policytuple[0] = state
            policytuple[1] = action
            policytuple[2] = reward
            self.matrix[index] = policytuple
        else:
            print("Out of bounds when inserting a state and action in policy")
            return