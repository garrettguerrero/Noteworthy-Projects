#ifndef NODE_H
#define NODE_H
#include "NetworkPacket.h"

class Node {
public:
  Node* next;
  Node* prev;
  NetworkPacket data;


  Node() : data(NetworkPacket()), next(nullptr), prev(nullptr) {}
  Node(const NetworkPacket& d) : data(d), next(nullptr), prev(nullptr) {}

  // getters
  NetworkPacket getData() {return data;}
  Node* getNext() {return next;}
  Node* getPrev() {return prev;}

  // setters
  void setData(const NetworkPacket& d) {
    data = d;
  }

  void setNext(Node* n) {
    next = n;
  }
  void setPrev(Node* p) {
    prev = p;
  }

};

#endif
