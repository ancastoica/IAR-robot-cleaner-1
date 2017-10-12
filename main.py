from dynamic_programming import DP
from monte_carlo import MC
from emulator import Emulator
import matplotlib.pyplot as plt
import api


algorithm_choice = ""
while algorithm_choice != "DP" or algorithm_choice != "MC" or algorithm_choice != "QL" or algorithm_choice != "dp" or algorithm_choice != "mc" or algorithm_choice != "ql" or algorithm_choice != "all":
    algorithm_choice = input("Choose the algorithm to execute (DP; MC; QL; all) : ")

if algorithm_choice == "DP" or algorithm_choice == "dp":
    """
    Dynamic Programming
    """
    # Initialization
    DP = DP()
    v_s0 = DP.run()
    print("The performance of Dynamic Programming is : ", v_s0)


elif algorithm_choice == "MC" or algorithm_choice == "mc":
    """
    Monte Carlo
    """
    MC = MC()
    q = []

    for t in range(10, 100):
        v = MC.run(10000, t)
        print(v)
        q.append(v)

    plt.plot(q)
    plt.legend("Monte Carlo")
    plt.show()

elif algorithm_choice == "QL" or algorithm_choice == "ql":
    print("Q-Learning algorithm in construction, please wait for the developper !")

elif algorithm_choice == "all":
    """
    Dynamic Programming
    """
    # Initialization
    DP = DP()
    v_s0 = DP.run()
    print("The performance of Dynamic Programming is : ", v_s0)

    """
    Monte Carlo
    """
    MC = MC()
    q = []

    for t in range(10, 100):
        v = MC.run(10000, t)
        print(v)
        q.append(v)

    plt.plot(q)
    plt.legend("Monte Carlo")
    plt.show()

    """
    Q-Learning
    """
    print("Q-Learning algorithm in construction, please wait for the developper !")
