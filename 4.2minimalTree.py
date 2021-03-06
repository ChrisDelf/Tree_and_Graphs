##4.2 Minimal Tree: Given a sorted (inscreasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.  
import random

a1 = [1,2,3,6,7,8,9,10,11,12,13,15,16]

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

    
    pivot = mid_point
    mid_point = temp_a[mid_point] -1
    
    self.root = binaryNode(mid_point)

    i = 0
    ## we are goint to set the roots
    ## goint need to get the midpoint of the left

    right_array= temp_a[pivot:]

  
    ## getting the left side mide point
    right_midpoint = len(right_array) % 2
    if  right_midpoint == 1:
      right_midpoint = round(len(right_array)/2)
    if  right_midpoint == 0:
      right_midpoint = (len (right_array) / 2)
      right_midpoint = int(right_midpoint)

   

    ##  right
    left_array = temp_a[:pivot]
    left_array.pop()
 

    left_midpoint = len(left_array) % 2

    if left_midpoint == 1:
      left_midpoint = round(len(left_array)/2)
    if left_midpoint == 0:
      left_midpoint = (len(left_array)/2)
      left_midpoint = int(left_midpoint)
  

 

    ## going to irrerate through right side and rearrange the array:
    temp_x = []
    dup_check = {}
    ## selecting the mid points for the right side
    for x in range(len(right_array)-2, 0, -2):
      temp_x.append(right_array[x])
      dup_check[right_array[x]] = 0
    

    for x in range(0, len(right_array)):
      if right_array[x] not in dup_check:
        temp_x.append(right_array[x])
    
    

    ##going to do the same to the left side
    temp_y = []
    for x in range(len(left_array)-2, 0, -2):
      temp_y.append(left_array[x])
      dup_check[left_array[x]] = 0
 

    for x in range(0, len(left_array)):
      if left_array[x] not in dup_check:
        temp_y.append(left_array[x])


    join_array = temp_x + temp_y
    
    
    print(join_array)
    for x in range(0, len(join_array)):
      selected_node = join_array[x]
      current_node = self.root
      print(selected_node)
      
      while selected_node:
        print(join_array)
        print("current", current_node.value)
        print("selected", selected_node)
        counter = 0
      
        ## move right
        if selected_node > current_node.value:
          if current_node.right == None:
            current_node.right = binaryNode(selected_node)
            print("breaK right", current_node.right.value)
            break
          else:
            current_node = current_node.right
            counter += 1
            print("moving right", current_node.value)
        
        ## move left 
        print(selected_node, current_node.value)
        if selected_node < current_node.value:
          if current_node.left == None:
            current_node.left = binaryNode(selected_node)
            print("breaK Left", current_node.left.value)
            break
          else:
            current_node = current_node.left
            counter += 1
        
   
     
      
            

          
        
        

        

    


bt = binaryTree(a1)
bt.generateTree()
