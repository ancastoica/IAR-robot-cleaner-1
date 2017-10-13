from dynamic_programming import DP
from monte_carlo import MC
from q_learning import QL
import matplotlib.pyplot as plt

EPISODE = 100

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

    plt.plot([v_s0 for i in range(10000)])
    plt.legend("Dynamic Programming")
    plt.show()
    print("The performance of Dynamic Programming is : ", v_s0)


elif algorithm_choice == "MC" or algorithm_choice == "mc":
    """
    Monte Carlo
    """
    MC = MC()
    q = []

    for t in range(0, EPISODE):
        v = MC.run(100, t)
        q.append(v)

    plt.plot(q)
    plt.legend("Monte Carlo")
    plt.show()

elif algorithm_choice == "QL" or algorithm_choice == "ql":
    """
    Q-Learning
    """
    QL = QL()
    ql = []

    i = 0
    while i < EPISODE:
        v = QL.run(i)
        ql.append(v)
        i += 1

    plt.plot(ql)
    plt.legend("Q-Learning")
    plt.show()

elif algorithm_choice == "all":
    """
    Dynamic Programming
    """
    plt.plot([4.7 for i in range(EPISODE)])

    """
    Monte Carlo
    """
    MC = MC()
    q = []

    for t in range(0, EPISODE):
        v = MC.run(EPISODE, t)
        q.append(v)

    plt.plot(q, label='MC')

    """
    Q-Learning
    """
    QL = QL()
    ql = []

    i = 0
    while i < EPISODE:
        v = QL.run(i)
        ql.append(v)
        i += 1

    plt.plot(ql, label='QL')
    plt.show()
