import java.util.ArrayList;

class Main {
  
// A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

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
//--------- Derpy --- // 
public class binary_tree {
  private Tree_node root;

public binary_tree() {}

public Tree_node getRoot() {
  return this.root;
}

public void setRoot(Tree_node node){
  this.root = node;
}

public void insert_node(int value){
 
if(this.root == null ){
  Tree_node new_node = new Tree_node(value);
  this.root = new_node;
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
      break;

    }
    else{
      current_node = current_node.getRight();
    }
}}}

/// travesing the tree

public void print_Tree() {

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



public static void main(String[] args) {
    Main main = new Main();
    main.run();

  }

public void run(){
    binary_tree tree = new binary_tree();
    tree.insert_node(3);
    tree.insert_node(2);
    tree.insert_node(5);
    tree.insert_node(1);
    tree.insert_node(6);
    tree.print_Tree();
}



}
