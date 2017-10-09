from dynamic_programming import DP
from monte_carlo import MC
import matplotlib.pyplot as plt
import numpy as np


"""
Dynamic Programming
"""
# Initialization
DP = DP()
policymatrix = DP.run()

print("Values in Dynamic Programming")
for i in range(len(policymatrix)):
    print(policymatrix[i][2])


# """
# Monte Carlo
# """
# # Initialization
# MC = MC()
# MC.run(1000000)
#
# # End of simulation
# plt.plot(MC.tuple_plot_x, MC.tuple_plot_y)
# plt.legend("Monte Carlo")
# plt.show()
