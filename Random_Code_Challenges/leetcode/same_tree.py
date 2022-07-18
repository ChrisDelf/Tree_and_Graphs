def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # going to use a iterative approach for this binary tree
    # going to create two stacks
    tree1 = [p]
    tree2 = [q]
    isSame = True

    while len(tree1) != 0 and len(tree2) != 0 and isSame == True:
           
        node1 = tree1.pop()
        node2 = tree2.pop()
            
            
        if node1 != None and node2 == None:
            return False
        if node1 == None and node2 != None:
            return False
                
        if node1 != None and node2 != None:
            
            if node1.val != node2.val:
                isSame = False
                return isSame
            else:
                tree1.append(node1.left)
                tree1.append(node1.right)
                tree2.append(node2.left)
                tree2.append(node2.right)
            
                    
                
            
                 
    return isSame

def isSameTreeRec(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True

    if not p or not q or p.val != q.val:
        return False


    
    isLeft = isSameTreeRec(p.left, q.left)
    isRight = isSameTreeRec(p.right, q.right)
    
    if isLeft and isRight == True:
        return True


