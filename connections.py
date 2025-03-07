class Node:
    
    #Class constructor
    def __init__(self, id):
        self.id = id

    #Equivalent to "toString" method in Java
    def __str__(self):
        return "Node Id: "+str(id)
    
class CustomGraph:

    def __init__(self, nUsers):
        self.n = nUsers
        self.network = {}

        """
        Plan to Store the Graph as a HashMap of List (in terms of JAVA)
        HashMap<Integer, List<Node>>
        """
    
    def readGraph(self):
        print("Enter one connection in each line eg: x y")
        while True:
            nodes = list(map(lambda id: Node(int(id)) ,input().split(" ")))
            
            if nodes[0].id == -1 and nodes[1].id == -1:
                break
            
            #creating a bi-directional edge/connection
            self.network.setdefault(nodes[0].id, []).append(nodes[1])
            self.network.setdefault(nodes[1].id, []).append(nodes[0])

    def nodesAtLevelN(self, source, level):
        visited = {}
        currList = [source]
        return self._findNodesHelper(currList, 0, level, visited)

    def _findNodesHelper(self, currList, currLvl, tgtLvl, visited):
        if currLvl == tgtLvl:
            # print("Final List: ", currList)
            return currList
            
        # print("Current List: ", currList)
        # print(visited)
        
        childNodes = []
        for id in currList:
            connections = self.network[id]
            unvisitedConns = list(filter(lambda node: not visited.get(node.id, False), connections))
            unvIDs = list(map(lambda node: node.id, unvisitedConns))
            # print("Unvisited IDs of ", id, ": " ,unvIDs)
            childNodes.extend(unvIDs)
            visited[id] = True
        
        # print("ChildNodes lvl: ", currLvl, ": ", childNodes)
        return self._findNodesHelper(childNodes, currLvl+1, tgtLvl, visited)

    #Just for testing
    def staticGraph(self):
        self.network[1] = [Node(2), Node(4)]
        self.network[2] = [Node(1),Node(3), Node(5)]
        self.network[3] = [Node(2)]
        self.network[4] = [Node(1)]
        self.network[5] = [Node(2)]

    def __str__(self):
        toDisplay = ""
        for id in self.network.keys():
            toDisplay += str(id) + "--> " + ', '.join(map(lambda node: str(node.id), self.network[id])) + "\n"

        return toDisplay+"\n"

if __name__ == '__main__':
    nUsers = int(input("Enter the no. of nodes"))
    g = CustomGraph(nUsers)
    g.readGraph()
    # g.staticGraph()
    # lvlNNodes = g.nodesAtLevelN(1, 2)
    
    src, lvl = list(map(int, input("Enter source and level (space separated): ").split()))
    lvlNNodes = g.nodesAtLevelN(src, lvl)
    
    print("Nodes at level ",lvl,"From Node: ",src,"are: ", lvlNNodes)

