##4.4 Checked Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is dfined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
##pg 244


class binaryNode():
  def __init__(self,value):
    self.value = value
    self.depth = 0
    self.left = None
    self.right = None

class binaryTree():
  def __init__(self):
    self.root = None
    self.depth = 0
    self.length = 0
    self.right_b = 0
    self.left_b = 0
    
  def insertNode(self, data):
    new_node = binaryNode(data)
    
    
    if self.root == None:
      new_node.depth = 1
      self.root = new_node
      self.length += 1
      return
    current_d = self.root.depth
    current_n = self.root

    while current_n != None:
      
      ## we move right
      if new_node.value > current_n.value:
        if current_n.right == None:
          new_node.depth = current_d + 1
          current_n.right = new_node
          self.length += 1
          if current_d + 1 > self.depth:
            self.depth = current_d + 1
          break
        else:
          current_d += 1
          current_n = current_n.right
      
      if new_node.value < current_n.value:
        if current_n.left == None:
          new_node.depth = current_d + 1
          current_n.left = new_node
          self.length += 1
          if current_d + 1 > self.depth:
            self.depth = current_d + 1
          break
        else:
          current_d += 1
          current_n = current_n.left

  def checkBalanced(self):
    queue = []
    current_n = self.root.right
    queue.append(current_n)
    ## first we are going to check the right side of the tree
    while len(queue) > 0:
      x = queue.pop(0)
      if x.right != None or x.left != None:
        if x.right != None:
          queue.append(x.right)
        if x.left != None:  
          queue.append(x.left)
        self.right_b += 1

    ## now time to check the left side
    current_n = self.root.left

    queue.append(current_n)
    while len(queue) > 0:
      x = queue.pop(0)

    if x.right != None or x.left != None:
        if x.right != None:
          queue.append(x.right)
        if x.left != None:  
          queue.append(x.left)
        self.left_b += 1
    
    if self.right_b != self.left_b:
      return print("Tree is not Balanced")
    else:
      return print("Tree is balanced")








b_t = binaryTree()

b_t.insertNode(10)
b_t.insertNode(3)
b_t.insertNode(2)
b_t.insertNode(6)
b_t.insertNode(9)
b_t.insertNode(7)
b_t.insertNode(15)
b_t.insertNode(13)
b_t.insertNode(16)


b_t.checkBalanced()
