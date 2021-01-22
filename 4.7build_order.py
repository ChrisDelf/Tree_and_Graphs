
##Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, 
## where the second project is dependent on the first project). All of the a project's dependencies must be built
## before the project is. Find a build order that will allow the projects to be built. If there is no valid build order,
## return an error

## example: input 
## projects: a,b,c,d,e,f
## dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)
## output:f, e, a, b, d, c
import pickle
class projectNode():
    def __init__(self):
        self.parent = []
        self.depen = []
        self.value = None

        
class projectOrder():
    def __init__(self, projects):
        self.root = None
        self.order = None
        self.tail = None
        self.hash = {}
        self.dependant = None
        self.projects = projects
        self.indep = []
    
    def createNodes(self):
        
        for x in  self.projects:
            newNode = projectNode()
            newNode.value = x
            self.hash[newNode.value] = newNode

    def connectProjects(self, data):
        projectsDict = {}
        for x in data:
            if x[0] in self.hash and x[1] in self.hash:
                ## we want to add the dependant nodes to the project
                self.hash[x[0]].depen.append(self.hash[x[1]])
                ## then we want to go the other way to add the parent to the dependant node
                self.hash[x[1]].parent.append(self.hash[x[0]])
            ## we want to find the root and save it for later
            if x[1] not in projectsDict:
                projectsDict[x[1]] = 0
        for x in data:
            if x[0] not in projectsDict:
                self.root = self.hash[x[0]]
        
        self.dependant = projectsDict


    def printOrder(self):
        current = self.root
        result_arr = [self.root.value]
        visited = {}
        stack = []
        for idx in range(0,len(self.root.depen)):
            stack.append(self.root.depen[idx])
       
        visited[self.root.value] = 0 
        
        self.dependant[self.root.value] = 0
        ## this check is required since we have to check for projects that have no connections to any other projects
        if len(self.dependant) != len(self.hash):
            for x in self.projects:
                if x not in self.dependant:
                    newNode = projectNode()
                    newNode.value = x
                    self.indep.append(newNode)
                    result_arr.append(x)
        

        ## now we are going to tranverse the graph
        
        while stack:
            node = stack.pop()
            ## going to need this for the to see if the the nodes parents have been explored
            parent_explored = True
            ## we want to see if we have visited all of the parents
            for idx in range(0, len(node.parent)):
                if node.parent[idx].value in visited:
                    
              
                ## now we have to append the the new depedancies to the stack




                ## if the parent node is not in the visited we keep on moving up the parents path until
                ## we reach one we have visted
                else:
                  
                    ## first we want to reappend the node to our stack
                    stack.append(node)
                    ## next we want to find a node that we have visited
                    current_node = node
                    node = node.parent

                    #while node:
                      
                        #if node not in visited:

                            #stack.append(node)
                            #current_node = node
                            #node = node.parent
                        #else:
                            #node = current_node
                            #visited[node.value] = 0
                            #results_arr.append(node.value)
                            #break
            ## now that we done all the checks we can now append the depens to the stack
            visited[node.value] = 0
            result_arr.append(node.value)
            for idx in range(0, len(node.depen)):
                stack.append(node.depen[idx])
            
