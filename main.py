from dynamic_programming import DP
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
