## List of Depths: Given a binary tree, design an algortimh which creates a linked list of all the nodes at each depth (e.g, if you have a tree with depth D, you'll have D linked Lists)


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
    

  def printTree(self):
    print("-----",self.root,"-------")
    end_loop = False
    current_n = self.root
    prev = None
    p_stack = [self.root]
    while len(p_stack) != 0:
      print("!!!")
      current_n = p_stack.pop()
      if current_n.left != None:
        print("left", current_n.left.value)
        p_stack.append(current_n.left)
        
      if current_n.right != None:
        print("right", current_n.right_value)
        p_stack.append(current_n.right)

  def insertNode(self, data):
    new_node = binaryNode(data)
    
    
    if self.root == None:
      new_node.depth = 1
      self.root = new_node
      return
    current_d = self.root.depth
    current_n = self.root

    while current_n != None:
      
      ## we move right
      if new_node.value > current_n.value:
        if current_n.right == None:
          new_node.depth = current_d + 1
          current_n.right = new_node
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
          if current_d + 1 > self.depth:
            self.depth = current_d + 1
          break
        else:
          current_d += 1
          current_n = current_n.left
      
      

b_t = binaryTree()

b_t.insertNode(5)
b_t.insertNode(3)
b_t.insertNode(2)
b_t.insertNode(4)
b_t.insertNode(1)
b_t.insertNode(6)
b_t.insertNode(9)
b_t.insertNode(7)
b_t.insertNode(10)

print(b_t.depth)
