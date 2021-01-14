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
        self.parent = None
        self.depen = []
        self.value = None

        
class projectOrder():
    def __init__(self):
        self.root = None
        self.order = None
        self.tail = None
        self.hash = None
        self.projects = {}
        
        
        
    def insertProjects(self, data):
        projectsDict = {}
        for x in data:
            if x[0] not in projectsDict:
                projectsDict[x[0]] = []
                projectsDict[x[0]].append(x[1])
               ## newPro = projectNode()
               ## newPro.value = x[0]
               ## newPro.depen.append(x[1])
               ## self.projects.add(newPro)
            else:
                projectsDict[x[0]].append(x[1])
        self.hash = projectsDict        
        print(self.hash)
    def sortProjects(self):
        
        ## its time to look for root project
        ## store the edges to a temp array
        temp_array = self.hash.values()
        print(temp_array)
        ## want to convert it into a dict for quick look up
        temp_dict = {}
        for x in temp_array:
            for idx in range(0,len(x)):
                if x[idx] not in temp_dict:
                    temp_dict[x[idx]] = 0
        ## now since we have sort our all the edges we can find which node could be a root
        for x in self.hash:
            if x not in temp_dict:
                newNode = projectNode()
                newNode.value = x
                ## we gotta grab our depencies from the hash we saved earlier
                newNode.depen = self.hash[x]
                self.root = newNode
                
        ## if we still don't have a root this project will fail        
        if self.root == None:
            return False
        
        current = self.root
        ## have to start somewhere with our stack why not with the root
        stack= self.root.depen
        current = None
        while stack:
            ## going to create the rest of the nodes by adding poping off this stack
            node = stack.pop()
            
            ## if the node is in our project hash we create the node
            if node in self.hash:
                newNode = projectNode()
                newNode.value = node
                newNode.depen = self.hash[node]
                current = newNode
                for idx in range(0, len(newNode.depen)):
                    stack.append(newNode.depen[idx])
        
        ##now we need to create the tail
        newNode = projectNode()
        newNode.value = current.depen[0]
        newNode.depen = None

        
                    
            
           
            
            
        
        
                
test_pro = projectOrder()

test_pro.insertProjects([["a","d"], ["f","b"], ["b","d"], ["f","a"],["d","c"]])

test_pro.sortProjects()
