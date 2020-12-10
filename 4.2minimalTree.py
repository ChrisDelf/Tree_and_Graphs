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

    left_array= temp_a[pivot:]
    print(left_array)
  
    ## getting the left side mide point
    left_midpoint = len(left_array) % 2
    if left_midpoint == 1:
      left_midpoint = round(len(left_array)/2)
    if left_midpoint == 0:
      left_midpoint = (len(left_array) / 2)
      left_midpoint = int(left_midpoint)

    self.root.left = binaryNode(left_array[left_midpoint])

    ##  right
    right_array = temp_a[:pivot]
    right_array.pop()
    print(right_array)

    right_midpoint = len(left_array) % 2

    if right_midpoint == 1:
      right_midpoint = round(len(right_array)/2)
    if right_midpoint == 0:
      right_midpoint = (len(right_array)/2)
      right_midpoint = int(right_midpoint)
    self.root.right = binaryNode(right_array[right_midpoint])

    print("left", self.root.left.value,"our Root", self.root.value, "right", self.root.right.value)

    while i < len(left_array) - 2:
      
      i+= 1


bt = binaryTree(a1)
bt.generateTree()
