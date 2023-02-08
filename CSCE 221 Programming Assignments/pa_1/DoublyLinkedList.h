#include <iostream>
#include <string>
#include "Node.h"

class DoublyLinkedList {
public:
//private:
	Node* head;
	Node* tail;
  int length;

//public:
	// Default constructor
	DoublyLinkedList();

	// Destructor
	~DoublyLinkedList();

	// Copy constructor
	DoublyLinkedList(const DoublyLinkedList& other);

	// Copy assignment
	DoublyLinkedList& operator=(const DoublyLinkedList& other);

  // getters
  int getLength() {return length;}
  Node* getFront() {return head;}
  Node* getBack() {return tail;}

  // inserts a node at a given index
  void insert(NetworkPacket data, int index);

  // removes a node from the list
  NetworkPacket remove(int index);

  // converts list data into a string
  std::string toString();


};
