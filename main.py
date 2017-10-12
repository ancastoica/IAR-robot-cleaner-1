from dynamic_programming import DP
from monte_carlo import MC
from emulator import Emulator
import matplotlib.pyplot as plt
import api

"""
Dynamic Programming
"""
# Initialization
DP = DP()
policymatrix = DP.run()

print("Values in Dynamic Programming")
for i in range(len(policymatrix)):
    print(policymatrix[i][2])
v_s0 = DP.run()
print("The performance of Dynamic Programming is : ", v_s0)

"""
Monte Carlo
"""
MC = MC()
q = []

for t in range(1, 100):
    v = MC.run(100, t)
    print("Value of Q_function for s0 when episode length = ", t, ": ", v)
    q.append(v)

plt.plot(q)
plt.legend("Monte Carlo")
plt.show()
