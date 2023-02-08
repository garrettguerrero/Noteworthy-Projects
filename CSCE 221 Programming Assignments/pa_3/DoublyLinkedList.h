#ifndef DOUBLYLINKEDLIST_H
#define DOUBLYLINKEDLIST_H

#include <iostream>
#include <string>
#include "Node.h"

template <typename T>
class DoublyLinkedList {

public:

	Node<T>* head;
	Node<T>* tail;
  int length;

	// Default constructor
	DoublyLinkedList();

	// Destructor
	~DoublyLinkedList();

	// Copy constructor
	DoublyLinkedList(const DoublyLinkedList<T>& other);

	// Copy assignment
	DoublyLinkedList<T>& operator=(const DoublyLinkedList<T>& other);

  // getters
  int getLength() {return length;}
  Node<T>* getFront() {return head;}
  Node<T>* getBack() {return tail;}

  // inserts a node at a given index
  void insert(T data, int index);

  // removes a node from the list
  T remove(int index);

  // converts list data into a string
  std::string toString();

};

#endif
