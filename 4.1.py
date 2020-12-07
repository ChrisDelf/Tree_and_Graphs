##4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a route between two nodes.   

class createNode ():
  def __init__(self,value):
    self.value = value
    self.edges = []

  def addEdges(self, edges):
    if edges is None:
      self.edges = None
      return
    for a in edges:
      self.edges.append(a)
  



class nodeGraph():
  def __init__(self):
    self.length = 0
    self.root = None
    self.graph = {}

  def insert(self, data, edges):
    newNode = createNode(data)
    if self.root is None:
      self.root = newNode
    if edges is None:
      newNode.addEdges(None)
      self.graph[newNode.value] = newNode.edges
      return
    if len(edges) > 0:
      newNode.addEdges(edges)
 
      
    self.graph[newNode.value] = newNode.edges



newGraph = nodeGraph()
newGraph.insert(1, [3,4])
newGraph.insert(4, None)
newGraph.insert(3, [2])
newGraph.insert(2, [5])


def routeBetween(node, graph):
  visited = {}
  current = node

  ## doing breath first traversal 
  ## checking to see if the node has any edges
  if current is None or current.edges is None:
    return False
  ## we visit the root node and add the edges to the unvisisted nodes
  visited[current.value] = current.edges
  unvisited = {}
  
  ## adding the edges to unvisited nodes
  for x in current.edges:
    if x not in unvisited:
      unvisited[x] = x
  ## now to visit the unvisited nodes
  while unvisited is not None:
    for x in unvisited:
      if x not in visited:
        
        current.value = x
        print(current.value)
        print(newGraph.graph[4])
        print("!!!!", newGraph.graph[x])
        
        if newGraph.graph[x] is not None and len(current.edges) > 0:

          current.edges = newGraph.graph[x]
          visited[current.value] = current.edges
          for y in current.edges:
            if y not in unvisited:
              unvisited[y] = y
          del unvisited[x]
        else:
          print("if we have no edges", x)
          visited[current.value] = current.edges
          del unvisited[x]
          

        print("visited",visited)
        print(unvisited)
        
  
      

routeBetween(newGraph.root,  newGraph)
