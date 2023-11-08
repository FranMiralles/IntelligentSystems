# Representation of nodes
class node:
    def __init__(self, step, priority, row, column):
        self.step = step # 'u', 'd', 'l', 'r' => up, down, left, right
        self.priority = priority
        self.row = row
        self.column = column
    def toString(self):
        return self.step + str(self.priority) + str(self.row) + str(self.column)
    

# Representation of a priority queue
class prioQueue:
    elements = []

    def insert(self, element):
        for existing_element in self.elements:
            if element == existing_element:
                return
        for i in range(len(self.elements)):
            if element.priority <= self.elements[i].priority:
                self.elements.insert(i, element)
                return
        self.elements.append(element)

    def getElements(self):
        return [element.toString() for element in self.elements]

    def pop(self):
        # Removes first element
        return self.elements.pop(0)
    
    def last(self):
        # Removes last element
        return self.elements.pop()

    def isEmpty(self):
        return len(self.elements) == 0
    
    def clear(self):
        self.elements = []