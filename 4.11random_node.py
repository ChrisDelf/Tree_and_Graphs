## You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen, Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.


class binaryNode():
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

class binaryTree():
  def __init__(self):
    self.root = None
    

  def printTree(self):
    print("<-------",self.root.value, "----->")
    current_n = self.root
    p_stack = [self.root]
    while len(p_stack) != 0:
      print("!!!")
      current_n = p_stack.pop()
      if current_n.left != None:
        print("left", current_n.left.value)
        p_stack.append(current_n.left)
        
      if current_n.right != None:
        print("right", current_n.right.value)
        p_stack.append(current_n.right)

  def insertNode(self, value):

    ## if we don't have a root then we insert the first value as a root
    if self.root is None:
      ## instanitate the root Node   
      new_node = binaryNode(value)
      new_node.value = value
      self.root = new_node
      return
    ## we want to start at the root a go down from there
    current_node = self.root

    while current_node:
      
      ## if the current value is less that input value we left:
      if current_node.value >= value:
        ## if current_node.left is none then we have to create a new node
        if current_node.left == None:
          ## instanitate the new node    
          new_node = binaryNode(value)
          new_node.parent = current_node
          current_node.left = new_node
          return
        ## if we have a value there we want to move to that node    
        else:
          current_node = current_node.left
      
      ## now for the right cases
      else:
       ## if current_node.right is none then we have to create a new node
        if current_node.right == None:
          ## instanitate the new node    
          new_node = binaryNode(value)
          new_node.parent = current_node
          current_node.right = new_node
          return
        ## if we have a value there we want to move to that node    
        else:
          current_node = current_node.right
