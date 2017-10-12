from dynamic_programming import DP
from monte_carlo import MC
import matplotlib.pyplot as plt

algorithm_choice = ""
while algorithm_choice != "DP" and algorithm_choice != "MC" and algorithm_choice != "QL" and algorithm_choice != "dp" and algorithm_choice != "mc" and algorithm_choice != "ql" and algorithm_choice != "all":
    algorithm_choice = str(input("Choose the algorithm to execute (DP; MC; QL; all) : "))

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
