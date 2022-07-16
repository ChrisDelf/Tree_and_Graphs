def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
  #recursive solution
    if not root:
        return None

    # swap the childern
    temp = root.left
    root.left = root.right
    root.right = temp

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root

