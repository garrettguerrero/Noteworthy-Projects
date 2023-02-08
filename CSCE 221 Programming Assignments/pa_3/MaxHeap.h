#ifndef MAXHEAP_H
#define MAXHEAP_H

#pragma once

#include "DNode.h"
#include <iostream>
#include <string>
#include <vector>

using std::vector;

template <typename T>
class MaxHeap {
public:

  // vector holds the values of the heap
  vector<T> nodes;

  // constructors
  MaxHeap() {}
  MaxHeap(vector<T> node_list) : nodes(node_list) {
    heapify();
  }

  // given an index, use some magic math to determine where the parent and children are
  int getParent(int curr) const {return (curr - 1) / 2;}
  int getLeft(int curr) const {return 2 * curr + 1;}
  int getRight(int curr) const {return 2 * curr + 2;}

  // if the list is empty, so is the heap
  bool empty() const {
    if (nodes.size() == 0) return true;
    else return false;
  }

  // define some functions
  void upheap(int node);
  void downheap(int node);
  void heapify();
  void insert(T to_insert);
  T removeMax();
};

template <typename T>
void MaxHeap<T>::upheap(int node) { // recursively check the parent's value and swap if it is greater than the current node

  if (getParent(node) < 0) return;

  if (nodes.at(node) > nodes.at(getParent(node))) {
    std::swap(nodes[node], nodes[getParent(node)]);
    upheap(getParent(node));
  }
  return;
}

template <typename T>
void MaxHeap<T>::downheap(int node) { // recursively check each child and swap if they are greater than the current node

  if (!(getLeft(node) >= nodes.size()) && nodes.at(node) < nodes.at(getLeft(node))) {
    std::swap(nodes[node], nodes[getLeft(node)]);
    downheap(getLeft(node));
  }
  if (!(getRight(node) >= nodes.size()) && nodes.at(node) < nodes.at(getRight(node))) {
    std::swap(nodes[node], nodes[getRight(node)]);
    downheap(getRight(node));
  }
  return;
}

template <typename T>
void MaxHeap<T>::heapify() { // starting from the last parent, check each child and ensure heap is properly sorted
  int parent = getParent(nodes.size() - 1);
  for (int i = parent; i >= 0; i--) {
    downheap(i);
  }
}

template <typename T>
void MaxHeap<T>::insert(T to_insert) { // push a value to the back of the list and move it up the heap if necessary
  nodes.push_back(to_insert);
  upheap(nodes.size() - 1);
}

template <typename T>
T MaxHeap<T>::removeMax() { // swap first value with last, then remove the value and move the swapped value down the heap.
  T temp = nodes.at(0);
  std::swap(nodes.at(0), nodes.at(nodes.size() - 1));
  nodes.pop_back();
  downheap(0);
  return temp;
}

#endif

template <typename T>
vector<T> heapsort(vector<T> v) { // remove each value, pushing each value onto a vector, and return the vector.
  MaxHeap<T> h(v);
  vector<T> new_vect;
  for (int i : h.nodes) {
    new_vect.push_back(h.removeMax());
  }
  return new_vect;
}

template class MaxHeap<int>;
