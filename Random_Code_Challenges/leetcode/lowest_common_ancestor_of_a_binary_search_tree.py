def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
   # time complexity is going to be o(n)
    current = root

    while current:
    # checking to see what direction we are going in
    if p.val > current.val and q.val > current.val:
            current = current.right
    elif p.val < current.val and q.val < current.val:
            current = current.left
        else:
                
            return current

        
