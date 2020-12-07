
##4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.   

class createNode ():
  def __init__(self,value):
    self.value = value
    self.edges = []

  def addEdges(self, edges):  
    for a in edges:
      self.edges.append(a)
  



class nodeGraph():
  def __init__(self):
    self.length = 0
    self.root = None

  def insert(self, data, edges):
    newNode = createNode(data)
    if self.root is None:
      self.root = newNode
    print(len(edges))
    if len(edges) >= 0:
      newNode.addEdges(edges)



newGraph = nodeGraph()
newGraph.insert(1, [3,4])
newGraph.insert(3, [2])
newGraph.insert(2, [5])


def routeBetween():
  
