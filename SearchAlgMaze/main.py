import interface as inter
from structure import *
import time



def electAlgorithmToSolve(event):
    algorithm = inter.getAlgorithmName()
    inter.clearMethod(0)
    if(algorithm == "BFS"): SearchAlgorithm2("BFS")
    elif(algorithm == "DFS"): SearchAlgorithm2("DFS")
    elif(algorithm == "GREEDY MANHATTAN"): SearchAlgorithm2("GREEDY MANHATTAN")
    elif(algorithm == "A MANHATTAN"): SearchAlgorithm("A MANHATTAN")


def SearchAlgorithm2(type):
    ini = time.time()
    directionsMap = createDirectionsMap()
    pq = prioQueue()
    close = []
    pq.clear()
    if(type == 'BFS' or type == 'DFS'):
        pq.insert(node2(None, 0, 0, 1, 1))
    if(type == 'GREEDY MANHATTAN'):
        pq.insert(node2(None, distanceManhattan(1,1), 0, 1, 1))
    
    while(not(pq.isEmpty())):
        if(type == 'BFS' or type == 'GREEDY MANHATTAN'):
            currentNode = pq.pop()
        if(type == 'DFS'):
            currentNode = pq.last()
        close.append(currentNode)
        if(type == 'BFS' or type == 'DFS'):
            adjacents = getAdjacents2(currentNode, currentNode.__getattribute__("f"), currentNode.__getattribute__("g"), currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), 0)
        if(type == 'GREEDY MANHATTAN'):
            adjacents = getAdjacents2(currentNode, currentNode.__getattribute__("f"), 0, currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), 'A')
        for adjacent in adjacents:
            if(adjacent.__getattribute__("row") == 13 and adjacent.__getattribute__("column") == 13):
                reconstructPath2(directionsMap, adjacent)
                fin = time.time()
                inter.timeValue.config(text=str(round(fin - ini, 5)))
                pq.clear()
                return "encontrado"
            if(directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] == None):
                directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] = 0
                pq.insert(adjacent)
    print("no encontrado")
    return "no encontrado"
            


def getAdjacents2(father, f, g, fatherRow, fatherColumn, type):
    res = []
    if (fatherColumn + 1 < 15  and inter.buttons[fatherRow][fatherColumn + 1].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow, fatherColumn+1), g+1, fatherRow, fatherColumn + 1))
        else:
            res.append(node2(father, g+1, g+1, fatherRow, fatherColumn + 1))
    if (fatherRow + 1 < 15  and inter.buttons[fatherRow + 1][fatherColumn].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow+1, fatherColumn), g+1, fatherRow + 1, fatherColumn))
        else:
            res.append(node2(father, g+1, g+1, fatherRow + 1, fatherColumn))
    if (fatherRow - 1 >= 0 and inter.buttons[fatherRow - 1][fatherColumn].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow-1, fatherColumn), g+1, fatherRow - 1, fatherColumn))
        else:
            res.append(node2(father, g+1, g+1, fatherRow - 1, fatherColumn))
    if (fatherColumn - 1 >= 0  and inter.buttons[fatherRow][fatherColumn - 1].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow, fatherColumn-1), g+1, fatherRow - 1, fatherColumn))
        else:
            res.append(node2(father, g+1, g+1, fatherRow, fatherColumn - 1))
    return res

def reconstructPath2(directionsmap, goal):
    nodesGenerated = 0
    for i in range(15):
        for j in range(15):
            if((i != 1 or j != 1) and (i != 13 or j != 13)):
                if(inter.buttons[i][j].cget("bg") != inter.WALLS and directionsmap[i][j] != None):
                    inter.buttons[i][j].config(bg=inter.GENERATED)
                    nodesGenerated += 1
    inter.nodesGeneratedValue.config(text=str(nodesGenerated))

    currentNode = goal.father
    lengthRoute = 0
    while(currentNode != None):
        currentRow = currentNode.row
        currentColumn = currentNode.column
        currentButton = inter.buttons[currentRow][currentColumn]
        currentButton.config(bg=inter.ROUTE)
        currentNode = currentNode.father
        lengthRoute += 1
    currentButton.config(bg=inter.SPECIAL)
    inter.pathLengthValue.config(text=str(lengthRoute))

