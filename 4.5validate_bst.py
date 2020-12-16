##Implement a function to check if a binary tree is a binary search:


class treeNode():
  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

class binaryTree():
  def __init__(self):
    self.root = None
  


  def insert(self, data):
    new_node = treeNode(data)   
    if self.root == None:
      self.root = new_node
      return

    current_node = self.root

    while current_node != None:
      
      if new_node.value > current_node.value:
        if current_node.right == None:
          current_node.right = new_node
          break
        else:
          current_node = current_node.right

      if new_node.value < current_node.value:
        if current_node.left == None:
          current_node.left = new_node
          break
        else:
          current_node = current_node.left

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
  
  def binary_check(self):
    queue = []

    queue.append(self.root)  

    while len(queue) > 0:
      x = queue.pop(0)

      if x.right != None:
        if x.right.value < x.value:
          return False
        else:
          queue.append(x.right)

      if x.left != None:
        if x.left.value > x.value:
          return False
        else:
          queue.append(x.left)     
      return True 

bt = binaryTree()

bt.insert(10)
bt.insert(5)
bt.insert(6)
bt.insert(7)
bt.insert(11)
bt.insert(12)
bt.insert(13)

bt.print_node()

print(bt.binary_check())
