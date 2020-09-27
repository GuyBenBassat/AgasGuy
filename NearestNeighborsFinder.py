class RunScore:
    def __init__(self, armyId, minutes,  seconds, miliSeconds):
        self.armyId = armyId
        self.minutes = minutes
        self.seconds = seconds
        self.miliSeconds = miliSeconds

    def __lt__(self, other):
        return self.minutes < other.minutes or self.seconds < other.seconds or self.miliSeconds < other.miliSeconds

def mapUserToNeighbors(allUsersRunScores, numberOfNeighbors = 4):
    allUsersRunScores.sort()
    radius = int(numberOfNeighbors/2)
    numberOfScores = len(allUsersRunScores)
    userToNeighborsMap = {}

    # Find neighbors for the first #radius Ids
    for i in range(radius):
        armyId = allUsersRunScores[i].armyId
        neighbors = []
        for x in range(i):
            neighbors += {allUsersRunScores[x].armyId}

        neighborsFromRight = numberOfNeighbors - i
        for j in range(i + 1, i + 1 + neighborsFromRight):
            neighbors += {allUsersRunScores[j].armyId}

        userToNeighborsMap[armyId] = neighbors

    # Get neighbors of all the Ids that have radius neighbors
    # that are bigger than them and radius neighbors that are smaller
    # than them.
    for i in range(radius, numberOfScores - radius):
        armyId = allUsersRunScores[i].armyId
        neighbors = []
        for j in range(i-radius, i):
            neighbors += {allUsersRunScores[j].armyId}
        for j in range(i+1, i+1+radius):
            neighbors += {allUsersRunScores[j].armyId}
        userToNeighborsMap[armyId] = neighbors

    # Find neighbors for the last #radius Ids
    for i in range(numberOfScores-radius, numberOfScores):
        armyId = allUsersRunScores[i].armyId
        neighbors = []
        neighborsFromRight = numberOfScores - (i+1)
        neighborsFromLeft = numberOfNeighbors - neighborsFromRight

        for j in range(i - neighborsFromLeft, i):
            neighbors += {allUsersRunScores[j].armyId}

        for x in range(i+1, i + neighborsFromRight+1):
            neighbors += {allUsersRunScores[x].armyId}

        userToNeighborsMap[armyId] = neighbors

    return  userToNeighborsMap

if __name__ == '__main__':
    runScore1 = RunScore(1, 1, 2, 3)
    runScore2 = RunScore(2, 2, 2, 4)
    runScore3 = RunScore(3, 2, 2, 5)
    runScore4 = RunScore(4, 3, 2, 5)
    runScore5 = RunScore(5, 4, 2, 5)
    runScore6 = RunScore(6, 4, 2, 6)
    runScore7 = RunScore(7, 4, 2, 7)
    runScore8 = RunScore(8, 4, 2, 8)
    runScores = [runScore5, runScore4, runScore1, runScore6, runScore2, runScore3,runScore7,runScore8]

    print(mapUserToNeighbors(runScores,6))

    for runScore in runScores:
        print(runScore.armyId),
    runScores.sort()
    for runScore in runScores:
        print(runScore.armyId),