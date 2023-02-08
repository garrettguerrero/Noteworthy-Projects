#ifndef NODE_H
#define NODE_H

template <typename T>
class Node {
public:
  Node<T>* next;
  Node<T>* prev;
  T data;

  Node<T>() : data(T()), next(nullptr), prev(nullptr) {}
  Node<T>(const T& d) : data(d), next(nullptr), prev(nullptr) {}

  // getters
  T getData() {return data;}
  Node<T>* getNext() {return next;}
  Node<T>* getPrev() {return prev;}

  // setters
  void setData(const T& d) {data = d;}
  void setNext(Node* n) {next = n;}
  void setPrev(Node* p) {prev = p;}

};

#endif
