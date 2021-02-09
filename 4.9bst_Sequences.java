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
// A binary search tree was created by traversing through an array from left to right and inserting each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.
// we know that the first element has to zero.


public ArrayList<LinkedList<Integer>> sequences(Tree_node node) {
  ArrayList<LinkedList<Integer>> result = new ArrayList<LinkedList<Integer>>();

  if(node == null){
    result.add(new LinkedList<Integer>());
    return result;
  }
 LinkedList<Integer> prefix = new LinkedList<Integer>();
 prefix.add(node.value);

 // Recurse on left and right subtrees
  ArrayList<LinkedList<Integer>> leftSeq = sequences(node.left);
  ArrayList<LinkedList<Integer>> rightSeq = sequences(node.right);

  // Weave each list from the left and right sides.
  for (LinkedList<Integer> left : leftSeq) {
    for (LinkedList<Integer> right: rightSeq){
      ArrayList<LinkedList<Integer>> weaved = new ArrayList<LinkedList<Integer>>();
      weaveList(left, right, weaved,prefix);
    result.addAll(weaved);
    }
  }
return result;
}
// now we create the function to weave the lists together in all possible ways. This algorithm works by removing the head from one list, recursing and doing the same thing with the other list.

public void weaveList(LinkedList<Integer> first,  LinkedList<Integer> second,  ArrayList<LinkedList<Integer>> results, LinkedList<Integer> prefix){
  // One list is empty. add remainder to [a clone] prefix and store result.
  
  if(first.size() <= 0 || second.size() <= 0){
    LinkedList<Integer> result = (LinkedList<Integer>) prefix.clone();
    result.addAll(first);
    result.addAll(second);
    results.add(result);
    return;

  }
  //Recurse with head of the first added to the prefix. Removing the head will damage first, so we'll need ot put it back where we found it afterwards.
int head_First = first.removeFirst();
prefix.addLast(head_First);
weaveList(first, second, results, prefix);
prefix.removeLast();
// we put it back
first.addFirst(head_First);


// we have to do the same thing to the second array
if (second.size() == 0){
  return;
}
int head_second = second.removeFirst();
prefix.addLast(head_second);
weaveList(first, second, results, prefix);
prefix.removeLast();
// we put it back
first.addFirst(head_second);
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
    tree.insert_node(4);
    tree.print_Tree();
    System.out.println(tree.sequences(tree.root));
}



}
