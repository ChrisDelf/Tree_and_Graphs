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

/// travesing the tree

public void print_Tree() {
  System.out.println(this.sequence_arr);
  // going the need a stack
  ArrayList<Tree_node> stack = new ArrayList<Tree_node>();

  // want the append the root into our stack
  stack.add(this.root);
  

  while(stack.size() != 0){

    Tree_node current_node = stack.get(stack.size() -1);
    stack.remove(stack.size() - 1);
    System.out.println(current_node.getValue());
    if(current_node.getLeft() != null){
      stack.add(current_node.getLeft());

    }

    if(current_node.getRight() != null){
      stack.add(current_node.getRight());
    }

  if (stack.size() == 0) {
    break;
  }

  }
}
}
  // Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2 create an algorithm to determine if T2 is a subtree of T1.

  // A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree n is identical to T2 that is, if you cut off the tree a node n, the two trees would be identical

  public static void main(String[] args) {
    System.out.println("Hello world!");
  }