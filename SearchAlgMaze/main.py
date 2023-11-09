import interface as inter
from structure import *


def electAlgorithmToSolve(event):
    algorithm = inter.getAlgorithmName()
    if(algorithm == "BFS"): BFSsearch()
    elif(algorithm == "DFS"): DFSsearch()
    elif(algorithm == "Voraz"): VorazSearch()

def BFSsearch():
    directionsMap = createDirectionsMap()
    # Starting the algorithm
    pq = prioQueue()
    pq.clear()
    pq.insert(node('E', 0, 1, 1))
    while(not(pq.isEmpty())):
        currentNode = pq.pop()
        adjacents = getAdjacents(currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), currentNode.__getattribute__("priority") + 1)
        for adjacent in adjacents:
            if(adjacent.__getattribute__("row") == 13 and adjacent.__getattribute__("column") == 13):
                reconstructPath(directionsMap, adjacent)
                pq.clear()
                return "encontrado"
            if(directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] == None):
                pq.insert(adjacent)
                directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] = adjacent.__getattribute__("step")
    pq.clear()
    return "no encontrado"

def DFSsearch():
    directionsMap = createDirectionsMap()

    # Starting the algorithm
    pq = prioQueue()
    pq.clear()
    pq.insert(node('E', 0, 1, 1))
    while(not(pq.isEmpty())):
        currentNode = pq.last()
        adjacents = getAdjacents(currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), currentNode.__getattribute__("priority") + 1)
        for adjacent in adjacents:
            if(adjacent.__getattribute__("row") == 13 and adjacent.__getattribute__("column") == 13):
                reconstructPath(directionsMap, adjacent)
                pq.clear()
                return "encontrado"
            if(directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] == None):
                pq.insert(adjacent)
                directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] = adjacent.__getattribute__("step")
    pq.clear()
    return "no encontrado"

def VorazSearch():
    directionsMap = createDirectionsMap()

    # Starting the algorithm
    pq = prioQueue()
    pq.clear()
    pq.insert(node('E', distanceManhattan(1, 1), 1, 1))
    while(not(pq.isEmpty())):
        currentNode = pq.pop()
        adjacents = getAdjacents(currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), distanceManhattan(currentNode.__getattribute__("row"), currentNode.__getattribute__("column")))
        for adjacent in adjacents:
            if(adjacent.__getattribute__("row") == 13 and adjacent.__getattribute__("column") == 13):
                reconstructPath(directionsMap, adjacent)
                pq.clear()
                return "encontrado"
            if(directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] == None):
                pq.insert(adjacent)
                directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] = adjacent.__getattribute__("step")
    pq.clear()
    return "no encontrado"


# Adjacent return method
def getAdjacents(row, column, childPriority):
    res = []
    if (column + 1 < 15  and inter.buttons[row][column + 1].cget('bg') != inter.WALLS):
        res.append(node('l', childPriority, row, column + 1))
    if (row + 1 < 15  and inter.buttons[row + 1][column].cget('bg') != inter.WALLS):
        res.append(node('u', childPriority, row + 1, column))
    if (row - 1 >= 0 and inter.buttons[row - 1][column].cget('bg') != inter.WALLS):
        res.append(node('d', childPriority, row - 1, column))
    if (column - 1 >= 0  and inter.buttons[row][column - 1].cget('bg') != inter.WALLS):
        res.append(node('r', childPriority, row, column - 1))
    
    return res


# Reconstruct the path 
def reconstructPath(directionsmap, currentNode):
    for i in range(15):
        for j in range(15):
            if((i != 1 or j != 1) and (i != 13 or j != 13)):
                if(inter.buttons[i][j].cget("bg") != inter.WALLS and directionsmap[i][j] != None):
                    inter.buttons[i][j].config(bg=inter.GENERATED)

    currentRow = currentNode.__getattribute__("row")
    currentColumn = currentNode.__getattribute__("column")
    step = currentNode.__getattribute__("step")
    while(True):
        if(step == 'l'):
            currentColumn -= 1
            currentButton = inter.buttons[currentRow][currentColumn]
        if(step == 'r'):
            currentColumn += 1
            currentButton = inter.buttons[currentRow][currentColumn]
        if(step == 'u'):
            currentRow -= 1
            currentButton = inter.buttons[currentRow][currentColumn]
        if(step == 'd'):
            currentRow += 1
            currentButton = inter.buttons[currentRow][currentColumn]

        step = directionsmap[currentRow][currentColumn]
        if(step == 'E'):
            break
        currentButton.config(bg=inter.ROUTE)
    return 0

def createDirectionsMap():
    # Instance of a map that contains inverted directions to obtain the final path
    directionsMap = []
    for i in range(15):
        directionsMap.append([])
        for j in range(15):
            directionsMap[i].append(None)
    directionsMap[1][1] = 'E'
    return directionsMap


def distanceManhattan(row, column):
    # Goal point: 
    return abs(row - 13) + abs(column - 13)


solveButton = inter.getSolveButoon()
solveButton.bind("<Button-1>", electAlgorithmToSolve)


# Running window

inter.loop()