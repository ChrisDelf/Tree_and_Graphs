def stringsRearrangement(inputArray):
    ## going to have to use recusion to be able to a solution
   
    def recusFunc(N, n ,k, edge1, edge2, tab):
        #end case to break the cycle
        if n == (N-1):
            return n
            
        if n == 0:
            ## set converts a array into a dictionary in ascending order
            tab = tab | set([k])
        ## We next remove K from all further perutations
        edge2 = [row[:] for row in edge1]
        for j in range(N):
            edge2[j][k] = False
            edge2[k][j] = False
        max = n
        # Doing a depth first search
        for j in range(N):
            if edge1[k][j]:
                u = recusFunc(N, n+1,j,edge1,edge2,tab)
                if u == (N-1):
                   #breaking out
                   return u
           
            # if we cannot find the solution we go with j
                if j not in tab:
                    v = recusFunc(N,0,j,edge1,edge2,tab)
                    if v == (N-1):
                        return v
                    if v > max:
                        max = v
                if u > max:
                    max = u
        return max
    
    N = len(inputArray)
    edge1 = [[False]*N for i in range(N)]
    
    for j in range(N-1):
        for i in range(j+1, N):
            x = sum(u != v for u, v in zip(inputArray[i],inputArray[j]))
            edge1[i][j] = (x == 1)
            edge1[j][i] = (x == 1)  
    degOne = set()
    ## we can only have one degree of change  
    for i in range(N):
        s = sum(edge1[i])
        if s == 0:
            return False
        if s == 1:
            degOne = degOne | set([i])
    if len(degOne) > 2:
        return False
    tab = set() if len(degOne) == 0 else set(range(N)) - degOne
    
    p = recusFunc(N, 0, 0, edge1,edge1, tab)
    
    return (N-1) == p
                
        
