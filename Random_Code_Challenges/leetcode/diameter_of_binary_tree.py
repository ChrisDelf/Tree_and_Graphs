def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # going to use recusion

    # going to set a global variable
    res = [0]

    # doing a depth first search
    def dfs(node):
        # need the exit case

        if node is None:
            return -1

        #now we move the left and right nodes
        right = dfs(node.right)
        left = dfs(node.left)
        
        # storing the the maxium value
        res[0] = max(res[0], 2 + right + left)
        
        # setting the height
        return 1+ max(left, right)
    dfs(root)

    return res[0]
