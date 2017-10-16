Artificial Intelligence Project - Homework 1

To execute the project :

Execution :
    In the main, you'll be asked to choose one of the 3 algorithms, or all three.
    >>> "Choose the algorithm to execute (DP; MC; QL; all) : "
    To get an idea of the computing time :
        - DP : ~ 5h
        - MC : ~ 3 min
        - QL : ~ 3 min
    In order to facilitate the execution, we ran the DP algorithm many times, averaged the results, and when choosing "all" algorithm,
    the plot of the DP will be the plot of this value, and not a complete recomputation of the performance.



Project Structure :
    main.py: Run the algorithms
    emulator.py: The simulator which simulates the environment given a state and an action, which returns a reward, a probability and a next possible state (MC, TD) / a list of possible states (DP)
    robot.py: The actual robot with its position, battery and orientation
    cell.py: The cell with its dirtiness states
    state.py: The state with the map, the robot parameters and the home base position
    policy.py: The policy which can be improved (tuples of states and optimal actions)
    api.py: The api of the project
    dynamic_programming.py: The dynamic programming algorithm
    monte-carlo.py: The monte-carlo algorithm
    qLearning.py: The Q learning algorithm


Initial state
    Home base :
    Position x = 0
    Position y = 0
    Robot :
    Position x = 0
    Position y = 0
    Battery = 100
    Orientation = 1


States
    The state is composed of multiple parametres:
    Robot position { x  [0, length of map], y  [0, height of map] }
    Robot orientation  { 0 (N), 1 (E), 2 (S), 3 (O) }
    Robot battery { sufficient, critical (10%), empty}
    Status of each cell { 0 (clean), 1 (dirty) }
    Homebase position { x  [0, length of map], y  [0, height of map] }

Robot actions
    {
    Vacuum
    Go forward vacuuming
    Go forward no vacuum
    Rotation +90°
    Rotation -90°
    Recharge
    }
