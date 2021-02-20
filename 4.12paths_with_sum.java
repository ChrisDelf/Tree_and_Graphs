import java.util.ArrayList;
import java.util.*;

class Main {
  public class Tree_node{
private Tree_node parent;
private int value;
private Tree_node left;
private Tree_node right;

public Tree_node() {}

public Tree_node(int value) {this.value = value;
}

public int getValue() {
  return value;
}

public void setValue(int value ){
  this.value = value;
}

public Tree_node getRight() {
  return right;
}

public void setRight(Tree_node node){
  this.right = node;

}

public Tree_node getLeft() {
  return this.left;
}

public void setLeft(Tree_node node) {
  this.left = node;
}

public Tree_node getParent(){
  return parent;
}

public void setParent(Tree_node node) {
  this.parent = node;
}
}
//--------- Binary Tree Class--- // 
public class binary_tree {
  private Tree_node root;
  private ArrayList<Integer> sequence_arr = new ArrayList<Integer>();


public binary_tree() {}

public Tree_node getRoot() {
  return this.root;
}

public ArrayList<Integer> getSequence(){

  return this.sequence_arr;
}

public void addSequence(int node){
  this.sequence_arr.add(node);
}

public void setRoot(Tree_node node){
  this.root = node;
}

// <-------- Inserting a node------- >
public void insert_node(int value){
 
if(this.root == null ){
  Tree_node new_node = new Tree_node(value);
  this.root = new_node;
  this.sequence_arr.add(new_node.getValue());
  return;
}

// now its time to insert node from left to right lets setup our vairables
Tree_node current_node = this.root;

while(current_node != null){

  if (current_node.getValue() > value){
    
    if(current_node.getLeft() == null){
       
      Tree_node new_node = new Tree_node(value);
      new_node.setParent(current_node);
      current_node.setLeft(new_node);
      this.sequence_arr.add(new_node.getValue());
      break;

    }
    else{
      current_node = current_node.getLeft();
    }
  }
   if (current_node.getValue() < value){
    
    if(current_node.getRight() == null){
       
      Tree_node new_node = new Tree_node(value);
      new_node.setParent(current_node);
      current_node.setRight(new_node);
      this.sequence_arr.add(new_node.getValue());
      break;

    }
    else{
      current_node = current_node.getRight();
    }
}}}
}
// Paths with sum: You are given a binary tree in which each node contains an integer value (which might be positive or negative). Desing an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or leaf, but it must go downwards (raveling only from parent nodes to child node).
public boolean paths_with_sum(binary_tree T1, int input){
System.out.println(T1.root.value + input);
  if (T1.root == null )
  {
    return false;
  }
 // if (input > T1.root.value){
   // return false;
//  }
  if (input == T1.root.value){
    return true;
  }
  // first thing we can sub track from the sum in the root of the tree:
  int current_sum = T1.root.value - input; 
  System.out.println(current_sum);
  return true;
}





  public void run(){
    System.out.println("are we running");
    binary_tree Tree = new binary_tree();
    Tree.insert_node(14);
    Tree.insert_node(7);
    Tree.insert_node(9);
    Tree.insert_node(2);
    Tree.insert_node(5);
    Tree.insert_node(1);
    Tree.insert_node(23);
    Tree.insert_node(18);
    Tree.insert_node(15);
    Tree.insert_node(22);
    System.out.println(Tree);
    
    System.out.print(paths_with_sum(Tree, 5));



  }
  public static void main(String[] args) {
    Main main = new Main();
  
    main.run();
  }
}
