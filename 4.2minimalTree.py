##4.2 Minimal Tree: Given a sorted (inscreasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.  


a1 = [1,2,3,6,7,8,9]

## binary search

class binaryNode():
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

class binaryTree():
  def __init__(self, input_array):
    self.root = None
    self.input_array = input_array


  def generateTree(self):
    temp_a = self.input_array
    if self.input_array is None:
      return
    if len(temp_a) < 0:
      return
    ## need to find our midpoint to create this binary search tree


    mid_point = len(temp_a) % 2
    if mid_point == 1:
      mid_point = round(len(temp_a)/2)
    if mid_point == 0:
      mid_point = (len(temp_a) / 2)
      mid_point = int(mid_point)

    

    mid_point = temp_a[mid_point] -1
    print(mid_point)
    self.root = binaryNode(mid_point)

    i = 0
    ## we are goint to set the roots
    ## goint need to get the midpoint of the left
   
    left_array= temp_a[4:]

    self.root.left = binaryNode(temp_a[-1])
    ##  right

    print(temp_a[-1])
  
    while i < len(self.input_array) - 2:
      i+= 1


bt = binaryTree(a1)
bt.generateTree()
