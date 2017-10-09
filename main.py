from dynamic_programming import DP
from monte_carlo import MC
import matplotlib.pyplot as plt

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
for t in range(3,10):
    q.append(MC.run(10, t))

plt.plot(q)
plt.legend("Monte Carlo")
plt.show()
