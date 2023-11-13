import interface as inter
from structure import *
import time



def electAlgorithmToSolve(event):
    algorithm = inter.getAlgorithmName()
    inter.clearMethod(0)
    if(algorithm == "BFS"): SearchAlgorithm("BFS")
    elif(algorithm == "DFS"): SearchAlgorithm("DFS")
    elif(algorithm == "GREEDY MANHATTAN"): SearchAlgorithm("GREEDY MANHATTAN")
    elif(algorithm == "A MANHATTAN"): SearchAlgorithm("A MANHATTAN")


def SearchAlgorithm(type):
    directionsMap = createDirectionsMap()
    pq = prioQueue()
    close = []
    pq.clear()
    ini = time.time()
    if(type == 'BFS' or type == 'DFS'):
        pq.insert(node2(None, 0, 0, 1, 1))
    if(type == 'GREEDY MANHATTAN' or type == 'A MANHATTAN'):
        pq.insert(node2(None, distanceManhattan(1,1), 0, 1, 1))
    
    while(not(pq.isEmpty())):
        if(type == 'BFS' or type == 'GREEDY MANHATTAN' or type == 'A MANHATTAN'):
            currentNode = pq.pop()
        if(type == 'DFS'):
            currentNode = pq.last()

        close.append(currentNode)
        if(type == 'BFS' or type == 'DFS'):
            adjacents = getAdjacents(currentNode, currentNode.f, currentNode.g, currentNode.row, currentNode.column, 0)
        if(type == 'GREEDY MANHATTAN'):
            adjacents = getAdjacents(currentNode, currentNode.f, 0, currentNode.row, currentNode.column, 'A')
        if(type == 'A MANHATTAN'):
            adjacents = getAdjacents(currentNode, currentNode.f, currentNode.g, currentNode.row, currentNode.column, 'A')
        for adjacent in adjacents:
            if(adjacent.row == 13 and adjacent.column == 13):
                reconstructPath(directionsMap, adjacent)
                fin = time.time()
                inter.timeValue.config(text=str(round(fin - ini, 5)))
                pq.clear()
                return "encontrado"
            if(directionsMap[adjacent.row][adjacent.column] == None):
                directionsMap[adjacent.row][adjacent.column] = 0
                pq.insert(adjacent)
            #Re-expansion
            else:
                closed = elementInList(close, adjacent)
                if(None != closed):
                    if(adjacent.f < closed.f):
                        close.remove(closed)
                        pq.insert(adjacent)
                else:
                    opened = elementInList(pq.elements, adjacent)
                    if(None != opened):
                        if(adjacent.f < opened.f):
                            pq.elements.remove(opened)
                            pq.insert(adjacent)
                    

    print("no encontrado")
    return "no encontrado"
            

def getAdjacents(father, f, g, fatherRow, fatherColumn, type):
    res = []
    if (fatherColumn + 1 < 15  and inter.buttons[fatherRow][fatherColumn + 1].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow, fatherColumn+1) + g, g+1, fatherRow, fatherColumn + 1))
        else:
            res.append(node2(father, g+1, g+1, fatherRow, fatherColumn + 1))
    if (fatherRow + 1 < 15  and inter.buttons[fatherRow + 1][fatherColumn].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow+1, fatherColumn) + g, g+1, fatherRow + 1, fatherColumn))
        else:
            res.append(node2(father, g+1, g+1, fatherRow + 1, fatherColumn))
    if (fatherRow - 1 >= 0 and inter.buttons[fatherRow - 1][fatherColumn].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow-1, fatherColumn) + g, g+1, fatherRow - 1, fatherColumn))
        else:
            res.append(node2(father, g+1, g+1, fatherRow - 1, fatherColumn))
    if (fatherColumn - 1 >= 0  and inter.buttons[fatherRow][fatherColumn - 1].cget('bg') != inter.WALLS):
        if(type == 'A'):
            res.append(node2(father, distanceManhattan(fatherRow, fatherColumn-1) + g, g+1, fatherRow, fatherColumn - 1))
        else:
            res.append(node2(father, g+1, g+1, fatherRow, fatherColumn - 1))
    return res

def reconstructPath(directionsmap, goal):
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


def elementInList(list, node):
    for element in list:
        if(node.compare(element)):
            return node
    return None

def createDirectionsMap():
    # Instance of a map that contains inverted directions to obtain the final path
    directionsMap = []
    for i in range(15):
        directionsMap.append([])
        for j in range(15):
            directionsMap[i].append(None)
    directionsMap[1][1] = 'E'
    return directionsMap


# In A algorithms, g has few weight, so distanceManhattan is /5 to lower its influence
def distanceManhattan(row, column):
    # Goal point: 
    return (abs(row - 13) + abs(column - 13))/5


solveButton = inter.getSolveButoon()
solveButton.bind("<Button-1>", electAlgorithmToSolve)


# Running window

inter.loop()