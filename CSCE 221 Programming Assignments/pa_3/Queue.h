#ifndef QUEUE_H
#define QUEUE_H

#include <iostream>
#include <sstream>
#include "DoublyLinkedList.h"

template <typename T>
class Queue {
public:
  Node<T>* back;
  Node<T>* front;
  int length;

  // constructor
  Queue<T>() : back(nullptr), front(nullptr), length(0) {}

  // destructor
  ~Queue<T>() {
    int temp = length;
    for (int i = 0; i < temp; i++) {
      //std::cout << "Popping: " << pop_front().data << std::endl;
      pop_front();
    }
  }

  // copy constructor
  Queue<T>(const Queue<T>& other) {}

  bool empty() {
    // if no elements in queue, return true
    if (length == 0)
      return true;
    else
      return false;
  }

  void push_back(T data) {
    Node<T>* to_insert = new Node<T>(data);

    // if there are no elements in the list, set up front and back
    if (back == nullptr && length == 0) {
      back = to_insert;
      front = to_insert;
      length++;
      return;
    }

    // slide new node into the list and update back
    to_insert -> prev = back;
    back = to_insert;
    (back -> prev) -> next = back;
    length++;

  }


  T pop_front() {
    if (front == nullptr) {
      throw std::out_of_range("index outside of list bounds");
    }

    T data_to_return = front -> data;

    // if there is only one element left in the list, update pointers to null
    if (length == 1) {
      delete front;
      front = nullptr;
      back = nullptr;
      length--;
      return data_to_return;
    }

    // give front to the next node and delete the previous pointer
    Node<T>* temp = front;
    front = front -> next;
    delete temp;
    length--;
    return data_to_return;

  }

  std::string toString() {
    std::stringstream node_info;

    // output node data into a string stream
    Node<T>* current_node = front;
    while (current_node != nullptr) {
      node_info << current_node -> data << ' ';

      current_node = current_node -> next;
    }

    // convert stringstream to string and return
    return node_info.str();
  }


};


#endif
