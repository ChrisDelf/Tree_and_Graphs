##4.6 Successor: Write an algorithm to find the "next" node (i.e, in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent

class binaryNode():
  def __init__(self,value):
    self.value = value
    self.depth = 0
    self.left = None
    self.right = None
    self.parent = None

class binaryTree():
  def __init__(self):
    self.root = None
    self.depth = 0
    self.length = 0
    self.right_b = 0
    self.left_b = 0
  
  def inorderT(self):
    stack = []
    visited = {}
    current = self.root
    stack.append(current.value)
    visited[self.root] = 0
    current = current.left
    visited[current] = 0
    stack.append(current.value)
    counter = 0
    ##while visited.length < self.length:
    while counter < 6:
      print("current value:", current.left.value)
      if current.left != None or current.right != None:
        
        if current.left != None:
          if current.left not in visited:
            visited[current.left] = 0
            stack.append(current.left.value)
            current = current.left
            print(current.value)
        if current.left == None:
           print("left is none", current.value)
           if current.parent.right not in visited:
            visited[current.parent.right] = 0
            if current.parent.right != None:
              stack.append(current.parent.right.value)
              current = current.parent.right
            else:
              break
           else:
             current = current.parent.right
             print("derp")
        
        

      
        if current.right != None:
        
          
          if current.right not in visited:
            visited[current.right] = 0
            stack.append(current.right.value)
            current = current.right
    
            
        else:
           
           if current.parent.left not in visited:
            visited[current.parent.left] = 0
            stack.append(current.parent.left.value)
            current = current.parent.left
           else:
             current = current.parent.left
      
      
              
      
        
        
      counter +=1

    print(stack)


      

  def print_node(self):
    queue = []

    queue.append(self.root)

    print(self.root.value)

    while len(queue) > 0:
      x = queue.pop(0)
   
      if x.right != None:
        print(x.right.value)
        queue.append(x.right)

      if x.left != None:
        print(x.left.value)
        queue.append(x.left)      

    
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
          new_node.parent = current_n
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
          new_node.parent = current_n
          current_n.left = new_node
          self.length += 1
          if current_d + 1 > self.depth:
            self.depth = current_d + 1
          break
        else:
          current_d += 1
          current_n = current_n.left

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

b_t.inorderT()

b_t.print_node()


