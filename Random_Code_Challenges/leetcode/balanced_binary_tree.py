def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # time complexity is going to be O(n) same with memory complexity
    def dfs(root):
        # base case
        # if the root is null then we have a balanced tree
        if root is None:
            return [True, 0]
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        # we are taking the previous nodes to see if they are balanced
        # and we are checking if the differences from current nodes 
        # are balanced
        balanced = (left[0] and right[0] 
                and abs(left[1] - right[1]) <=1)

        height = max(left[1], right[1])
        return [balanced, 1 + height]
    return dfs(root)[0]
