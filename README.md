Artificial Intelligence Project - Homework 1

To execute the project :


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


État initial
    Home base :
    Position x = 0
    Position y = 0
    Robot :
    Position x = 0
    Position y = 0
    Battery = 100
    Orientation = 1


Etat
    L’état est constitué de plusieurs sous paramètres :
    Position du robot sur la carte { x  [0, length of map], y  [0, height of map] }
    Orientation du robot  { 0 (N), 1 (E), 2 (S), 3 (O) }
    Batterie du robot { Batterie suffisante, batterie critique (10%), batterie vide }
    Propreté de chaque cellule de la carte  { 0 (propre), 1 (sale) }
    Position de la homebase{ x  [0, length of map], y  [0, height of map] }

Actions du robot
    {
    Aspirer sans bouger
    Avancer sans aspirer
    Avancer en aspirant
    Rotation +90°
    Rotation -90°
    Charger
    }
