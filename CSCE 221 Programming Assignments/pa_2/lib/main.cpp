#include "BST.hpp"

int main() {
  BST<int, int> tree;
  tree.insert(5, 1);
  tree.insert(6, 2);
  tree.insert(4, 3);
  tree.print();
  //tree.removeNode(7);
  return 0;
}
