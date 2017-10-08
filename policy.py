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
            self.matrix[index][1] = action
        else:
            print("Out of bounds when inserting an action in policy")
            return

    def insert_state(self, index, state):
        if index < len(self.matrix):
            self.matrix[index][0] = state
        else:
            print("Out of bounds when inserting a state in policy")
            return

    def insert_state_action(self, index, state, action):
        if index < len(self.matrix):
            self.matrix[index][0] = state
            self.matrix[index][1] = action
        else:
            print("Out of bounds when inserting a state and action in policy")
            return

    def init_policy(self, length):
        self.matrix = [(0, 0) for i in range(length)]
