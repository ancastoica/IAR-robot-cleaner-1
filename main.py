from emulator import Emulator
from random import randrange

# Initialization
emule = Emulator()
episodesnb = 100

# Actual rendering
emule.createmap()

# Simulate the algorithm
for i in range(episodesnb):
    reward = emule.simulate(emule.firstState, emule.actions[randrange(0, len(emule.actions))])
    emule.resetiterationnb()
    print("**************")


# End of simulation
