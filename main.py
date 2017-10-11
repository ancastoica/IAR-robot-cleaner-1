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

"""
Monte Carlo
"""
"""
# Initialization
MC = MC()
MC.run(10000)

# End of simulation
plt.plot(MC.tuple_plot_x, MC.tuple_plot_y)
plt.legend("Monte Carlo")
plt.show()
"""
