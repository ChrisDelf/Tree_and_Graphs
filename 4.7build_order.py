
##Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, 
## where the second project is dependent on the first project). All of the a project's dependencies must be built
## before the project is. Find a build order that will allow the projects to be built. If there is no valid build order,
## return an error

## example: input 
## projects: a,b,c,d,e,f
## dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)
## output:f, e, a, b, d, c

class projectNode():
    def __init__(self):
        self.parent = []
        self.depen = []
        self.value = None

        
class projectOrder():
    def __init__(self):
        self.root = None
        self.order = None
        self.tail = None
        self.hash = None
        self.final = {}
        self.projects = {}
        
        
        
    def insertProjects(self, data):
        projectsDict = {}
        for x in data:
            if x[0] not in projectsDict:
                projectsDict[x[0]] = []
                newNode = projectNode()
                newNode.value = x[1]
                projectsDict[x[0]].append(newNode)
             
            else:
                newNode = projectNode()
                newNode.value = x[1]
                projectsDict[x[0]].append(newNode)
        self.hash = projectsDict        
        
    def printResults(self):
        current = self.root
        project_order = []
        stack = []
        stack.append(current.depen)
        
        while stack:
            project_order.append(current.value)
            stack.append(current.depen)
            node = stack.pop()
            current = node
            
            if node[-1] in self.final:
                
                current = self.final[node]
               
 
            
        
        
    def sortProjects(self):
        
        ## its time to look for root project
        ## store the edges to a temp array
        temp_array = self.hash.values()
        
        
        ## want to convert it into a dict for quick look up
        temp_dict = {}
        for x in temp_array:
            for idx in range(0,len(x)):
                if x[idx] not in temp_dict:
                    temp_dict[x[idx].value] = 0
        ## now since we have sort our all the edges we can find which node could be a root
        for x in self.hash:
            if x not in temp_dict:
                newNode = projectNode()
                newNode.value = x
                ## we gotta grab our depencies from the hash we saved earlier
                for idx in range(0, len(self.hash[x])):
                    depen_node = projectNode()
                    newNode.depen.append(self.hash[x][idx])
                self.root = newNode
                break
    
        ## if we still don't have a root this project will fail        
        if self.root == None:
            return False
        
        ## have to start somewhere with our stack why not with the root
        stack = [] 
        
        for x in self.root.depen:
            temp_copy = []
            temp_copy.append(x)
            temp_copy.append(self.root)
            stack.append(temp_copy)
        print(self.hash)
        
        current = self.root
        ##print(stack[0][0].value, stack[0][1].value, stack[0][2].value)
        while stack:
            ## going to create the rest of the nodes by adding poping off this stack
            children = stack.pop()
            
            ## if the node is in our project hash we create the node
            for idx in range(0 , len(children)-1):
                node = children[idx]
                
                if node.value in self.hash:
                    for idx in range(0, len(self.hash[node.value])):
                        node.depen.append(self.hash[node.value][idx])
                       
                    node.parent.append(children[-1])
                    if len(node.depen) < 0:
        
                        temp_arr = []
                        for y in range(0, len(node.depen)):
                            print(node.depen[y].value)
                            temp_arr.append(node.depen[y])
                    temp_copy = []
                    temp_copy.append(self.hash[node.value][idx])
                    temp_copy.append(node)
                    stack.append(temp_copy)
                    
                else:
                    newNode = projectNode()
                    newNode.value = current.depen[0]
                    newNode.depen = None
                    self.hash[node] = None

            self.final[newNode] = 0
        
        ##now we need to create the tail
        
        
        
                    
            
           
            
            
        
        
                
test_pro = projectOrder()

test_pro.insertProjects([["a","d"], ["f","b"], ["b","d"], ["f","a"],["d","c"]])

test_pro.sortProjects()

##test_pro.printResults()
## dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

print(test_pro.root.depen[1].depen[0].depen[0].value)
        
