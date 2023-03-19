import pandas as pd

matrix = pd.read_csv("data/minpathsum_matrix.txt", sep=",", header=None)

def naiveOptiPath(matrix, stepsAllowed):
    steps = []
    costs = []
    pos = [0,0]
    goal=[len(matrix[0])-1, len(matrix)-1]
    for i in range(sum(goal)):
        if pos == goal: return steps

        cost = {}
        for dX,dY in stepsAllowed:
            # print(pos)
            # print(dX,dY)
            # print(f"{pos[0]+dX}, {pos[1]+dY}")
            # print("---")
            if 0 <= pos[0]+dX <= goal[0] and 0 <= pos[1]+dY <= goal[1]:
                cost[matrix[pos[1]+dY][pos[0]+dX]] = [pos[0]+dX, pos[1]+dY]

        steps.append(cost[min(cost)])
        costs.append(min(cost))

        pos = cost[min(cost)]
    
    return steps, costs

def naiveOptiPath2(matrix, stepsAllowed, goal, pos=[0,0]):
    steps = []
    costs = []
    
    if pos == goal: return [], 0

    for i,(dX,dY) in enumerate(stepsAllowed):
        if 0 <= pos[0]+dX <= goal[0] and 0 <= pos[1]+dY <= goal[1]:
            steps1, costs1 = naiveOptiPath2(matrix, stepsAllowed, goal, [pos[0]+dX, pos[1]+dY])
            steps.append(steps1)
            costs.append(costs1)

    return [pos] + steps[costs.index(min(costs))], min(costs)+matrix[pos[1]][pos[0]]


stepsAllowed = [(1,0), (0,1)]
goal=[len(matrix[0])-1, len(matrix)-1]

steps, costs = naiveOptiPath(matrix, stepsAllowed)#, goal)

viz = [
    ["1" if [a,i] in steps else "0" for i in range(80)]
    for a in range(80)
]
# print(steps)
print("\n".join(["".join(r) for r in viz]))


