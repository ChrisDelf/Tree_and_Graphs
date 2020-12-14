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
    self.length = 0
    

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
      
  def generateDepthL(self):
    d_list = []
    queue = []
    visited_dic = {}
    for x in range(0, self.depth):
      d_list.append([])
    current_n = self.root
    d_list[0].append(current_n.value)
    print(d_list)
    queue.append(current_n)
    current_n = current_n.left
    print("hello",queue[0].value)
    while queue != None:
     
      x = queue.pop(0)
    
      if x.right != None:
        queue.append(x.right)
        d_list[x.right.depth - 1].append(x.right.value)
      if x.left != None:
        queue.append(x.left)
        d_list[x.left.depth - 1].append(x.left.value)

      if len(queue) == 0:
        break

    return d_list
      ##if current_n.left == None and current_n.rigth == None:

        

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

print("length", b_t.length)

b_t.generateDepthL()
          
