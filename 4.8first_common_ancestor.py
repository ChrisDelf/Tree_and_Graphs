## 4.8 First Common Ancestor: Design an algorithmn and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: this is not necessarily a binary search tree.


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

  def find_commmon_an(self, value1, value2):
    ## going to start at the root   
    current_node = self.root

    ## the plan is to find the nodes locations and work up from there
    anc1 = None
    anc2 = None
    values_arr = [value1, value2]
    ## going to record the parents of located nodes
    node_arr = []
    x = 0
    while current_node:

      ## if the current value is less that input value we left:
      if current_node.value > values_arr[x]:
        ## if current_node.left is none then we have to create a new node
        if current_node.left == None:
          ## we have reach the end of our options and the node does not exist
          return False
        else:
          current_node = current_node.left  
      if current_node.value == values_arr[x]:
        ## we have found a node and now we should store iter
        node_arr.append(current_node)
        x += 1
        ## need to reset the tree so we move back to root
        current_node = self.root
        if x == 2:
          break
      ## now for the right cases
      if current_node.value < values_arr[x]:

       
        if current_node.right == None:
          ## we have not found the node return false
          return False

        ##  now its safe to move to the right
        else:
          current_node = current_node.right
    
    ## once we have located the nodes now it is time to compare parents
    ## problems what if node1 is the child of node2 
      ## in that case we common ancestor is the parent of node2 
      ## can do the same for the other way around
    common_anc = None
    current_anc = None
    target_anc = None
    current_anc = None
    while common_anc == None:
      ## we can do a quick check if the node exists on either side of the the tree then common ancestor should be the root
      if node_arr[0].value < self.root.value and  node_arr[1].value > self.root.value:
        common_anc = self.root
        break
      if node_arr[0].value > self.root.value and  node_arr[1].value < self.root.value:
        common_anc = self.root
        break
      
      if node_arr[0].value > node_arr[1].value:
        if node_arr[0].parent.value == node_arr[1].parent.value:
          common_anc = node_arr[0].parent
          break
        ## now we should check if node_arr[0] is the parent of node_arr2
        if node_arr[0].value == node_arr[1].parent.value:
          common_anc = node_arr[0].parent
          break
        target_anc = node_arr[0].parent
        current_anc = node_arr[1].parent
    
    
      if node_arr[0].value < node_arr[1].value:
      
        if node_arr[0].parent.value == node_arr[1].parent.value:
          common_anc = node_arr[0].parent
          break
      ## now we should check if node_arr[0] is the parent of node_arr2
        if node_arr[0].value == node_arr[1].parent.value:
          common_anc = node_arr[0].parent
          break
        target_anc = node_arr[1].parent
        ## now we have exhausted the edge cases we must iter rate through until we find   a common ancestor
        current_anc = node_arr[0].parent

      while current_anc:
        if current_anc.value == target_anc.value:
          ## we have found a common anc
            common_anc = target_anc
            break
        ## if this occurs then current becomes target and target becomes current
        if current_anc.value < target_anc.value:
          ## checking the right
          if current_anc.right != None:
            if current_anc.right.value == target_anc.value:
              common_anc = current_anc
              break
        if current_anc.value == self.root.value:
          common_anc = self.root
          break 
        if current_anc.parent.value == target_anc.value:
          common_anc = current_anc
          break
        ## if neither of these are true then we will move to the next node
        else:
          current_anc = current_anc.parent

        if current_anc.value > target_anc.value:
          ## checking the right
          if current_anc.left != None:
            if current_anc.left.value == target_anc.value:
              common_anc = target_anc
              break
        if current_anc.value == self.root.value:
          common_anc = self.root
          break     
        ## if we do not have a right then we check parent
        if current_anc.parent.value == target_anc.value:
          common_anc = target_anc
          break
                ## if neither of these are true then we will move to the next node
        else:
          current_anc = current_anc.parent

        target_anc = target_anc.parent

      ## want want to check if the current_anc is not the same as teh common anc1

    for x in node_arr:
      if x.value == common_anc.value:
        common_anc = common_anc.parent
      
          
        


    

    return common_anc.value


    



test_tree = binaryTree()

test_tree.insertNode(7)
test_tree.insertNode(3)
test_tree.insertNode(4)
test_tree.insertNode(11)
test_tree.insertNode(10)
test_tree.insertNode(8)
test_tree.insertNode(2)
test_tree.insertNode(6)
test_tree.insertNode(5)
test_tree.insertNode(1)
test_tree.insertNode(9)
test_tree.insertNode(12)

test_tree.printTree()
print(test_tree.find_commmon_an(9,12))
