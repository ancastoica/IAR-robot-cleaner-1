from dynamic_programming import DP
from monte_carlo import MC
import matplotlib.pyplot as plt
import numpy as np


"""
Dynamic Programming
"""
# Initialization
DP = DP()
averageperf = DP.run()

# End of simulation
x = np.linspace(0, 1, len(averageperf))
plt.plot(x * 1000, averageperf)
plt.legend("Dynamic Programming")
plt.show()


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
