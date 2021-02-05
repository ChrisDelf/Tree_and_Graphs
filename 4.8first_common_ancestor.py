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
}



public static void main(String[] args) {
    Main main = new Main();
    main.run();

  }

public void run(){
    Tree_node new_node = new Tree_node(3);
    System.out.println(new_node.getValue());
}



}
