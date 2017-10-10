from dynamic_programming import DP
from monte_carlo import MC
from emulator import Emulator
import matplotlib.pyplot as plt
import api

"""
Tests
"""
# state = api.INITIAL_STATE
# api.printstate(state)
# action = "go_forward_vacuuming"
# emulator = Emulator("MC")
# (r,s,p) = emulator.simulate(state, action)
# api.printstate(s)
# print(r)

"""
Dynamic Programming
"""
# Initialization
DP = DP()
policymatrix = DP.run()

print("Values in Dynamic Programming")
for i in range(len(policymatrix)):
    print(policymatrix[i][2])

"""
Monte Carlo
"""
MC = MC()
q = []

for t in range(10, 100):
    v = MC.run(1000, t)
    q.append(v)

plt.plot(q)
plt.legend("Monte Carlo")
plt.show()