def nodeInClosed(close, node):
    for element in close:
        if(node.compare(element)):
            return True
    return False


def SearchAlgorithm(type):
    directionsMap = createDirectionsMap()
    # Starting the algorithm
    maxNodesStored = 1
    pq = prioQueue()
    close = []
    pq.clear()
    if(type == 'BFS'):
        pq.insert(node('E', 0, 1, 1))
    if(type == 'DFS'):
        pq.insert(node('E', 0, 1, 1))
    if(type == 'GREEDY MANHATTAN'):
        pq.insert(node('E', distanceManhattan(1, 1), 1, 1))
    if(type == 'A MANHATTAN'):
        pq.insert(node('E', distanceManhattan(1, 1), 1, 1))
    
    while(not(pq.isEmpty())):
        #Case of every algorithm
        if(type == 'BFS'):
            currentNode = pq.pop()
            close.append(currentNode)
            adjacents = getAdjacents(currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), currentNode.__getattribute__("priority"), 0)
        if(type == 'DFS'):
            currentNode = pq.last()
            close.append(currentNode)
            adjacents = getAdjacents(currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), currentNode.__getattribute__("priority"), 0)
        if(type == 'GREEDY MANHATTAN'):
            currentNode = pq.pop()
            close.append(currentNode)
            adjacents = getAdjacents(currentNode.__getattribute__("row"), currentNode.__getattribute__("column"), 0, 'A')
        #Adjacents
        for adjacent in adjacents:
            if(maxNodesStored < len(pq.elements)):
                maxNodesStored = len(pq.elements)
            if(adjacent.__getattribute__("row") == 13 and adjacent.__getattribute__("column") == 13):
                inter.maxNodesStoredValue.config(text=str(maxNodesStored))
                reconstructPath(directionsMap, adjacent)
                pq.clear()
                return "encontrado"
            if(directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] == None):
            #if(adjacent not in close):
                pq.insert(adjacent)
                directionsMap[adjacent.__getattribute__("row")][adjacent.__getattribute__("column")] = adjacent.__getattribute__("step")

    pq.clear()
    return "no encontrado"


# Adjacent return method, type detects if it is an A algorithm
def getAdjacents(row, column, fatherPriority, type):
    res = []
    if (column + 1 < 15  and inter.buttons[row][column + 1].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node('l', fatherPriority + distanceManhattan(row, column + 1), row, column + 1))
        else:
            res.append(node('l', fatherPriority + 1, row, column + 1))
    if (row + 1 < 15  and inter.buttons[row + 1][column].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node('u', fatherPriority + distanceManhattan(row + 1, column), row + 1, column))
        else:
            res.append(node('u', fatherPriority + 1, row + 1, column))
    if (row - 1 >= 0 and inter.buttons[row - 1][column].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node('d', fatherPriority + distanceManhattan(row - 1, column), row - 1, column))
        else:
            res.append(node('d', fatherPriority + 1, row - 1, column))
    if (column - 1 >= 0  and inter.buttons[row][column - 1].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node('r', fatherPriority + distanceManhattan(row, column - 1), row, column - 1))
        else:
            res.append(node('r', fatherPriority + 1, row, column - 1))
    
    return res


# Reconstruct the path 
def reconstructPath(directionsmap, currentNode):
    nodesGenerated = 0
    for i in range(15):
        for j in range(15):
            if((i != 1 or j != 1) and (i != 13 or j != 13)):
                if(inter.buttons[i][j].cget("bg") != inter.WALLS and directionsmap[i][j] != None):
                    inter.buttons[i][j].config(bg=inter.GENERATED)
                    nodesGenerated += 1
    inter.nodesGeneratedValue.config(text=str(nodesGenerated))

    currentRow = currentNode.__getattribute__("row")
    currentColumn = currentNode.__getattribute__("column")
    step = currentNode.__getattribute__("step")
    lengthRoute = 0
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
        lengthRoute += 1
    inter.pathLengthValue.config(text=str(lengthRoute + 1))
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