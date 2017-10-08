from dynamic_programming import DP

# Initialization
DP = DP()
policymatrix = DP.run()

# End of simulation
average = 0
for i in range(len(policymatrix)):
    average = average + policymatrix[i][2]

average = average / len(policymatrix)
print("Average performance : ", average)
